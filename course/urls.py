from django.urls import path
from .views import CourseCreateView, CourseDetailView, CourseListView

urlpatterns = [
    path('courses/', CourseListView.as_view, name = 'course-view'),
    path('courses/<int:pk>/', CourseDetailView.as_view, name = 'course-detail'),
    path('courses/new/',CourseCreateView.as_view, name = 'course-create')
]