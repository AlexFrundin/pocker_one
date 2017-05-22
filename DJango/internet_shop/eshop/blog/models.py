from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, verbose_name='Автор')
    name = models.CharField("Название", max_length=200)
    date = models.DateField("Дата", auto_now_add=True)
    text = models.TextField("Пост")
    slug = models.SlugField(unique_for_date = 'date', max_length=1000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('post_details',
        kwargs={
        'slug':self.slug,
        'date':self.date
        })
