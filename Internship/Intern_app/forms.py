from django import forms
from .models import *
from django.forms import TextInput

class new_asssignment(forms.ModelForm):
    class Meta:
        model=Assignment_Details
        fields=('Course_name','Assignment_id','Assignment_instructions','Assignment_content')

class new_material(forms.ModelForm):
    class Meta:
        model=ReadingMaterial_Details
        fields=('Course_name','ReadingMaterial_id','ReadingMaterial_instructions','ReadingMaterial_content')

class ass_submission(forms.ModelForm):
    class Meta:
        model=Students_Ass_Submission
        fields=('Submission_content',)

class marks1(forms.ModelForm):
    class Meta:
        model=Marks
        fields=('Marks1',)
        widgets = {
            'Marks1': TextInput(attrs={
                'style': 'width: 150px;height:30px;border: none;color: ;background-image: linear-gradient(to right, rgba(255,0,0,0), rgba(255,0,0,1));',
                })
            }

class marks2(forms.ModelForm):
    class Meta:
        model=Marks
        fields=('Marks2',)
        widgets = {
            'Marks2': TextInput(attrs={
                'style': 'width: 150px;height:30px;border: none;color: ;background-image: linear-gradient(to right, rgba(255,0,0,0), rgba(255,0,0,1));',
                })
            }

class marks3(forms.ModelForm):
    class Meta:
        model=Marks
        fields=('Marks3',)
        widgets = {
            'Marks3': TextInput(attrs={
                'style': 'width: 150px;height:30px;border: none;color: ;background-image: linear-gradient(to right, rgba(255,0,0,0), rgba(255,0,0,1));',
                })
            }
