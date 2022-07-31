from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Login_Teacher),
admin.site.register(Login_Student),
admin.site.register(Teacher_Course),
admin.site.register(Student_Course),
admin.site.register(Course_Details),
admin.site.register(Assignment_Details),
admin.site.register(ReadingMaterial_Details),
admin.site.register(Students_Ass_Submission),
admin.site.register(Marks)
