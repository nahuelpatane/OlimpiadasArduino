from django.conf.urls import url
from django.views.generic import RedirectView
from Arduinitos import views
urlpatterns = [
            url(r'^$', RedirectView.as_view(url='home', permanent=False), name='root'),
            url(r'^home/$', views.verhome , name='home' ),
            ]
