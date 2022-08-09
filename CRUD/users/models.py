from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None):
        if not email:
            raise ValueError('User must have an email')
        if not phone_number:
            raise ValueError('User must have an email')
        
        user = self.model(
            email = self.normalize_email(email),
            phone_number = phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, phone_number, password):
        user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			phone_number=phone_number
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=20,unique=True)
    phone_number = models.CharField(max_length=15,unique=True)
    password = models.CharField(max_length=10)
    data_join = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm (self, perm , obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


