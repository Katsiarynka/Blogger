#coding: utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import logout as _logout
from django.utils.translation import ugettext as _
from decorators import render_to
from django.core.urlresolvers import reverse

from apps.posts.models import Blog, Picture
from apps.notes.models import Note



def user_notes(request, user_id):
    context = {
        'posts': Note.objects.filter(user__id=user_id).order_by('-date_and_time')
    }
    return render_to_response('posts.html', context,
                          context_instance=RequestContext(request))


