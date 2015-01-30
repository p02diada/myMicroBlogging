from django.conf.urls import patterns, url
from app_myMicroBlogging import views
from django.views.generic import TemplateView

urlpatterns=patterns('',
	url(r'^crear_usuario/$', views.crear_usuario, name='crear_usuario'),
	url(r'^user_login/$', views.user_login, name='user_login'),
	url(r'^user_logout/$', views.user_logout, name='user_logout'),
	url(r'^home/$', views.home, name='home'),
	#url(r'^listarMicroPost/(?P<my_user_id>\d+)/$', views.listarMicroPost, name='listarMicroPost'),
	url(r'^listarMicroPost/$', views.listarMicroPost, name='listarMicroPost'),
	url(r'^crearMicroPost/$', views.crearMicroPost, name='crearMicroPost'),
	url(r'^seguidores/$', views.seguidores, name='seguidores'),
	url(r'^seguidos/$', views.seguidos, name='seguidos'),
	url(r'^listarTablon/$', views.listarTablon, name='listarTablon'),
	url(r'^verPerfil/(?P<usuario_id>\d+)/$', views.verPerfil, name='verPerfil'),
	url(r'^anyadirSeguidos/(?P<usuario_id>\d+)/$', views.anyadirSeguidos, name='anyadirSeguidos'),
	url(r'^quitarSeguidos/(?P<usuario_id>\d+)/$', views.quitarSeguidos, name='quitarSeguidos'),
	url(r'^editarUsuario/$', views.editarUsuario, name='editarUsuario'),
	url(r'^eliminarMicroPost/(?P<micro_post_id>\d+)/$', views.eliminarMicroPost, name='eliminarMicroPost'),
	url(r'^repostear/(?P<micro_post_id>\d+)/$', views.repostear, name='repostear'),
	url(r'^anyadirFavorito/(?P<micro_post_id>\d+)/$', views.anyadirFavorito, name='anyadirFavorito'),
	url(r'^listarFavoritos/$', views.listarFavoritos, name='listarFavoritos'),
	url(r'^eliminarFavoritos/(?P<favorito_id>\d+)/$', views.eliminarFavoritos, name='eliminarFavoritos'),
	url(r'^verListas/$', views.verListas, name='verListas'),
	url(r'^mostrarLista/(?P<lista_id>\d+)/$', views.mostrarLista, name='mostrarLista'),
	url(r'^elegirLista/(?P<usuario_id>\d+)/$', views.elegirLista, name='elegirLista'),
	url(r'^anyadirUsuarioLista/(?P<lista_id>\d+)/(?P<usuario_id>\d+)/$', views.anyadirUsuarioLista, name='anyadirUsuarioLista'),
	url(r'^eliminarLista/(?P<lista_id>\d+)/$', views.eliminarLista, name='eliminarLista'),
	url(r'^crearLista/$', views.crearLista, name='crearLista'),
	url(r'^verTT/$', views.verTT, name='verTT'),
	url(r'^verMicroPostTT/(?P<hashtag_id>\d+)/$', views.verMicroPostTT, name='verMicroPostTT'),
	url(r'^menciones/$', views.menciones, name='menciones'),
	url(r'^verSeguidos/(?P<usuario_id>\d+)/$', views.verSeguidos, name='verSeguidos'),
	url(r'^verSeguidores/(?P<usuario_id>\d+)/$', views.verSeguidores, name='verSeguidores'),






	#url(r'^crearMicroPost/(?P<my_user_id>\d+)/$', views.crearMicroPost, name='crearMicroPost'),

	#url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
	#url(r'^primero/$', views.mostrarPrimero, name='mostrarPrimero'),
#	url(r'^listaEquipos/$', views.listaEquipos, name='listaEquipos'),
#	url(r'^equipos/(?P<equipo_id>\d+)/$', views.mostrarEquipo, name='equipo'),
#	url(r'^listaJugadores/$', views.listaJugadores, name='listaJugadores'),
#	url(r'^jugador/(?P<jugador_id>\d+)/$', views.mostrarJugador, name='equipo'),
#	url(r'^jugador/eliminar/(?P<jugador_id>\d+)/$', views.eliminarJugador, name='equipo'),
#	url(r'^nuevoEquipo/$', views.nuevoEquipo , name='nuevoEquipo'),
#	url(r'^nuevoJugador/$', views.nuevoJugador, name='nuevoJugador'),
#	url(r'^editarJugador/(?P<jugador_id>\d+)/$', views.editarJugador, name='editarJugador'),
#	url(r'^editarEquipo/(?P<equipo_id>\d+)/$', views.editarEquipo, name='editarEquipo'),
#	url(r'^newUser/$', views.newUser, name='NewUser'),
#	url(r'^userlogin/$', views.user_login, name='NewUser'),

	

	
	
)