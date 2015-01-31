from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from apps.posts.models import Post

from django.contrib import admin


class Like(models.Model):
    post = models.ForeignKey(Post, null=False, verbose_name=_('Post'))
    user = models.ManyToManyField(User, verbose_name=_('User'), null=False)

    def save(self, *args, **kwargs):
        self.post.count_of_likes += 1
        self.post.save()
        return super(Like, self).save(args, kwargs)

    def delete(self, *args, **kwargs):
        self.post.count_of_likes -= 1
        self.post.save()
        return super(Like, self).delete(args, kwargs)


class Dislike(models.Model):
    post = models.ForeignKey(Post, null=False, verbose_name=_('Post'))
    user = models.ManyToManyField(User, verbose_name =_('User'), null=False)

    def save(self, *args, **kwargs):
        self.post.count_of_dislikes += 1
        self.post.save()
        return super(Dislike, self).save(args, kwargs)

    def delete(self, *args, **kwargs):
        self.post.count_of_dislikes -= 1
        self.post.save()
        return super(Dislike, self).delete(args, kwargs)


admin.site.register(Like)
admin.site.register(Dislike)