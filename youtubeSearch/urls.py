from django.conf.urls import url
from youtubeSearch.api import Videos
app_name = 'tests'

urlpatterns = [
    url('v1/videos/$', Videos.as_view()),
]
