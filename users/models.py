from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    number = models.PositiveIntegerField(verbose_name='номер')

    def __str__(self):
        return f'{self.name}({self.number})'

    class Meta:
        verbose_name = 'отдел'
        verbose_name_plural = 'отделы'


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=60, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True,
                                       verbose_name='добавлен')
    avatar = models.ImageField(upload_to='images/', default='noavatar.png',
                               verbose_name='фото')
    department = models.ForeignKey(Department, on_delete=models.PROTECT,
                                   null=True, blank=True, verbose_name='отдел')
    position = models.CharField(max_length=100, verbose_name='должность')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'
