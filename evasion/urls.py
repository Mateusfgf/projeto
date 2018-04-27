from django.conf.urls import url
from . import views

urlpatterns = [
	    url(r'^$', views.listar_dados, name='listar_dados'),
	    url(r'^evasion/(?P<pk>\d+)/$', views.listar_graficos, name='listar_graficos'),
	    url(r'^form/$', views.formulario_usuario, name='formulario_usuario')
]