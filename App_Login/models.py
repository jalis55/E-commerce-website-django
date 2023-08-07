from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils.translation import ugettext_lazy


# Create your models here.
class CustomUserManager(BaseUserManager):
    
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Email must be set")
        
        email=self.normalize_email(email)

        user=self.model(email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Must a staff")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Must be super user")
        return self._create_user(email,password,**extra_fields)
class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True,null=False)
    is_staff=models.BooleanField(ugettext_lazy('staff status'),default=False,help_text=("user can login can login this site"))
    is_active=models.BooleanField(ugettext_lazy('active'),default=True,help_text=ugettext_lazy("user should active.Unselect to make inactive"))

    USERNAME_FIELD=email
    objects=CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    username=models.CharField(max_length=50,blank=True)
    full_name=models.CharField(max_length=256,blank=True)
    address_1=models.TextField(max_length=300,blank=True)
    city=models.CharField(max_length=40,blank=True)
    zip_code=models.CharField(max_length=50,blank=True)
    country=models.CharField(max_length=40,blank=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    

