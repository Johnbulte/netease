from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
    # 访问路径是/的时候，交给index_views去处理
    url(r'^$', index_views),
    # 访问路径是/login的时候，交给login_views去处理
    url(r'^login$', login_views),
    # 访问路径是/register的时候，交给register_views去处理
    url(r'^register$', register_views),
]
urlpatterns += [
    path('01_template.html/', getTemp_views),
    path('02_template.html/', getTemp1_views),
    path('03_var.html', var_views),
    path('04_static.html', static_views),
	path('05_temp.html',temp_views),
]
