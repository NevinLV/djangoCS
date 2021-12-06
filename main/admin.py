from django.contrib import admin
from .models import Authors
from .models import Categories
from .models import CourseTag
from .models import CourseUser
from .models import Courses
from .models import Img
from .models import Users
from .models import Tags
from .models import Video

admin.site.register(Authors)
admin.site.register(Categories)
admin.site.register(CourseTag)
admin.site.register(CourseUser)
admin.site.register(Courses)
admin.site.register(Img)
admin.site.register(Users)
admin.site.register(Tags)
admin.site.register(Video)
