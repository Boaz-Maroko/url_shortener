from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', shorten_url, name='home'),
]
