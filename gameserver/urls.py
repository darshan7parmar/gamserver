"""gameserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from gameserverapp import views

urlpatterns = [
    url(r'^gameserver/game/create', views.create),
    url(r'^gameserver/game/join', views.join),
    url(r'^gameserver/game/info', views.info),
    url(r'^gameserver/game/start', views.start),
    url(r'^gameserver/game/play', views.play),
    url(r'^gameserver/game/pass', views.pass_turn),
    url(r'^gameserver/game/locate', views.locate_word),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
