from django.db import models

class Tag(models.Model):
  tags = ()
  tag = models.CharField(choices=tags, unique=True, primary_key=True, max_length=32)

  def getTag(self):
    return self.tag


TEST1 = 'TEST1'
TEST2 = 'TEST2'
TEST3 = 'TEST3'
TEST4 = 'TEST4'
TEST5 = 'TEST5'
TEST6 = 'TEST6'

TestTags = (
  (TEST1, 'Test1'),
  (TEST2, 'Test2'),
  (TEST3, 'Test3'),
  (TEST4, 'Test4'),
  (TEST5, 'Test5'),
  (TEST6, 'Test6'),
)

TaskTags = TestTags