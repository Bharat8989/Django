# from django.contrib import admin
# from .models import Student,Teacher

# admin.site.register(Student)
# admin.site.register(Teacher)


# admin.py

from django.contrib import admin
from .models import Student,Teacher



# class Teacher(admin.ModelAdmin):
#     list_display = ("id", "name", "age", "city")

# admin.site.register(Student, Teacher)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "city")
    search_fields = ("name", "city", "age")
    list_filter = ("city", "age")
    ordering = ("name",)

    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "city")