from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView,CreateView
from .models import Student
from .forms import StudentForm

# view for all the students
class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

# detail view for a single student
class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = '/students/'
