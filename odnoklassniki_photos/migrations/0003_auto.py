# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field like_users on 'Album'
        m2m_table_name = db.shorten_name(u'odnoklassniki_photos_album_like_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('album', models.ForeignKey(orm[u'odnoklassniki_photos.album'], null=False)),
            ('user', models.ForeignKey(orm[u'odnoklassniki_users.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['album_id', 'user_id'])

        # Adding field 'Album.like_users.through.time_from'
        db.add_column('odnoklassniki_photos_album_like_users', 'time_from',
            self.gf('django.db.models.fields.DateTimeField')(null=True, db_index=True),
            keep_default=False)
        
        # Adding field 'Album.like_users.through.time_to'
        db.add_column('odnoklassniki_photos_album_like_users', 'time_to',
            self.gf('django.db.models.fields.DateTimeField')(null=True, db_index=True),
            keep_default=False)

    def backwards(self, orm):
        # Removing M2M table for field like_users on 'Album'
        db.delete_table(db.shorten_name(u'odnoklassniki_photos_album_like_users'))


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'odnoklassniki_photos.album': {
            'Meta': {'object_name': 'Album'},
            'created': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'fetched': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'last_like_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'like_users': ('m2m_history.fields.ManyToManyHistoryField', [], {'related_name': "'like_albums'", 'symmetrical': 'False', 'to': u"orm['odnoklassniki_users.User']"}),
            'likes_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'owner_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'odnoklassniki_albums_owners'", 'to': u"orm['contenttypes.ContentType']"}),
            'owner_id': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True'}),
            'owner_name': ('django.db.models.fields.TextField', [], {}),
            'photos_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'odnoklassniki_photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos'", 'to': u"orm['odnoklassniki_photos.Album']"}),
            'comments_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'fetched': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'last_like_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'like_users': ('m2m_history.fields.ManyToManyHistoryField', [], {'related_name': "'like_photos'", 'symmetrical': 'False', 'to': u"orm['odnoklassniki_users.User']"}),
            'likes_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'owner_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'odnoklassniki_photos_owners'", 'to': u"orm['contenttypes.ContentType']"}),
            'owner_id': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True'}),
            'owner_name': ('django.db.models.fields.TextField', [], {}),
            'pic1024max': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'pic1024x768': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'pic128max': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'pic128x128': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'pic180min': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'pic190x190': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'pic240min': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'pic320min': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'pic50x50': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'pic640x480': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'standard_height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'standard_width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'odnoklassniki_users.user': {
            'Meta': {'object_name': 'User'},
            'allows_anonym_access': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'current_status': ('django.db.models.fields.TextField', [], {}),
            'current_status_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'current_status_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'fetched': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gender': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'has_email': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_service_invisible': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'last_online': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'locale': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photo_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'pic1024x768': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'pic128max': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'pic128x128': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'pic180min': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'pic190x190': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'pic240min': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'pic320min': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'pic50x50': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'pic640x480': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'private': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'registered_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'url_profile': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'url_profile_mobile': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['odnoklassniki_photos']