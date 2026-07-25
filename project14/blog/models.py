from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    city=models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    
    
    def __str__(self):
        return f'{self.name} , {self.age} year old -from {self.city}'