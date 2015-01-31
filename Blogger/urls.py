#unicode: utf-8

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'apps.posts.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^djangocontrib/jsi18n', 'django.views.i18n.javascript_catalog', name='djangocontrib_jsi18n'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
)

urlpatterns += patterns('apps.posts.views',
    url(r'^pictures/$', 'pictures', name='pictures'),
    url(r'^blogs/$', 'blogs', name='blogs'),
    url(r'^blogs/new$', 'new_blog', name='new_blog'),
    url(r'^pictures/new$', 'new_pic', name='new_pic'),
    url(r'^user(?P<user_id>\d+)/blogs/$', 'user_blogs', name='user_blogs'),
    url(r'^user(?P<user_id>\d+)/pictures/$', 'user_pictures', name='user_pictures'),
    url(r'^blogs/(?P<post_id>\d+)/$', 'blog', name='blog'),
    url(r'^pictures/(?P<post_id>\d+)/$', 'picture', name='picture'),
    url(r'^get_slide_images/$', 'get_slide_images', name='get_slide_images'),
)


urlpatterns += patterns('apps.profiles.views',
    url(r'^user(?P<user_id>\d+)/$', 'user_profile', name='user_profile'),
    url(r'^peoples/$', 'peoples', name='peoples'),
)

urlpatterns += patterns('apps.notes.views',
    url(r'^user(?P<user_id>\d+)/notes/$', 'user_notes', name='user_notes'),
)

urlpatterns += patterns('apps.comments.views',
    url(r'^write_message/(?P<post_id>\d+)$', 'write_message', name='write_message'),
    url(r'^write_review/(?P<post_id>\d+)$', 'write_review', name='write_review'),
    url(r'^show_childs_or_tree/$', 'show_childs_or_tree', name='show_childs_or_tree'),
)