from django.conf import settings
from django.core.cache import cache
#from syncr.twitter import models
from django.contrib.redirects.models import Redirect

#def tweet(request):
#    tweet = cache.get('tweet')
#
#    if tweet:
#        return {"tweet": tweet}
#
#    u = models.TwitterUser.objects.get(id=1)
#    tweet = u.tweet_set.order_by('-pub_date')[0]
#
#    cache.set('tweet', tweet, settings.TWITTER_TIMEOUT)
#
#    return {"tweet": tweet}

def redirects(request):
    """
    Adds a list of redirects for target=_blanking.
    
    TODO: Filter by site
    """
    redirects = cache.get('redirects')

    if redirects:
        return {"redirects": redirects}

    redirects = Redirect.objects.filter(new_path__startswith="http://").exclude(
            new_path__startswith="http://waituntildarkfringe.com")

    cache.set("redirects", redirects)

    return {"redirects": redirects}



