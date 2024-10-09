from django.db import models

class Course(models.Model):
    course_ID = models.CharField(max_length=50)
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.course
