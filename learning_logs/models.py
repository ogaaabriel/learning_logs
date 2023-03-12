from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Topic(models.Model):
    title = models.CharField(max_length=250)
    public = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name="topics", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["title", "owner"], name="unique title")
        ]
        ordering = ["-date_created"]

    def __str__(self):
        return f"{self.title} - {self.owner}"


class Entry(models.Model):
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, related_name="entries", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "entries"
        ordering = ["-date_created"]

    def __str__(self):
        return self.content
