from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, null=False, verbose_name=_('User'))
    first_name = models.CharField(max_length=255, verbose_name=_('First name'))
    second_name = models.CharField(max_length=255, verbose_name=_('Second name'))
    last_name = models.CharField(max_length=255, verbose_name=_('Last name'))
    date_of_birthday = models.DateField(null=False, verbose_name=_('Date of birthday'))

class Follower(models.Model):
    user = models.ForeignKey(User, null=False, verbose_name=_('User'), related_name='follower')
    user_followed = models.ForeignKey(User, null=False, verbose_name=_('User'), related_name='user_follower')
    date_of_follow = models.DateField(verbose_name=_('Date of follow'))


from django.contrib import admin
admin.site.register(Profile)