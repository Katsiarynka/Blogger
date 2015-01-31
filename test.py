import random

from random import randrange
from datetime import timedelta
import datetime
import time


from copy import deepcopy



EN_ALPHABET = u'abcdefghijklmnopqrstuvwxyz1234567890'


def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)

    return time.strftime("%Y-%m-%d %I:%M:%S", time.localtime(ptime))



import os
import sys


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Blogger.settings")
    from django.contrib.auth.models import User
    from apps.notes.models import Note
    for user in User.objects.all():
        for i in xrange(int(random.random()*3)):
            title = u''.join(EN_ALPHABET[int(random.random()*EN_ALPHABET.__len__())] for i in xrange(int(random.random()*10)+10))
            date =  strTimeProp("1/1/2013", "1/1/2015",'%m/%d/%Y',  random.random())
            print title
            print(date)
            note = Note(user=user,
                        title=title,
                        date_and_time = date)
            note.save()

def generate_posts():
    from django.contrib.auth.models import User
    from apps.posts.models import Blog, Picture
    blog = Blog.objects.select_related().get(post_ptr_id=2)

    pic = Picture.objects.select_related().get(post_ptr_id=1)
    post_pic = pic.post
    for user in User.objects.all():
        for i in xrange(int(random.random()*3)+1):
            copy_of_blog = blog.copy(Blog())
            copy_of_blog.user = user
            copy_of_blog.save()

        for i in xrange(int(random.random()*3)+1):
            copy_of_pic = pic.copy(Picture())
            copy_of_pic.user = user
            copy_of_pic.save()


def generate_users():
    from django.contrib.auth.models import User
    for i in xrange(1000):
        username = ''.join(EN_ALPHABET[int(random.random()*EN_ALPHABET.__len__())] for i in xrange(int(random.random()*10)+10))
        first_name = ''.join(EN_ALPHABET[int(random.random()*EN_ALPHABET.__len__())] for i in xrange(int(random.random()*10)+1))
        last_name = ''.join(EN_ALPHABET[int(random.random()*EN_ALPHABET.__len__())] for i in xrange(int(random.random()*10)+1))
        email = ''.join(EN_ALPHABET[int(random.random()*EN_ALPHABET.__len__())] for i in xrange(int(random.random()*10)+1))+'@mail.ru'
        is_staff = False
        is_active = True
        password = ''.join(EN_ALPHABET[int(random.random()*EN_ALPHABET.__len__())] for i in xrange(int(random.random()*10)+1))
        date_joined = strTimeProp("1/1/2014", "1/1/2015",'%m/%d/%Y',  random.random())
        date_of_birthday = strTimeProp("1/1/1980", "1/1/2015",'%m/%d/%Y',  random.random())
        user = User(username=username, first_name=first_name, last_name=last_name, email=email, is_staff=is_staff, is_active=is_active, password=password,
                    date_joined=date_joined)
        try:
            user.save()
        except Exception as e:
            print e
        else:
            print(user)
