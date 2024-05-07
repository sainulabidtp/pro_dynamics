from django import forms
from .models import Student
from .models import Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name']
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'subject', 'grade']

