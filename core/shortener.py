import pyshorteners


APIKEY = "021e5f275c2efccff85d477232a6d577978a1f05"

# write pyshortener

def short(url):
    shortener = pyshorteners.Shortener(api_key=APIKEY)
    short_url = shortener.bitly.short(url)
    return short_url