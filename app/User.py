from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    NOTE: # represents line of code that represents the main logic or intention
    Here AbstractUser is extended such that email id is used for authentication purposes

    # USERNAME_FIELD = "email"
    """