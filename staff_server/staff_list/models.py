from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Organization(models.Model):
    type = models.CharField(max_length=32, verbose_name='Организация')

    def __str__(self):
        return self.type


class Substation(models.Model):
    subtype = models.CharField(max_length=32, blank=True)
    name = models.CharField(max_length=32, verbose_name='Объект')
    email = models.EmailField(blank=True, verbose_name='email')
    organization = models.ForeignKey(Organization,
                                     on_delete=models.PROTECT,
                                     null=True, blank=True,
                                     verbose_name='Организация',
                                     related_name='organization')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class Staff(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Полное имя')
    job_title = models.CharField(max_length=32, blank=True, verbose_name='Должность')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Создан')
    job = models.ForeignKey(Substation,
                            on_delete=models.PROTECT,
                            related_name='substation',
                            verbose_name='Объект')

    def __str__(self):
        return self.full_name
