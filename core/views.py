from django.shortcuts import render, redirect, HttpResponse
from .models import URL
from hashids import Hashids
from .shortener import short

hashids = Hashids(min_length=4, salt='mangos')

# Create your views here.
def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST['url']
        short_url = short(original_url)

        url = URL(original_url=original_url, short_url=short_url)

        url.save()

        # url, created = URL.objects.get_or_create(original_url=original_url)
        
        # if created:
        #     url.save()

        # short_url = shorten_url(url)
        # short_url.save()
        return render(request, 'home.html', {'short_url': short_url})
    return render(request, 'home.html')

        