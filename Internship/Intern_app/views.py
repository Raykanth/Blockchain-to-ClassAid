from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import *
from .forms import *
import pyautogui,random

global Teacher_id,Student_id,data_SUBMISSIONS,main;o=0
def HOME(request):
    return render(request,'Intern_app/Home.html')

def TEACHER_LOGIN(request):
    global Teacher_id
    data_TL=Login_Teacher.objects.all()
    if request.method == "POST":
        Teacher_id = request.POST['Uname']
        Teacher_password = request.POST['Pass']   
        n=int(data_TL.count())
        for a in range(n):
            if  Teacher_id==data_TL[a].Teacher_name:
                if Teacher_password==data_TL[a].Teacher_pass:
                    return HttpResponseRedirect("Teacher-Loginpage-Courses")
    return render(request,'Intern_app/Login.html')

def STUDENT_LOGIN(request):
    global Student_id,o
    data_SL=Login_Student.objects.all()
    if request.method == "POST":
        Student_id = request.POST['Uname']
        Student_password = request.POST['Pass']   
        n=int(data_SL.count())
        for a in range(n):
            if  Student_id==data_SL[a].Student_name:
                if Student_password==data_SL[a].Student_pass:
                    o=o+1
                    return HttpResponseRedirect("Student-Loginpage-Courses")
    return render(request,'Intern_app/Login.html')

def TEACHER(request):
    data = Teacher_Course.objects.filter(Teacher_name= Teacher_id)
    if request.method == "POST":
        newcourse = request.POST['coursename']
        a=Course_Details(
            Course_name=newcourse,
            Assignments=0,
            Reading_Materials=0
        )
        a.save()
        AB=Teacher_Course(
            Teacher_name= Teacher_id,
            Course_name=newcourse
        )
        AB.save()
        
    return render(request,'Intern_app/Teacher.html',{
        "COURSES":data,
    })

def STUDENT(request):
    global Student_id 
    if request.user.is_authenticated and o == 0:
        Student_id = request.user.username
    print(Student_id)
    count=0
    # global Student_id
    # if request.user.is_authenticated:
    #     Student_id = request.user.username;
    #     if request.method == "POST":
    #         Student_password = request.POST['psw'] 
    #         a=Login_Student(
    #             Student_name=Student_id,
    #             Student_pass=Student_password,
    #         )
    #         a.save()  
    # else:
    #     if request.method == "POST":
    #         Student_password = request.POST['psw'] 
    #         a=Login_Student.objects.get(Student_name=Student_id)    
    #         a.Student_pass=Student_password
    #         a.save(update_fields=["Student_pass"])
    #         a.save() 
    data = Student_Course.objects.filter(Student_name= Student_id)
    data_CD = Course_Details.objects.all()
    if request.method == "POST":
        newcourse = request.POST['coursename']
        n=int(data_CD.count())
        for a in range(n):
            if  newcourse==data_CD[a].Course_name:
                count=count+1
                AB=Student_Course(
                    Student_name= Student_id,
                    Course_name=newcourse
                )
                AB.save()
        if count==0:
            pyautogui.alert('NO COURSE DETECTED')
    return render(request,'Intern_app/Student.html',{
        "COURSES":data,"s_id":Student_id
    })

def TEACHER_1(request,id):
    data = Teacher_Course.objects.filter(pk=id)
    if request.method == 'POST':  
        new_ass = new_asssignment(request.POST, request.FILES) 
        if new_ass.is_valid():  
            new_ass.save()
            a=Assignment_Details.objects.get(Course_name="")
            a.Course_name=data[0].Course_name
            a.Assignment_id=request.POST['ass_title']
            a.Assignment_instructions=request.POST['ass_instructions']
            a.save(update_fields=["Course_name","Assignment_id","Assignment_instructions"])
            a.save() 
    if request.method == 'POST':  
        new_rea = new_material(request.POST, request.FILES)  
        if new_rea.is_valid():  
            new_rea.save()
            a=ReadingMaterial_Details.objects.get(Course_name="")
            a.Course_name=data[0].Course_name
            a.ReadingMaterial_id=request.POST['rea_title']
            a.ReadingMaterial_instructions=request.POST['rea_instructions']
            a.save(update_fields=["Course_name","ReadingMaterial_id","ReadingMaterial_instructions"])
            a.save() 
    data_CD = Course_Details.objects.all()
    l=data_CD.count()
    for a in range(l):
        if  data_CD[a].Course_name==data[0].Course_name:
            data_1 = Assignment_Details.objects.filter(Course_name = data[0].Course_name)
            data_2 = ReadingMaterial_Details.objects.filter(Course_name = data[0].Course_name)
    new_ass=new_asssignment()
    new_mat=new_material()
    return render(request,'Intern_app/Teacher_1.html',{
        "ass":data_1,"rea":data_2,"new_ass":new_ass,"new_mat":new_mat
    })

