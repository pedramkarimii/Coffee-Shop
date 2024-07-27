from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

"""
  +-------------+     1    +---------------------+
  |    User     |◄ ─ ─ ─ ─ ┤     Profile         |
  +-------------+          +---------------------+
  | id          |◄─────────┤ user_id (PK, FK)    |
  | username    |          | phone_number        |
  | password    |          | full_name           |
  | email       |          | create_time         |
  | ...         |          | update_time         |
  +-------------+          +---------------------+

"""


class Profile(models.Model):
    """
    Model representing additional information associated with a user.

    user: One-to-one relationship with the User model.
    If a User object is deleted, the associated Profile object will also be deleted.
    'related_name' attribute allows accessing Profile objects from a User instance using 'user.profile'.

    phone number: Field to store the user's phone number.
    'unique=True' ensures each phone number is not unique.

    full name: Field to store the user's full name

    create time: Field to store the creation time of the profile.
    'auto_now_add=True' automatically sets the field to the current datetime when the object is first created.
    'editable=False' prevents this field from being edited.

   update time: Field to store the last update time of the profile.
   'auto_now=True' automatically updates the field to the current datetime whenever the object is saved.
   'editable=False' prevents this field from being edited.
   """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=11)
    full_name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True, editable=False)
    update_time = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ["-update_time"]
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Method to return a string representation of the Profile object."""
        return f"ID: {self.id} full name: {self.full_name}"

    def get_absolute_url(self):
        """Method to return the absolute URL of the profile instance."""
        return reverse("profile_detail", args=[self.id])

    @property
    def capitalize(self):
        """Property method that returns the full name of the user with each word capitalized."""
        return self.full_name.title()
