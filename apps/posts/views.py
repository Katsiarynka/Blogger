#coding: utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import logout as _logout
from django.utils.translation import ugettext as _
from Blogger import settings
from Blogger.settings import DATABASES
from apps.comments.forms import WriteReviewToMessageForm
from apps.comments.models import Comment
from apps.comments.views import get_int_if_error_zero, get_wall_of_messages
from apps.partners.models import Partner
from decorators import render_to
from django.core.urlresolvers import reverse

from apps.posts.models import Blog, Picture, Post

def home(request):
    context = {
        'blogs': Blog.objects.select_related().filter(is_public=True).order_by('-date_and_time')[0:10],
        'pictures': Picture.objects.select_related().filter(is_public=True).order_by('-date_and_time')[0:10],
        'partners': Partner.objects.all(),
    }
    return render_to_response('index.html', context,
                          context_instance=RequestContext(request))

def pictures(request):
    context = {
        'posts': Picture.objects.filter(is_public=True).order_by('-date_and_time'),
        'title': 'Pictures'
    }
    return render_to_response('posts.html', context,
                          context_instance=RequestContext(request))

def picture(request, post_id):
    context = {
        'post': Picture.objects.select_related().get(post_ptr_id=post_id),
        'title': 'Picture'
    }

    child_ids = tree_ids = heirs_of_tree = set()
    if request.method == 'GET':
        if request.GET.has_key("childs"):
            child_ids = child_ids.union(get_int_if_error_zero(i) for i in request.GET.getlist('childs'))
        if request.GET.has_key("trees"):
            tree_ids = tree_ids.union([get_int_if_error_zero(i) for i in request.GET.getlist('trees')])
            msgs = Comment.objects.filter(id__in=tree_ids)
            for msg in msgs:
                heirs_of_tree |= set(Comment.objects.filter(pos__idt=post_id,node_history__startswith=msg.node_history).values_list('id', flat=True))
    context['messages'] = get_wall_of_messages(0, Comment.objects.filter(parent=None).order_by('-date_and_time'),
                                               child_ids, tree_ids)
    form = WriteReviewToMessageForm()
    context['form'] = form
    context['trees'] = list(heirs_of_tree)
    context['childs'] = list(child_ids)
    return render_to_response('post.html', context,
                          context_instance=RequestContext(request))

def new_pic(request):
    context = {
        'title': 'New picture'
    }
    return render_to_response('new_post.html', context,
                          context_instance=RequestContext(request))

def new_blog(request):
    context = {
        'title': 'New blog'
    }
    return render_to_response('new_post.html', context,
                          context_instance=RequestContext(request))


def blogs(request):
    context = {
        'posts': Blog.objects.select_related().filter(is_public=True).order_by('-date_and_time')[0:100],
        'title': 'Blogs'
    }
    return render_to_response('posts.html', context,
                          context_instance=RequestContext(request))




def blog(request, post_id):
    context = {
        'post': Blog.objects.get(post_ptr_id=post_id)
    }

    child_ids = tree_ids = heirs_of_tree = set()
    if request.method == 'GET':
        if request.GET.has_key("childs"):
            child_ids = child_ids.union(get_int_if_error_zero(i) for i in request.GET.getlist('childs'))
        if request.GET.has_key("trees"):
            tree_ids = tree_ids.union([get_int_if_error_zero(i) for i in request.GET.getlist('trees')])
            msgs = Comment.objects.filter(id__in=tree_ids)
            for msg in msgs:
                heirs_of_tree |= set(Comment.objects.filter(pos__idt=post_id,node_history__startswith=msg.node_history).values_list('id', flat=True))
    context['messages'] = get_wall_of_messages(0, Comment.objects.filter(parent=None).order_by('-date_and_time'),
                                               child_ids, tree_ids)
    form = WriteReviewToMessageForm()
    context['form'] = form
    context['trees'] = list(heirs_of_tree)
    context['childs'] = list(child_ids)
    context['title'] = 'Blog'
    return render_to_response('post.html', context,
                          context_instance=RequestContext(request))


def user_blogs(request, user_id):
    context = {
        'posts': Blog.objects.filter(is_public=True, user__id=user_id).order_by('-date_and_time'),
        'title': 'User blogs'
    }
    return render_to_response('posts.html', context,
                          context_instance=RequestContext(request))


def user_pictures(request, user_id):
    context = {
        'posts': Picture.objects.filter(is_public=True, user__id=user_id).order_by('-date_and_time'),
        'title': 'User pictures'
    }
    return render_to_response('posts.html', context,
                          context_instance=RequestContext(request))

def get_slide_images(request):
    context = {
        "slides": [settings.MEDIA_URL+i.photo.name for i in Picture.objects.order_by('count_of_likes')[0:10]],
    }
    return render_to_response('slider_view.html',
                          context,
                          context_instance=RequestContext(request))
