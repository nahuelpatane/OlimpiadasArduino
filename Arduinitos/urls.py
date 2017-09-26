from django.conf.urls import url
from django.views.generic import RedirectView
from Arduinitos import views
urlpatterns = [
            url(r'^$', RedirectView.as_view(url='home', permanent=False), name='root'),
            url(r'^home/$', views.VerHome , name='home' ),
            url(r'^temp/$', views.VerTemp , name='temptemp' ),
            url(r'^luz/$', views.VerLuz , name='luztemp' ),
            url(r'^agua/$', views.VerAgua , name='aguatemp' ),
            ]
