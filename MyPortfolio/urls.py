"""MyPortfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage, name='home'),
    url(r'^whoami/$', whopage, name='who'),
    url(r'^myprojects/$', projectspage, name='projects'),
    url(r'^myskills/$', Skillzpage, name='skills'),
    url(r'^products/', include("ListWeb.urls"), name='products'),
    url(r'^faketube/', include("faketube.urls"), name='videos'),
    url(r'^DownloadAblePrograms/', include("DownloadAbleFiles.urls"), name='download'),
    url(r'^blog/', include(("myblog.urls", 'myblog'), namespace='xxx'), name='blog')
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
