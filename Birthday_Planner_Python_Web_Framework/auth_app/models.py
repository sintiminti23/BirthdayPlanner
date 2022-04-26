from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models

from Birthday_Planner_Python_Web_Framework.auth_app.manager import BirthdayPlannerManager


class BirthdayPlannerUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        max_length=60,
        unique=True,
        blank=False,
        error_messages={
            'unique': f"This Birthday Planner email address already exists.",
        },

    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_superuser = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    date_changed = models.DateTimeField(
        auto_now=True,
    )

    last_login = models.DateTimeField(
        auto_now=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = BirthdayPlannerManager()

    class Meta:
        unique_together = ("email",)
        db_table = "User"
