from django.db import models
from django.contrib.auth.models import AbstractUser
from task.models import Task

MIN_BALANCE = 0
MAX_BALANCE = 100

class UserTask(models.Model): 
  is_done = models.BooleanField(default=False)

  task = models.ForeignKey(to=Task, on_delete=models.CASCADE)

class User(AbstractUser):
  """
  An user class. 
  
  Parent's properties and methods that should only be used:
  username,
  email
  """

  balance = models.IntegerField(default=0)

  tasks = models.ForeignKey(to=UserTask, on_delete=models.CASCADE)

  image = models.URLField()

  USERNAME_FIELD = 'email'

  REQUIRED_FIELDS = [ 'username']

  def increase_balance(self, by):
    self._change_balance(by)

  def decrease_balance(self, by): 
    self._change_balance(-by)

  def _change_balance(self, by): 
    if (MIN_BALANCE <= self.balance + by <= MAX_BALANCE):
      self.balance += by
      self.save()