def STUDENT_1(request,id):
    global Student_id
    data = Student_Course.objects.filter(pk=id)
    data_CD = Course_Details.objects.all()
    l=data_CD.count()
    for a in range(l):
        if  data_CD[a].Course_name==data[0].Course_name:
            data_1 = Assignment_Details.objects.filter(Course_name = data[0].Course_name)
            data_2 = ReadingMaterial_Details.objects.filter(Course_name = data[0].Course_name)
    return render(request,'Intern_app/Student_1.html',{
        "ass":data_1,"rea":data_2
    })

def TEACHER_ASS_DETAILS(request,id):
    global data_SUBMISSIONS
    data=Assignment_Details.objects.get(pk=id)
    data_S=Student_Course.objects.filter(Course_name=data.Course_name)
    data_SUBMISSIONS=Students_Ass_Submission.objects.filter(Course_name=data.Course_name,Assignment_id=data.Assignment_id)
    name=data_S.values_list('Student_name', flat=True)
    name1=data_SUBMISSIONS.values_list("Student_name", flat=True)
    data_un=[]
    for a in name:
        if a not in name1:
            data_un.append(a)
    aa=Marks.objects.filter(Course_name=data.Course_name,Assignment_id=data.Assignment_id)
    if aa.exists() :
        bb="True"
    else: 
        bb="False"
    return render(request,'Intern_app/Teacher_2_Ass.html',{
        "ass":data,"students":data_S,"submissions":data_SUBMISSIONS,"unsub":data_un,"aa":bb
    })

