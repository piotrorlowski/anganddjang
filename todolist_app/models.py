from django.db import models

# Create your models here.


class ToDoList(models.Model):
  title = models.CharField(max_length=250)

  def __unicode__(self):
    return self.title


class ToDoListElement(models.Model):
  title = models.CharField(max_length=250)
  to_do_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)