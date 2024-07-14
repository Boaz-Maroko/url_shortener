import pyshorteners
from django.conf import settings


APIKEY = settings.BITLY_API_TOKEN

# write pyshortener

def short(url):
    shortener = pyshorteners.Shortener(api_key=APIKEY)
    short_url = shortener.bitly.short(url)
    return short_url