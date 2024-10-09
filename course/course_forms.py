from django import forms
from .models import Course

class CourseForm(forms.modelsForm):
    class Meta:
        model = Course
        fields = ['course_ID','Course']