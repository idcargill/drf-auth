from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  something_different   = models.CharField(max_length=10)

  def __str__(self):
    return self.username








# class MyAccountManager(BaseUserManager):
#   def create_user(self,  username, password=None):
#     # if not email:
#     #   raise ValueError('Must have email address')

#     if not username:
#       raise ValueError('Must have username')

#     user = self.model(
#       # email = self.normalize_email(email),
#       username=username,
#     )

#     user.set_password(password)
#     user.save(using=self._db)
#     return user

  
#   def create_superuser(self, username, password):
#     user = self.create_user(
#       # email = self.normalize_email(email),
#       username=username,
#       password=password,
#     )

#     user.is_admin = True
#     user.is_staff = True
#     user.is_superuser = True
#     user.save(using=self._db)
#     return user



# class Account(AbstractBaseUser):
#   # email           = models.EmailField(verbose_name="email", max_length=60, unique=True)
#   username        = models.CharField(max_length=30, unique=True)
#   date_joined     = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
#   last_login      = models.DateTimeField(verbose_name="last login", auto_now=True)
#   is_admin        = models.BooleanField(default=False)
#   is_active       = models.BooleanField(default=True)
#   is_staff        = models.BooleanField(default=False)
#   is_superuser    = models.BooleanField(default=False)

#   USERNAME_FIELD  = 'username'
#   REQUIRED_FIELDS = []

#   objects = MyAccountManager()

#   def __str__(self):
#     return self.username

#   def has_perm(self, perm, obj=None):
#     return self.is_admin

#   def has_module_perms(self, app_label):
#     return True

