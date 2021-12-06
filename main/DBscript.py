import sqlite3

conn = sqlite3.connect('CS.sqlite')
cursor = conn.cursor()


# -----------------------------------------
# Запрос для добавления нового пользователя
# -----------------------------------------
def addUser():
    isExists = True

    print("Введите имя: ", end='')
    inName = input()

    # Проверка на наличие адреса электронной почты в базе
    while isExists:
        print("Адрес электронной почты: ", end='')
        inEmail = input()

        info = cursor.execute('SELECT * FROM Users WHERE email =?', (inEmail,))
        if info.fetchone() is None:
            isExists = False
        else:
            print("Данный адрес электронной почты уже занят. Введите другой адрес.")

    print("Пароль: ", end='')
    inPassword = input()

    cursor.execute("INSERT INTO Users(name, email, password) VALUES (?, ?, ?);", (inName, inEmail, inPassword,))
    conn.commit()
    print("Пользователь успешно зарегистрирован!")


# ----------------------------------
# Запрос для добавления нового курса
# ----------------------------------
def addCourse():
    print("Название курса: ")
    cInTitle = input()

    print("Описание: ")
    cInDesc = input()

    isExists = True
    while isExists:
        print("Ваша электронная почта: ")
        cInEmail = input()

        info = cursor.execute('SELECT * FROM Users WHERE email =?', (cInEmail,))
        if info.fetchone() is None:
            print("Вас не существует. Используйте другой адрес или зарегистрируйтесь.")
        else:
            cursor.execute("SELECT id, name FROM Users WHERE email = ?", (cInEmail,))
            res = cursor.fetchall()

            cInUserId = int(res[0][0])
            cInUserName = res[0][1]

            info = cursor.execute('SELECT * FROM Authors WHERE User_id =?', (cInUserId,))
            if info.fetchone() is None:
                cursor.execute("INSERT INTO Authors(name, User_id) VALUES (?, ?);", (cInUserName, cInUserId,))
                conn.commit()

            cursor.execute("SELECT id FROM Authors WHERE User_id = ?;", (cInUserId,))
            res = cursor.fetchall()
            cInAuthor = int(res[0][0])

            isExists = False

    print("Категория: ")
    cInCategory = input()
    cursor.execute("SELECT id FROM Categories WHERE title = ?", (cInCategory,))
    res = cursor.fetchall()
    cInCategory = int(res[0][0])

    cursor.execute("""INSERT INTO Courses(title, description, Author_id, Category_id, date) 
                        VALUES (?, ?, ?, ?, strftime('%Y-%m-%d','now'));""",
                   (cInTitle, cInDesc, cInAuthor, cInCategory,))
    conn.commit()

    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name = 'Categories'")
    courseId = cursor.fetchall()

    print("Теги (через запятую): ")
    Tags = []
    Tags = input().split(', ')
    for t in Tags:
        info = cursor.execute('SELECT id FROM Tags WHERE title = ?', (t,))
        tagId = info.fetchone()
        if tagId is None:
            cursor.execute("INSERT INTO Tags(title) VALUES (?);", (t,))
            cursor.execute("SELECT seq FROM sqlite_sequence WHERE name = 'Tags'")
            tagId = cursor.fetchall()

        cursor.execute("INSERT INTO Course_Tag(Tag_id, Course_id) VALUES (?, ?);",
                       (int(tagId[0]), int(courseId[0][0]),))
        conn.commit()

    print("Курс успешно добавлен!")

# -------------------------------------
# Запрос для поиска курса по параметрам
# -------------------------------------
def findCourse():
    print("Название курса: ")
    cTitle = f"%{input()}%"

    print("Описание: ")
    cDesc = f"%{input()}%"

    print("Автор: ")
    cAuthor = f"%{input()}%"

    print("Категория: ")
    cCategory = f"%{input()}%"

    print("Дата публикаии (YYYY-MM-DD), начиная с: ")
    cDate = input()

    print("Теги (через запятую): ")
    _TagsFilter = 'AND t2.title IN ('

    Tags = input().split(', ')

    # Создаём дополнительное условие для фильтрации по нескольким тегам
    # (Пришлось сделать в виде строки, т.к. других способ вставить этот кусок в запрос я не нашёл)
    isFirst = True
    for t in Tags:
        if isFirst:
            _TagsFilter += f"'{t}'"
            isFirst = False
        else:
            _TagsFilter += f", '{t}'"
    _TagsFilter += ")"

    # Если нет тегов - нет фильтра
    if Tags == ['']:
        _TagsFilter = ''

    cursor.execute(f"""SELECT DISTINCT Courses.title,
                                (SELECT title FROM Categories WHERE Category_id = id) AS _category,
                                (SELECT name FROM Authors WHERE Author_id = id) AS _author,
                                description,
                                date,
                                group_concat(t1.title,  ', ') AS _tag
                                FROM Courses
                                JOIN Course_Tag ft1
                                    ON ft1.Course_id= Courses.id
                                JOIN Tags t1
                                    ON t1.id = ft1.Tag_id
                                JOIN Course_Tag ft2
                                    ON ft2.Course_id = Courses.id
                                JOIN Tags t2
                                    ON t2.id = ft2.Tag_id {_TagsFilter}
                                WHERE Courses.title LIKE ? AND
                                      description LIKE ? AND
                                      _author LIKE ? AND
                                      _category LIKE ? AND
                                      strftime('%Y-%m-%d',date) >= ?
                                GROUP BY t2.title, Courses.id
                                ORDER BY strftime('%Y-%m-%d', date);""", (cTitle, cDesc, cAuthor, cCategory, cDate,))

    res = cursor.fetchall()

    for s in res:
        print("Название курса:", s[0])
        print("Описание:", s[3])
        print("Категория:", s[1])
        print("Автор:", s[2])
        print("Дата публикации:", s[4])
        print("Тэги:", s[5])
        print("================================")


# -----------------------------
# Запрос для показа всех курсов
# -----------------------------
def showCourse():
    cursor.execute("""SELECT Courses.title,
                   (SELECT title FROM Categories WHERE Category_id = id) AS _category, 
                   (SELECT name FROM Authors WHERE Author_id = id) AS _author, 
                   description, 
                   date, 
                   group_concat(t1.title, ', ') AS _tag 
                   FROM Courses 
                       JOIN Course_Tag ft1 
                            ON ft1.Course_id= Courses.id 
                       JOIN Tags t1 
                            ON t1.id = ft1.Tag_id 
                   GROUP BY Courses.id;""")

    for s in cursor.fetchall():
        print("Название курса:", s[0])
        print("Описание:", s[3])
        print("Категория:", s[1])
        print("Автор:", s[2])
        print("Дата публикации:", s[4])
        print("Тэги:", s[5])
        print("================================")


# ---------------------------
# Меню
# ---------------------------
while True:
    print("Выберите действие:\n"
          "<1> Добавить нового пользователя \n"
          "<2> Вывести все курсы и данные о них \n"
          "<3> Поиск \n"
          "<4> Добавить курс\n"
          "<0> ВЫХОД")

    menu = int(input())
    if menu == 1:
        addUser()
    elif menu == 2:
        showCourse()
    elif menu == 3:
        findCourse()
    elif menu == 4:
        addCourse()
    elif menu == 0:
        conn.close()
        break

    print("\n")
