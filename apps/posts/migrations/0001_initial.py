# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'posts_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('date_and_time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
        ))
        db.send_create_signal(u'posts', ['Post'])

        # Adding model 'Blog'
        db.create_table(u'posts_blog', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['posts.Post'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('text', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'posts', ['Blog'])

        # Adding model 'Picture'
        db.create_table(u'posts_picture', (
            (u'post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['posts.Post'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('picture', self.gf('django.db.models.FileField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'posts', ['Picture'])

        # Adding model 'CommentToBlog'
        db.create_table(u'posts_commenttoblog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(related_name='blog', to=orm['posts.Blog'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['posts.Post'], null=True)),
            ('node_history', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, blank=True)),
        ))
        db.send_create_signal(u'posts', ['CommentToBlog'])

        # Adding model 'CommentToPicture'
        db.create_table(u'posts_commenttopicture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comment', to=orm['posts.Picture'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('date_and_time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['posts.Post'], null=True)),
            ('node_history', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, blank=True)),
        ))
        db.send_create_signal(u'posts', ['CommentToPicture'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'posts_post')

        # Deleting model 'Blog'
        db.delete_table(u'posts_blog')

        # Deleting model 'Picture'
        db.delete_table(u'posts_picture')

        # Deleting model 'CommentToBlog'
        db.delete_table(u'posts_commenttoblog')

        # Deleting model 'CommentToPicture'
        db.delete_table(u'posts_commenttopicture')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'posts.blog': {
            'Meta': {'object_name': 'Blog', '_ormbases': [u'posts.Post']},
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['posts.Post']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'posts.commenttoblog': {
            'Meta': {'object_name': 'CommentToBlog'},
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blog'", 'to': u"orm['posts.Blog']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node_history': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['posts.Post']", 'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'posts.commenttopicture': {
            'Meta': {'object_name': 'CommentToPicture'},
            'date_and_time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node_history': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['posts.Post']", 'null': 'True'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comment'", 'to': u"orm['posts.Picture']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'posts.picture': {
            'Meta': {'object_name': 'Picture', '_ormbases': [u'posts.Post']},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'picture': ('django.db.models.FileField', [], {'max_length': '100'}),
            u'post_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['posts.Post']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'posts.post': {
            'Meta': {'object_name': 'Post'},
            'date_and_time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['posts']