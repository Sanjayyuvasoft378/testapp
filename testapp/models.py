from django.db import models

# Create your models here.



class UserRegistration(models.Model):
    username = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)
    confirmPassword = models.CharField(max_length=20)

    def __str__(self):
        return self.email



