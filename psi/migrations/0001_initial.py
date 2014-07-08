# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PageInsight'
        db.create_table(u'psi_pageinsight', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('responseCode', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('strategy', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('numberResources', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('numberHosts', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('totalRequestBytes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('numberStaticResources', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('htmlResponseBytes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cssResponseBytes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('imageResponseBytes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('javascriptResponseBytes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('otherResponseBytes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('numberJsResources', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('numberCssResources', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('json', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'psi', ['PageInsight'])

        # Adding model 'RuleResult'
        db.create_table(u'psi_ruleresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('impact', self.gf('django.db.models.fields.FloatField')()),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pageInsight', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['psi.PageInsight'])),
        ))
        db.send_create_signal(u'psi', ['RuleResult'])

        # Adding model 'Screenshot'
        db.create_table(u'psi_screenshot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')()),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
            ('data', self.gf('django.db.models.fields.TextField')()),
            ('mime_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pageInsight', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['psi.PageInsight'])),
        ))
        db.send_create_signal(u'psi', ['Screenshot'])


    def backwards(self, orm):
        # Deleting model 'PageInsight'
        db.delete_table(u'psi_pageinsight')

        # Deleting model 'RuleResult'
        db.delete_table(u'psi_ruleresult')

        # Deleting model 'Screenshot'
        db.delete_table(u'psi_screenshot')


    models = {
        u'psi.pageinsight': {
            'Meta': {'object_name': 'PageInsight'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'cssResponseBytes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'htmlResponseBytes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageResponseBytes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'javascriptResponseBytes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'json': ('django.db.models.fields.TextField', [], {}),
            'numberCssResources': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'numberHosts': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'numberJsResources': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'numberResources': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'numberStaticResources': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'otherResponseBytes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'responseCode': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'strategy': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'totalRequestBytes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'psi.ruleresult': {
            'Meta': {'object_name': 'RuleResult'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impact': ('django.db.models.fields.FloatField', [], {}),
            'pageInsight': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['psi.PageInsight']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'psi.screenshot': {
            'Meta': {'object_name': 'Screenshot'},
            'data': ('django.db.models.fields.TextField', [], {}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mime_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pageInsight': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['psi.PageInsight']"}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['psi']