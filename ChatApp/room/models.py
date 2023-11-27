from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField

class Room(models.Model):
    name = models.CharField(max_length=255)
    #slug = models.SlugField(unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def delete_msg(self):
        self.delete()

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)


