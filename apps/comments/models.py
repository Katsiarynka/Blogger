from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

import datetime

from apps.posts.models import Post


class Comment(models.Model):
    user = models.ForeignKey(User, null=False, verbose_name=_('Users'))
    date_and_time = models.DateTimeField(verbose_name=_(u"Date and time"), db_index=True)
    count_of_likes = models.IntegerField(verbose_name=_('Count of likes'), default=0)
    count_of_dislikes = models.IntegerField(verbose_name=_('Count of dislikes'), default=0)
    is_public = models.BooleanField(verbose_name=_("This post is enabled to all?"))
    is_banned_by_admin = models.BooleanField(verbose_name=_("This post is banned by admin"))
    text = models.TextField(verbose_name=_(u"Text"))
    parent = models.ForeignKey('self', null=True)
    node_history = models.CharField(max_length=255, db_index=True, blank=True)
    post = models.ForeignKey(Post, verbose_name=_('Post'), null=False, related_name='post')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.date_and_time = datetime.datetime.now()
        parent = self.parent
        self.node_history = ("" if (parent==None) else parent.node_history)+len(Comment.objects.filter(parent=parent))+"-"
        return super(Comment, self).save()

    def in__dict(self, args):
        dict = {
            'id': self.id,
            'text': self.text,
            'date_and_time': str(self.date_and_time),}
        dict.update(args)
        return dict

    @classmethod
    def get_root_comments(cls, post_id):
        return Comment.objects.filter(parent=None, post=post_id)

admin.site.register(Comment)