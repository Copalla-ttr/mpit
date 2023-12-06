from django.db import models
from shared.models import ( TaskTags, Tag )

class TaskTag(Tag):
  tags = TaskTags

class Task(models.Model):
  name = models.CharField(max_length=255, unique=True, primary_key=True)

  title = models.CharField(max_length=255)

  text = models.TextField(max_length=4095)

  cost = models.IntegerField()
  
  tags = models.ForeignKey(to=TaskTag, on_delete=models.CASCADE)