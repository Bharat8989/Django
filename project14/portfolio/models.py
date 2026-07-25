from django.db import models

# Create your models here.
class StudentPortfolio(models.Model):
    name=models.CharField(max_length=100)
    # email=models.email_field()
    age=models.IntegerField()
    city=models.CharField()
    # phone=models.CharField()
    
    def __str__(self):
        return self.name
    