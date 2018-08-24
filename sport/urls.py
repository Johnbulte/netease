from django.conf.urls import url

from .views import *

urlpatterns = [
    #访问路径是index的时候，交给index_views去处理
    url(r'^$',index_views),
]
