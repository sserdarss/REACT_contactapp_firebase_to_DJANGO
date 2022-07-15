from django.db import models

class Contact(models.Model):
    gender_choices = [("F","Female"),("M", "Male"),("O","Other")]
    username = models.CharField(max_length=20, unique=True)
    phoneNumber = models.CharField(max_length=15)
    gender= models.CharField(max_length=1, choices=gender_choices)


    def __str__(self) :

        return f"{self.username}"

