from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.posts.models import Post

class Tag(models.Model):
    name_of_tag = models.CharField(blank=False, max_length=255, verbose_name=_('Name of tag'))
    post = models.ForeignKey(Post, null=False, verbose_name=_('Post'))


from django.contrib import admin
admin.site.register(Tag)