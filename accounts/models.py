# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from .manager import CustomManger

# class CustomUser(AbstractUser):
#     phone_number = models.CharField(unique=True, max_length=50)
#     age = models.IntegerField()
#     gender = models.CharField(choices=(
#         ('Male', 'Male'),
#         ('female', 'female')
#     ), max_length=100)
#     profile_picture = models.ImageField(upload_to="profile/images/")

#     USERNAME_FIELD ="phone_number"
#     REQUIRED_FIELDS = []

#     objects = CustomManger()

    