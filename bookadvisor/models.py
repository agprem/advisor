
from django.db import models
from django import forms
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

# Create your models here.



#from django.db.models import Model

# Create your models here.
class UserTestManager(BaseUserManager):
    def create_user(self,email,password=None):
        print("Hello",email)
        if not email:
            raise ValueError("User must have Email")
        print("normal user created")
        email=self.normalize_email(email)
        user=self.model(email=email)
        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self,email,password=None):
        #user = self.create_user(email=self.normalize_email(email))
        print("superuser created")
        print(email)
        user = self.create_user(email=email,password=password,)
        user.set_password(password)
        user.is_admin= True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserTest(AbstractBaseUser):
    id=models.AutoField(verbose_name='UID',
                                  serialize=False,
                                  auto_created=True,
                                 primary_key=True )
    name= models.CharField(max_length=20)
    email= models.EmailField('Email Address',unique=True)
    password= models.CharField(max_length=20,null=True)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []
    objects=UserTestManager()

    def __str__(self):
        return self.name

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

    def is_superuser(self):
       return self.is_admin





class AdvisorManager(BaseUserManager):
    def create_user(self,first_name,password=None):
        print("Hello",first_name)
        if not first_name:
            raise ValueError("Advisor must have Name")
        print("normal user created")
        user=self.model(first_name=first_name,)
        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,password,email=None):
        #user = self.create_user(email=self.normalize_email(email))
        print("superuser created")
        print(first_name)
        user = self.create_user(first_name=first_name,password=password,)
        user.set_password(password)
        user.is_admin= True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user




class Advisor(AbstractBaseUser):
    id = models.IntegerField(verbose_name='Advisor-ID',
                                  serialize=False,
                                  auto_created=True,primary_key=True
                                  )
    first_name = models.CharField(verbose_name='AdvName',max_length=20,unique=True,blank=True)
    profilepic = models.ImageField('Add Profilepic',null=False,blank=False,upload_to='images/')
    bid = models.IntegerField(blank=True,null=True)
    bookingtime = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True,null=True)
    is_staff = models.BooleanField(default=False),
    is_active=models.BooleanField(default=False),
    is_admin=models.BooleanField(default=False),
    is_superuser=models.BooleanField(default=False),
    is_admin=models.BooleanField(default=False)
    USERNAME_FIELD = 'first_name'
    REQUIRED_FIELD = []
    objects=AdvisorManager()

    def __str__(self):
        return self.first_name

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

    def is_superuser(self):
       return self.is_admin
