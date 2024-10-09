from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView,CreateView
from .models import Course
from .course_forms import CourseForm

# view all the courses
class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'

# single course view
class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_form.html'
    success_url = '/courses/'
