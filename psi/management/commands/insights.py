from django.core.management import BaseCommand, CommandError
from django.core.validators  import URLValidator
from django.conf import settings

from optparse import make_option
from psi.models import PageInsight, RuleResults
#GOOGLE DATA API
from apiclient.discovery import build


class Command(BaseCommand):
    help = "Create PageSpeedInsights for a given URL."
    option_list = BaseCommand.option_list + (
    	make_option("--url", "-u", action="store", dest="url",
    		help="The URL of the page for which the PageSpeed Insights API should generate results."),
    	make_option("--strategy", "-s", action="store", dest="strategy", default="desktop", 
    		help="The strategy to use when analyzing the page. Valid values are desktop and mobile."),
    	make_option("--locale", "-l", action="store", dest="locale", default="en_US",
    		help="The locale that results should be generated in. See the list of supported locales. If the specified locale is not supported, the default locale is used."),
    	make_option("--rule", "-r", action="store", dest="rule",
    		help="The PageSpeed rules to run. Can be specified multiple times (for example, &rule=AvoidBadRequests&rule=MinifyJavaScript) to request multiple rules. If unspecified, all rules for the current strategy are used. Most users of the API should not need to specify this parameter."),
    	make_option("--key", "-k", action="store", dest="key",
    		help="The Google developer API key used when making the request."),
    	)


    def _processRules(self, data, pageInsight):
    	for key in data:
    		ruleResult = RuleResults()     		
    		ruleResult.title = data[key]['localizedRuleName']
    		ruleResult.impact = data[key]['ruleImpact']
    		ruleResult.description = data[key]['urlBlocks'][0]['header']['format']
    		ruleResult.pageInsight = pageInsight
    		ruleResult.save()


    def _processPageInsight(self, data):
    	pageInsight = PageInsight()
    	pageInsight.json = data
    	pageInsight.responseCode = data["responseCode"]
    	pageInsight.title = data["title"]
    	pageInsight.score = data["score"]
    	pageInsight.url = data['id']
    	pageInsight.numberResources = data['pageStats']["numberResources"]
    	pageInsight.numberHosts = data['pageStats']["numberHosts"]
    	pageInsight.totalRequestBytes = int(data['pageStats']["totalRequestBytes"])
    	pageInsight.numberStaticResources = data['pageStats']["numberStaticResources"]
    	pageInsight.htmlResponseBytes = int(data['pageStats']["htmlResponseBytes"])
    	pageInsight.cssResponseBytes = int(data['pageStats'].get("cssResponseBytes",0))
    	pageInsight.imageResponseBytes = int(data['pageStats'].get("imageResponseBytes",0))
    	pageInsight.javascriptResponseBytes = int(data['pageStats'].get("javascriptResponseBytes",0))
    	pageInsight.otherResponseBytes = int(data['pageStats'].get("otherResponseBytes",0))
    	pageInsight.numberJsResources = int(data['pageStats'].get("numberJsResources",0))
    	pageInsight.numberCssResources = int(data['pageStats'].get("numberCssResources",0))
    	pageInsight.strategy = self.strategy
    	pageInsight.save()
    	return pageInsight


    def _processPageStats(self, data, pageInsight):
		pageStat = PageStats()
		pageStat.numberResources = data["numberResources"]
		pageStat.numberHosts = data["numberHosts"]
		pageStat.totalRequestBytes = int(data["totalRequestBytes"])
		pageStat.numberStaticResources = data["numberStaticResources"]
		pageStat.htmlResponseBytes = int(data["htmlResponseBytes"])
		pageStat.cssResponseBytes = int(data["cssResponseBytes"])
		pageStat.imageResponseBytes = int(data["imageResponseBytes"])
		pageStat.javascriptResponseBytes = int(data["javascriptResponseBytes"])
		pageStat.otherResponseBytes = int(data["otherResponseBytes"])
		pageStat.numberJsResources = int(data["numberJsResources"])
		pageStat.numberCssResources = int(data["numberCssResources"])
		pageStat.pageInsight = pageInsight
		pageStat.save()
		return pageStat


    def _process_results(self, data):
    	pageInsight = self._processPageInsight(data)
    	self._processRules(data['formattedResults']['ruleResults'],pageInsight)


    def handle(self, *args, **options):
        try:
        	urls = []
        	url = options.get('url')

        	if url:
        		urls.append(url)
        	else:
        		surls = getattr(settings, 'INSIGHTS_URLS', None)
        		if surls:
        			for url in surls:
        				urls.append(url)
        		else:
        			raise BaseException("No URLs provided. Please either pass a URL as an argument or define INSIGHTS_URLS in settings file.")

        	self.strategy = options.get('strategy')
        	locale = options.get('locale')
        	rule = options.get('rule')
        	key = options.get('key')
        	
        	if options.get('key', False):
        		key = getattr(settings,'GOOGLE_API_KEY', None)

        	service = build(serviceName='pagespeedonline', version='v1', developerKey=key)
        	for url in urls:
	        	try:
	        		URLValidator(url)
	        	except ValidationError, e:
	        		raise e
	        	results  = service.pagespeedapi().runpagespeed(url=url, strategy=self.strategy, locale=locale, rule=rule).execute()
	        	self._process_results(results)

        except Exception, e:
            raise CommandError, e.message

