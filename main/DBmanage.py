import sqlite3

conn = sqlite3.connect('CS.sqlite')
cursor = conn.cursor()

# -------------------------------------
# Запрос для поиска курса по параметрам
# -------------------------------------
def findCourse(categ):
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
                                    ON t2.id = ft2.Tag_id
                                WHERE _category LIKE ? 
                                GROUP BY t2.title, Courses.id
                                ORDER BY strftime('%Y-%m-%d', date);""", (categ,))

    res = cursor.fetchall()

    for s in res:
        print("Название курса:", s[0])
        print("Описание:", s[3])
        print("Категория:", s[1])
        print("Автор:", s[2])
        print("Дата публикации:", s[4])
        print("Тэги:", s[5])
        print("================================")

