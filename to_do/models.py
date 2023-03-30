from django.contrib.auth.models import User
from django.db import models


class ToDoListTitle(models.Model):
    title = models.CharField('Name of the to-do list', max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')

    class Meta:
        verbose_name = 'To do list title'
        verbose_name_plural = 'To do list headers'

    def __str__(self):
        return self.title


class Record(models.Model):
    record_title = models.CharField('Record title', max_length=45)
    status = models.BooleanField('Status', default=False)
    title = models.ForeignKey(ToDoListTitle, models.CASCADE, verbose_name='Title')

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'

    def __str__(self):
        return self.record_title
