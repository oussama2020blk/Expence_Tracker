# from django.contrib.auth.base_user import BaseUserManager

# class CustomManger(BaseUserManager):

#     def create_user(self, phone_number, password, **extra_fileds):
#         if phone_number is None:
#             raise ValueError("Phone number is required")
#         user = self.model(
#             phone_number = phone_number,
#             **extra_fileds
#         )
#         user.set_password(password)
#         user.save()
#         return user
    
#     def create_superuser(self, phone_number, password, **extrafileds):
#         extrafileds.detdefault('is_staff', True)
#         extrafileds.detdefault('is_superuser', True)
#         extrafileds.detdefault('is_active', True)

#         if extrafileds.get('is_staff') is not True:
#             raise ValueError("superuser must is_staff shpud be true")
#         if extrafileds.get('is_super_ser') is not True:
#             raise ValueError("superuser must is_superuser shpud be true")
#         if extrafileds.get('is_active') is not True:
#             raise ValueError("superuser must is_active shpud be true")
#         return self.create_user(phone_number, password, **extrafileds)