from django.db import models

# Create your models here.

class Student(models.Model):
      name=models.CharField(max_length=100)
      email=models.CharField(unique=True)
      age=models.IntegerField()
      city=models.CharField(max_length=100)
    # enrollment_data=models.DateField(auto_now_add=True)

# Student.objects.create(
#     name="Bharat",
#     age=21,
#     email="bharat@gmail.com"
# )

# student =Student.objects.all()

      def __str__(self):
        return self.name