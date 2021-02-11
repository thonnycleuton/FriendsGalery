from django.contrib.auth.models import User
from django.db import models


class Profile(User):
    """
    This class is responsible for modeling the module that control the access to the system.
    It also extends the User Class and provides some additional fields to our users.
    """
    # allows to check either user can upload pictures or not
    allowed_to_upload = models.BooleanField()

    def __str__(self):
        return self.first_name
