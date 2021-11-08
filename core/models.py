from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    course = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        

