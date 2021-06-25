from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=80)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'


    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'