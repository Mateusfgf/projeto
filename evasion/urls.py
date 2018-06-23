from django.conf.urls import url
from . import views 
from evasion.views import *



urlpatterns = [
		url(r'^$', views.listar_dados, name='listar_dados'),
		url(r'^evasion/(?P<pk>\d+)/$', views.listar_graficos, name='listar_graficos'),
		url(r'^form/$', views.formulario_usuario, name='formulario_usuario'),
		url(r'^cadastro/$', Criar.as_view(), name='cadastro'),
		url(r'^lista/$', Lista.as_view(), name='lista'),
		url(r'^events/$', views.events, name='events')
		# url(r'^cadastro/$', views.Criar, name='cadastro'),
		# url(r'^lista/$', views.Lista, name='lista')

	]

# url(r'^cadastro/$', Criar.as_view(), name='cadastro'),
# url(r'^lista/$', Lista.as_view(), name='lista'),
# url(r'^admin/', include(admin.site.urls)),
