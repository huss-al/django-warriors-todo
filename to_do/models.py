from django.db import models
from django.contrib.auth.models import User


STATUS = ((1, "todo"), (2, "InProgress"), (3, "Done"))


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, null=False)
    description = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="todo_posts"
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)

    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"