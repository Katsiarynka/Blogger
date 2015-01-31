from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField

from django.contrib.auth.models import User

from django.contrib import admin

class Note(models.Model):
    user = models.ForeignKey(User, null=False, verbose_name=_('Users'))
    date_and_time = models.DateTimeField(verbose_name=_(u"Date and time"), db_index=True)
    title = models.CharField(verbose_name=_('Title'), max_length=255)

    def __unicode__(self):
        return '%s %s'%(self.user, self.date_and_time)

    @classmethod
    def get_type(cls):
        return "note"

    class Meta:
        verbose_name = _(u"Note")
        verbose_name_plural = _(u"Notes")


admin.site.register(Note)