from django.conf.urls import url

from index.views import show_views
from .views import *

urlpatterns = [
	# 访问路径是index的时候，交给index_views去处理
	url(r'^$', index_views),
	url(r'show/$', show_views),
]
