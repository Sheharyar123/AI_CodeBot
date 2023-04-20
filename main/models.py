from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="records")
    question = models.TextField(max_length=5000)
    response = models.TextField(max_length=5000)
    language = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
