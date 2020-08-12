import hashlib

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from users.managers import UserManager


USER_TYPE = [
    ('1', 'USER'),
    ('2', 'ADMIN')
]


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), unique=True, blank=True,)
    first_name = models.CharField(_('name'), max_length=30, blank=True)
    last_name = models.CharField(_('surname'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('registered'), auto_now_add=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_active = models.BooleanField(_('is_active'), default=False)
    user_type = models.CharField(_('user_type'), choices=USER_TYPE, default=1, max_length=50)
    uuid = models.CharField(max_length=500, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.uuid:
            h = hashlib.md5(bytes(self.email, encoding='utf8'))
            self.uuid = h.hexdigest()
            self.save()
            self.email_user('Hello', f'Activate: http://localhost:8080//activate_email/{self.id}/{self.uuid}')

    def __str__(self):
        return f'{self.email} ID {self.id}'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def send(self):
        send_mail('Subject here', 'Here is the message.', 'from@example.com',
                  [self.email], fail_silently=False)
