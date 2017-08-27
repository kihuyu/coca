from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from datacollections import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^datacollections/$', views.datacollection_list,name='datacollection-list'),
    url(r'^datacollections/(?P<pk>[0-9]+)/$', views.datacollection_detail, name='datacollection-detail'),
    url(r'^users/$', views.user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail, name='user-detail'),
    url(r'^api-auth/', obtain_jwt_token, name='token'),


])
