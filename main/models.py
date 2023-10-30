from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import timezone
User = get_user_model()


class Todo(models.Model):
    text = models.TextField(blank=True, null=True)
    expires_at = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