def STUDENT_ASS_DETAILS(request,id):
    global main,Student_id,data_SUBMISSIONS
    data=Assignment_Details.objects.get(pk=id)
    data_SUBMISSIONS=Students_Ass_Submission.objects.filter(Course_name=data.Course_name,Assignment_id=data.Assignment_id)

    bb="True"
    try:
        q=Students_Ass_Submission.objects.get(Student_name=Student_id,Course_name=data.Course_name,Assignment_id=data.Assignment_id)
    except Students_Ass_Submission.DoesNotExist:
        q=None
        bb="False"
    main=data
    if request.method == 'POST':  
        form = ass_submission(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()
            a=Students_Ass_Submission.objects.get(Student_name="")
            a.Student_name=Student_id
            a.Assignment_id=data.Assignment_id
            a.Course_name=data.Course_name
            a.save(update_fields=["Student_name","Assignment_id","Course_name"])
            a.save()
    form=ass_submission()
    return render(request,'Intern_app/Student_2_Ass.html',{
        "ass":data,"ass_form":form,"q":q,"b":bb
    })

def TEACHER_ASS_MARKS(request):
    global data_SUBMISSIONS
    l=data_SUBMISSIONS.count()
    aa=Marks.objects.filter(Course_name=data_SUBMISSIONS[0].Course_name,Assignment_id=data_SUBMISSIONS[0].Assignment_id).delete()
    list=[]
    list1=[]
    lis=[]
    list2=[]
    li=[]
    list3=[]
    while len(list) < l or len(lis) < l or len(li) < l:
        r=random.randint(1,l)
        s=random.randint(1,l)
        t=random.randint(1,l)
        if r not in list and r !=len(list)+1: 
            list.append(r)
            list1.append(data_SUBMISSIONS[r-1])
        if s not in lis and s !=len(lis)+1: 
            lis.append(s)
            list2.append(data_SUBMISSIONS[s-1])
        if t not in li and t !=len(li)+1: 
            li.append(t)
            list3.append(data_SUBMISSIONS[t-1])
    for i in range(l):
        a=Marks(
            Student_name=data_SUBMISSIONS[i].Student_name,
            Course_name=data_SUBMISSIONS[i].Course_name,
            Assignment_id=data_SUBMISSIONS[i].Assignment_id,
            Content=data_SUBMISSIONS[i].Submission_content,
            Person1_name=list1[i].Student_name,
            Marks1=0,
            Person2_name=list2[i].Student_name,
            Marks2=0,
            Person3_name=list3[i].Student_name,
            Marks3=0
        )
        a.save()
    # print(data_SUBMISSIONS[0].Student_name)
    # print("q")
    # print(list1)
    # print("q")
    # print(list2)
    # print("q")
    # print(list3)



    dat=Marks.objects.filter(Course_name=data_SUBMISSIONS[0].Course_name,Assignment_id=data_SUBMISSIONS[0].Assignment_id)
    print(data_SUBMISSIONS[0].Course_name)
    print(data_SUBMISSIONS[0].Assignment_id)
    return render(request,'Intern_app/Teacher_2_Ass_Marks.html',{
        "data":dat
    })

def STUDENT_ASS_CORRECTION(request):
    global Student_id,data_SUBMISSIONS
    if request.method == 'POST':  
        m1 = marks1(request.POST) 
        a=Marks.objects.get(Person1_name=Student_id,Course_name=data_SUBMISSIONS[0].Course_name,Assignment_id=data_SUBMISSIONS[0].Assignment_id)
        if m1.is_valid() and (int)(a.Marks1)==0 : 
            a.Marks1=m1.cleaned_data.get("Marks1")
            a.Total=str(round(( ((int)(m1.cleaned_data.get("Marks1")) + (int)(a.Marks2) + (int)(a.Marks3)) / 3 ),2))
            a.save(update_fields=["Marks1","Total"])  
            a.save()
    if request.method == 'POST':  
        m2 = marks2(request.POST)  
        a=Marks.objects.get(Person2_name=Student_id,Course_name=data_SUBMISSIONS[0].Course_name,Assignment_id=data_SUBMISSIONS[0].Assignment_id)
        if m2.is_valid() and (int)(a.Marks2) == 0:  
            a.Marks2=m2.cleaned_data.get("Marks2")
            a.Total=str( round(( ((int)(m2.cleaned_data.get("Marks2")) + (int)(a.Marks1) + (int)(a.Marks3)) / 3 ),2))
            a.save(update_fields=["Marks2","Total"])
            a.save()
    if request.method == 'POST':  
        m3 = marks3(request.POST)  
        a=Marks.objects.get(Person3_name=Student_id,Course_name=data_SUBMISSIONS[0].Course_name,Assignment_id=data_SUBMISSIONS[0].Assignment_id)
        if m3.is_valid() and (int)(a.Marks3) == 0:  
            a.Marks3=m3.cleaned_data.get("Marks3")
            a.Total=str( round((((int)(m3.cleaned_data.get("Marks3")) + (int)(a.Marks1) + (int)(a.Marks2)) / 3), 2) )
            a.save(update_fields=["Marks3","Total"])
            a.save()
    m1=marks1()
    m2=marks2()
    m3=marks3()
    a1=Marks.objects.get(Person1_name=Student_id,Course_name=main.Course_name,Assignment_id=main.Assignment_id)
    a2=Marks.objects.get(Person2_name=Student_id,Course_name=main.Course_name,Assignment_id=main.Assignment_id)
    a3=Marks.objects.get(Person3_name=Student_id,Course_name=main.Course_name,Assignment_id=main.Assignment_id)

    return render(request,'Intern_app/Student_Ass_Correction.html',{
        "m1":m1,"m2":m2,"m3":m3,"a":a1,"b":a2,"c":a3
    })

def TEACHER_ASS_MARKS_CHECK(request):
    data=Marks.objects.filter(Course_name=data_SUBMISSIONS[0].Course_name,Assignment_id=data_SUBMISSIONS[0].Assignment_id)
    return render(request,'Intern_app/Teacher_2_Ass_Marks.html',{
        "data":data
    })


    