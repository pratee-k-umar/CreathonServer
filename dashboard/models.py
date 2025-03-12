from django.db import models
from django.contrib.auth.models import User
from core.challenges.models import Challenge

# Create your models here.

class UserProgress(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
  status = models.CharField(
    max_length=20,
    choices=[
      ("started", "Started"),
      ("submitted", "Submitted"),
      ("completed", "Completed"),
    ],
  )
  attempts = models.IntegerField(default=0)
  completed_at = models.DateTimeField(null=True)
