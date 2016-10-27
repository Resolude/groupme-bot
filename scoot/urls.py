from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

bot_url = 'https://api.groupme.com/v3/bots/post'
