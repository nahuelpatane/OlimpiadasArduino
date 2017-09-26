from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'Arduinitos.views.verhome', name='Inicio' ),
       
                      )
