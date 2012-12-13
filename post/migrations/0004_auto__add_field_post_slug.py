# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.slug'
        db.add_column('post_post', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='abc', unique=True, max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.slug'
        db.delete_column('post_post', 'slug')


    models = {
        'post.post': {
            'Meta': {'object_name': 'Post'},
            'edit_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'markdown': ('django.db.models.fields.TextField', [], {}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'abc'", 'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['post']