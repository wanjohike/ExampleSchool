from django.urls import path
from .views import StudentCreateView,StudentDetailView, StudentListView

urlpatterns = [
    path('Student/', StudentListView.as_view(), name = 'student-list'),
    path('Student/<int:pk>/', StudentDetailView.as_view(), name = 'student-detail'),
    path('Student/new/', StudentCreateView.as_view(), name = 'student-create'),

]