from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group

class UserManager(BaseUserManager):
    def _create_user(self, email, password,is_staff,is_superuser,**extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            is_active = True,
            last_login = now,
            date_joined = now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_user(self,email=None,password=None,**extra_fields):
        return self._create_user(email,password,False,False,**extra_fields)

    def create_superuser(self,email,password,**extra_fields):
        user = self._create_user(email,password,True,True,**extra_fields)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255, null=True,blank=True) 
    is_staff = models.BooleanField(default=False)  
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
    def get_email(self):
        return self.email
    def get_short_name(self):
        return self.name

class user_type(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_accountant = models.BooleanField(default= False)
    is_manager = models.BooleanField(default= False)

    def __str__(self):
        if self.is_accountant ==True:
            return User.get_email(self.user) + " - is_accountant "
        else:
            return User.get_email(self.user) + " - is_manager"
        
