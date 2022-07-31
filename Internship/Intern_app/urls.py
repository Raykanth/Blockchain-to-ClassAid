from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.HOME,name='home'),
    path('Teacher-Loginpage',views.TEACHER_LOGIN,name='teacher-login'),
    path('Student-Loginpage',views.STUDENT_LOGIN,name='student-login'),

    path('Teacher-Loginpage-Courses',views.TEACHER,name='teacher'),
    path('Student-Loginpage-Courses',views.STUDENT,name='student'),

    path('Teacher-Loginpage-Courses-Ass_Mat-<int:id>',views.TEACHER_1,name='teacher_1'),
    path('Student-Loginpage-Courses-Ass_Mat-<int:id>',views.STUDENT_1,name='student_1'),
    
    path('Teacher-Loginpage-Courses-Assignment-<int:id>',views.TEACHER_ASS_DETAILS,name='teacher_2_ass'),
    path('Student-Loginpage-Courses-Assignment-<int:id>',views.STUDENT_ASS_DETAILS,name='student_2_ass'),

    path('Teacher-Loginpage-Courses-Assignment-Marks',views.TEACHER_ASS_MARKS,name='teacher_2_ass_marks'),
    path('Student-Loginpage-Courses-Assignment-Correction',views.STUDENT_ASS_CORRECTION,name='student_2_ass_correction'),

    path('Teacher-Loginpage-Courses-Assignment-Marks-Checking',views.TEACHER_ASS_MARKS_CHECK,name='teacher_2_ass_marks_check'),
]