# -*- coding=utf-8 -*-
from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def is_active_url(context, url_name, user_id=''):
    request = context['request']
    if (url_name.find('home')+1):
        return "active" if request.path is '/' else ""
    else:
        url = reverse(url_name, kwargs=({'user_id':user_id } if (user_id) else {}))
        return "active" if request.path.find(url) + 1 else ""
