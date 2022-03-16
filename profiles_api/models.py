from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
  """Manager for user profiles""" 

  def create_user(self, email, name, company, password=None):
    "Creates a new user profile"
    if not email:
      raise ValueError("User must have an email address");

    email = self.normalize_email(email)
    user = self.model(email=email, name=name, company=company)

    user.set_password(password)
    user.save(using=self._db)

    return user

  def create_superuser(self, email, name, password, company):
    """Create a new supseruser with given details"""
    user = self.create_user(email, name, password, company)
    
    user.is_superuser = True
    user.is_staff = True
    user.save(using=self._db)
    

    return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
  """Database model for users in the system"""
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  company = models.CharField(max_length=200)

  objects = UserProfileManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  def get_full_name(self):
    """Retrieve full name of user"""
    return self.name

  def get_short_name(self):
    """Retrieve short name of user"""
    return self.name

  def __str__(self):
    """Return string representation of our user"""
    return self.email