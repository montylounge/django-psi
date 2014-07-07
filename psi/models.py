from django.db import models
from django.utils.translation import ugettext as _

from datetime import datetime

class PageInsight(models.Model):
    responseCode = models.IntegerField(_('Response Code'), default=0)
    title = models.CharField(_('Page Title'), max_length=255)
    strategy = models.CharField(_('Strategy'), max_length=50)
    score = models.IntegerField(_('Score'), default=0)
    url = models.URLField(_('URL'))
    numberResources = models.IntegerField(_('Number of Resources'), default=0)
    numberHosts = models.IntegerField(_('Number of Hosts'), default=0)
    totalRequestBytes = models.IntegerField(_('Total Request Bytes'), default=0)
    numberStaticResources = models.IntegerField(_('Number of Static Resources'), default=0)
    htmlResponseBytes = models.IntegerField(_('HTML Response Bytes'), default=0)
    cssResponseBytes = models.IntegerField(_('CSS Response Bytes'), default=0)
    imageResponseBytes = models.IntegerField(_('Image Response Bytes'), default=0)
    javascriptResponseBytes = models.IntegerField(_('Javascript Response Bytes'), default=0)
    otherResponseBytes = models.IntegerField(_('Other Response Bytes'), default=0)
    numberJsResources = models.IntegerField(_('Number of JS Resources'), default=0)
    numberCssResources = models.IntegerField(_('Number of CSS Resources'), default=0)
    created_date = models.DateTimeField(_('Created Date'), default=datetime.now())
    json = models.TextField(_('JSON Response'))

    def __unicode__(self):
        return _('PageInights for %s on %s') % (self.url, self.created_date)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = datetime.now()
        super(PageInsight, self).save(*args, **kwargs)


class RuleResults(models.Model):
    title = models.CharField(_('Page Title'), max_length=255)
    impact = models.FloatField(_('Impact'))
    description = models.TextField(_('Description'), blank=True, null=True)
    pageInsight = models.ForeignKey(PageInsight)

    def __unicode__(self):
        return self.title
