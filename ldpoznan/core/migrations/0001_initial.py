# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Registration'
        db.create_table(u'core_registration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('mail', self.gf('django.db.models.fields.EmailField')(max_length=200, blank=True)),
            ('info', self.gf('django.db.models.fields.TextField')(max_length=4000, blank=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Registration'])


    def backwards(self, orm):
        # Deleting model 'Registration'
        db.delete_table(u'core_registration')


    models = {
        u'core.registration': {
            'Meta': {'object_name': 'Registration'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'max_length': '4000', 'blank': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']