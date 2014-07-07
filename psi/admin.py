from django.contrib import admin
from psi.models import PageInsight, RuleResults

class RuleResultsAdmin(admin.ModelAdmin):
	list_display = ('title', 'impact', 'pageInsight')

class PageInsightAdmin(admin.ModelAdmin):
	list_display = ('title', 'url', 'strategy', 'score', 'responseCode', 'numberResources', 'imageResponseBytes', 'htmlResponseBytes', 'javascriptResponseBytes')

admin.site.register(PageInsight, PageInsightAdmin)
admin.site.register(RuleResults, RuleResultsAdmin)