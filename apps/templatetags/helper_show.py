from django import template
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from apps.posts.models import Blog
from apps.notes.models import Note


register = template.Library()


@register.inclusion_tag('latest_posts.html')
def show(name, count, user_id=''):
    url = reverse(name, kwargs=({'user_id' : user_id } if (user_id) else {}))
    objs = []
    url_item = 'blog'
    if name == 'blogs':
        title = _(u"Latest blogs")
        model = Blog
        objs = model.objects.filter(is_public=True).order_by('-date_and_time')[:count]
    elif name == 'user_blogs' and user_id:
        title = _(u"My blogs")
        model = Blog
        objs = model.objects.filter(user__id=user_id).order_by('-date_and_time')[:count]
    elif name == 'user_notes' and user_id:
        title = _(u"Your notes")
        model = Note
        url_item = ''
        objs = model.objects.filter(user__id=user_id).order_by('-date_and_time')[:count]
    return {'objs': objs, 'title': title, 'url': url, 'url_item': url_item,
            'type': name}
