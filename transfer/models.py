from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    ACADEMICYEAR_CHOICES = [
        (1,'First Year'),
        (2,'Second Year'),
        (3,'Third Year'),
        (4,'Fourth Year'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    full_name = models.CharField(max_length=200)
    University_id = models.CharField(max_length=10)
    academic_year = models.IntegerField(choices=ACADEMICYEAR_CHOICES)
    phone = models.CharField(max_length=11)
    telegram_user = models.CharField(max_length=25)


class TransferRequest(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    current_section = models.IntegerField()
    target_section = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

