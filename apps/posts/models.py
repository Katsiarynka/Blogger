from django.db import models
from django.utils.timezone import override
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from apps.posts.fields import ExtFileField
from django.contrib import admin

import datetime

TYPE_OF_POST = (
                (1, 'Blog'),
                (2, 'Picture')
                )

class Post(models.Model):
    user = models.ForeignKey(User, null=False, verbose_name=_('Users'))
    date_and_time = models.DateTimeField(verbose_name=_(u"Date and time"), db_index=True)
    count_of_likes = models.IntegerField(verbose_name=_('Count of likes'), default=0)
    count_of_dislikes = models.IntegerField(verbose_name=_('Count of dislikes'), default=0)
    is_public = models.BooleanField(verbose_name=_("This post is enabled to all?"))
    is_banned_by_admin = models.BooleanField(verbose_name=_("This post is banned by admin"))
    type = models.IntegerField(verbose_name=_('Type'), choices=TYPE_OF_POST, default=1)

    def copy(self, new_instance):
        new_instance.date_and_time = self.date_and_time
        new_instance.count_of_likes = self.count_of_likes
        new_instance.count_of_dislikes = self.count_of_dislikes
        new_instance.type = self.type
        new_instance.is_public = self.is_public
        new_instance.is_banned_by_admin = self.is_banned_by_admin
        return new_instance

    @property
    def get_type(self):
        return self.get_type_display()

    @property
    def get_url_of_item(self):
        return reverse(str(self.get_type_display()).lower(), kwargs=({'post_id' : self.id})),

    def get_count_of_like(self):
        return self.count_of_likes

    def get_count_of_dislike(self):
        return self.count_of_dislikes

    def get_main_part(self):
        model = eval(self.get_type_display())
        return model.objects.get(post_ptr_id=self.id).get_main_part()


    def in_dict(self, dict={}):
        return dict.update({
            'type': str(self.get_type).lower(),
            'likes': self.count_of_likes,
            'dislikes': self.count_of_dislikes,
            'date': self.date_and_time,
            'user': self.user,
            'is_public': self.is_public,
            'is_banned_by_admin': self.is_banned_by_admin,
            'main_part': self.get_main_part()
        })

    def __unicode__(self):
        return '%s by %s'%(self.get_type, self.user)


    class Meta:
        verbose_name = _(u"Post")
        verbose_name_plural = _(u"Posts")




class Blog(Post):
    title = models.CharField(max_length=255, blank=False, verbose_name=_("Title"))
    text = HTMLField(blank=False, verbose_name=_('Text'))

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.type = 1
        return super(Blog, self).save()

    def __unicode__(self):
        return 'Blog by %s %s'%(self.user, self.title)

    def get_main_part(self):
        return {
            'url_item': reverse('blog', kwargs=({'blog_id':self.id})),
            'main_part': {
                'title': self.title,
                'html_text': self.text
            }
        }

    def copy(self, new_instance):
        new_instance = super(Blog, self).copy(new_instance)
        new_instance.title = self.title
        new_instance.text = self.text
        return new_instance


    class Meta:
        verbose_name = _(u"Blog")
        verbose_name_plural = _(u"Blogs")


class Picture(Post):
    title = models.CharField(max_length=255, blank=False, verbose_name=_("Title"))
    picture = ExtFileField(upload_to='posts/pictures', verbose_name=_("Image"),
                             ext_whitelist=(".png", ".jpg", ".PNG", ".JPG", ".jpeg", ".JPEG"))
    description = models.CharField(max_length=255, blank=True, verbose_name=_("Description"))


    def copy(self, new_instance):
        new_instance = super(Picture, self).copy(new_instance)
        new_instance.title = self.title
        new_instance.picture = self.picture
        new_instance.description = self.description
        return new_instance

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.type = 2
        return super(Picture, self).save()

    def __unicode__(self):
        return 'Picture by %s %s'%(self.user, self.title)

    def get_main_part(self):
        {
            'url_item': reverse('picture', kwargs=({'pic_id':self.id})),
            'main_part':{
                'title' : self.title,
                'picture' : '<img  src="%s"/>'%self.picture.name,
                'description': self.description
            }
        }


    class Meta:
        verbose_name = _(u"Picture")
        verbose_name_plural = _(u"Pictures")

admin.site.register(Blog)
admin.site.register(Picture)