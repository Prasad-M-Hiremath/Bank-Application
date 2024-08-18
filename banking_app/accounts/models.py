from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    failed_attempts = models.PositiveIntegerField(default=0)
    last_failed_attempt = models.DateTimeField(null=True, blank=True)
