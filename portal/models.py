from django.db import models

# Create your models here.
class Students(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=30)
    dob = models.DateField()
    marks = models.FloatField()
    email = models.EmailField()
    # Store phone numbers as text (avoid integer overflow and preserve formatting)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"{self.roll_no} - {self.name}"