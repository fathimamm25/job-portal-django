from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES = (
        ('employer', 'Employer'),
        ('jobseeker', 'Job Seeker'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)