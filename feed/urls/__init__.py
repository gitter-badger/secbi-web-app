# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^$', 'feed.views.base.inicio', name='inicio'),
                       url(r'^equipo/', 'feed.views.base.sobre', name='sobre'),
                       #urls de section proyectos
                       url(r'^proyectos/', 'feed.views.projects.proyectos', name='proyectos'),
                       url(r'^verproyecto/(?P<pk>\d+)/$', 'feed.views.projects.ver_project', name='ver_project'),
                       url(r'^nuevoproyecto/', 'feed.views.projects.new_project', name='new_project'),
                       url(r'^editarproyecto/(?P<pk>\d+)/$', 'feed.views.projects.edit_project', name='edit_project'),
                       #Agenda
                       url(r'^agenda/', 'feed.views.base.agenda', name='agenda'),
                       )
