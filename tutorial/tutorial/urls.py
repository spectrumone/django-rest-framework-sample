from django.conf.urls import url, include
from django.contrib import admin

import rest_framework
from rest_framework import routers

from snippets import views

''' Using non viewset class based views '''
# from snippets import urls as snippets_urls
''' Sample from another app using class based views; app might break if not commented out '''
# from quickstart import views

router = routers.DefaultRouter()

router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

''' Sample from another app; app might break if not commented out '''
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)), 
    # url(r'^', include(snippets_urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]
