from django.db import models
# Create your models here.

class Login_Teacher(models.Model):
    Teacher_name=models.CharField(max_length=30)
    Teacher_pass=models.CharField(max_length=30)   
    def __str__(self):
        return f"{self.Teacher_name} / {self.Teacher_pass}"

class Login_Student(models.Model):
    Student_name=models.CharField(max_length=30)
    Student_pass=models.CharField(max_length=30)   
    def __str__(self):
        return f"{self.Student_name} / {self.Student_pass}"

class Teacher_Course(models.Model):
    Teacher_name=models.CharField(max_length=30)
    Course_name=models.CharField(max_length=30)   
    def __str__(self):
        return f"{self.Teacher_name} / {self.Course_name}"

class Student_Course(models.Model):
    Student_name=models.CharField(max_length=30)
    Course_name=models.CharField(max_length=30)   
    def __str__(self):
        return f"{self.Student_name} / {self.Course_name}"

class Course_Details(models.Model):
    Course_name=models.CharField(max_length=30)
    Assignments=models.CharField(max_length=30)
    Reading_Materials=models.CharField(max_length=30)   
    def __str__(self):
        return f"{self.Course_name} / {self.Assignments} / {self.Reading_Materials}"

class Assignment_Details(models.Model):
    Course_name=models.CharField(max_length=30,blank=True)
    Assignment_id=models.CharField(max_length=30,blank=True)
    Assignment_instructions=models.CharField(max_length=30,blank=True)
    Assignment_content = models.FileField(upload_to='static/Assignment_content')
    def __str__(self):
        return f"{self.Course_name} / {self.Assignment_id} / {self.Assignment_content}"

class ReadingMaterial_Details(models.Model):
    Course_name=models.CharField(max_length=30,blank=True)
    ReadingMaterial_id=models.CharField(max_length=30,blank=True)   
    ReadingMaterial_instructions=models.CharField(max_length=30,blank=True)   
    ReadingMaterial_content = models.FileField(upload_to='static/ReadingMaterial_content')
    def __str__(self):
        return f"{self.Course_name} / {self.ReadingMaterial_id} / {self.ReadingMaterial_content}"

class Students_Ass_Submission(models.Model):
    Student_name=models.CharField(max_length=30)
    Course_name=models.CharField(max_length=30)
    Assignment_id=models.CharField(max_length=30)   
    Submission_content = models.FileField(upload_to='static/Assignment_submissions')
    def __str__(self):
        return f"{self.Student_name} / {self.Course_name} / {self.Assignment_id} / {self.Submission_content}"

class Marks(models.Model):
    Student_name=models.CharField(max_length=30)
    Course_name=models.CharField(max_length=30)
    Assignment_id=models.CharField(max_length=30)  
    Content=models.CharField(max_length=100)
    Person1_name=models.CharField(max_length=30)
    Marks1=models.CharField(max_length=30)
    Person2_name=models.CharField(max_length=30)
    Marks2=models.CharField(max_length=30)
    Person3_name=models.CharField(max_length=30)
    Marks3=models.CharField(max_length=30)
    Total=models.CharField(max_length=30)
    def __str__(self):
        return f"{self.Course_name} / {self.Assignment_id} / {self.Student_name} / {self.Person1_name} / {self.Person2_name} / {self.Person3_name} /"
