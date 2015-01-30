from app_myMicroBlogging.models import my_user, micro_post, favorito, lista, hashtag
from app_myMicroBlogging.forms import my_user_form, my_micro_post, edit_my_user_form, lista_form
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import re


# Create your views here.
def inicio(request):
	return redirect ('/app/user_login')

def crear_usuario(request):
	if request.method == 'POST':
		form =my_user_form(request.POST, request.FILES)
		if form.is_valid():
			#form.save()
			user = request.POST['username']
			passwd = request.POST['password']
			e_mail = request.POST['email']
			my_user.objects.create_user(username=user, password=passwd, email=e_mail)
			return redirect('/app/user_login')
	else:
		form= my_user_form()
	context = {'form':form}
	return render(request, 'app_myMicroBlogging/nuevo_my_user.html', context)


def user_login(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = request.POST['username']
			passwd = request.POST['password']
			access = authenticate(username=user, password=passwd)
			if access is not None:
				if access.is_active:
					login(request, access)
					#identificador=access.pk
					#return redirect('/app/home/')
					#context = {'access':access}
					#return render (request,'app_myMicroBlogging/home.html', context)
					return redirect('/app/home/')
				else:
					return HttpResponse ("User inactive")
			else:
				return HttpResponse ("No user")
	else:
		form = AuthenticationForm()
	context = {'form': form}
	return render(request,'app_myMicroBlogging/login.html', context)

@login_required(login_url='/app/user_login')
def user_logout(request):
	logout(request)
	return redirect ('/app/user_login/')

@login_required(login_url='/app/user_login')
def editarUsuario(request):
	usuario=my_user.objects.get(pk=request.user.pk)
	if request.method == 'POST':
		form =edit_my_user_form(request.POST, request.FILES, instance=usuario)
		if form.is_valid():
			form.save()
			return redirect('/app/listarTablon/')
	else:
		form= edit_my_user_form(instance=usuario)
	context = {'form':form}
	return render(request, 'app_myMicroBlogging/edit_my_user.html', context)



@login_required(login_url='/app/user_login')
def home(request):
	usuario=my_user.objects.get(pk=request.user.pk)
	context = {'usuario':usuario}
	return render(request,'app_myMicroBlogging/home.html', context)

@login_required(login_url='/app/user_login')
def verPerfil(request, usuario_id):
	usuario=my_user.objects.get(pk=usuario_id)
	micro=micro_post.objects.filter(usuario=usuario).order_by("-fecha")
	listaSeguidores=my_user.objects.filter(seguidos=usuario)
	numMicroPost=micro.count()
	numSegui=usuario.seguidos.count()
	numSeguidores=listaSeguidores.count()
	context={'usuario':usuario, 'micro':micro, 'numMicroPost':numMicroPost, 'numSegui':numSegui, 'numSeguidores':numSeguidores}
	return render(request,'app_myMicroBlogging/ver_perfil.html', context)


##########################################
##########################################
##########################################
##########################################
# GESTION MICRO POST

@login_required(login_url='/app/user_login')
def listarMicroPost(request):
	#usuario=my_user.objects.get(pk=my_user_id)
	usuario=my_user.objects.get(pk=request.user.pk)
	listaMicroPost=micro_post.objects.filter(usuario=usuario).order_by("-fecha")
	context={'listaMicroPost':listaMicroPost}
	return render(request,'app_myMicroBlogging/listar_micro_post.html', context)

@login_required(login_url='/app/user_login')
def crearMicroPost(request):
	usuario=my_user.objects.get(pk=request.user.pk)
	if request.method == 'POST':
		form =my_micro_post(request.POST, request.FILES)
		if form.is_valid():
			#form.save()
			content = request.POST['contenido']
			#user = request.POST['username']
			#passwd = request.POST['password']
			#e_mail = request.POST['email']
			micro, creado=micro_post.objects.get_or_create(contenido=content, usuario=usuario)
			hashtags=re.findall('(?:#([^\s]+))+', content)
			for hash in hashtags:
				h, created=hashtag.objects.get_or_create(nombre=hash)
				h.micro_post.add(micro)
				h.repeticiones=h.repeticiones+1
				h.save()

			return redirect('/app/listarMicroPost/')
	else:
		form= my_micro_post()
	context = {'form':form}
	return render(request, 'app_myMicroBlogging/crear_micro_post.html', context)

@login_required(login_url='/app/user_login')
def eliminarMicroPost(request, micro_post_id):
	post=micro_post.objects.get(pk=micro_post_id)
	post.delete()
	return redirect('/app/listarMicroPost/')

@login_required(login_url='/app/user_login')
def repostear(request, micro_post_id):
	post=micro_post.objects.get(pk=micro_post_id)
	usuario=my_user.objects.get(pk=request.user.pk)
	micro_post.objects.create(contenido=post.contenido, usuario=usuario)
	return redirect('/app/listarMicroPost/')


##########################################
##########################################
##########################################
##########################################
# GESTION SEGUIDORES Y SEGUIDOS

@login_required(login_url='/app/user_login')
def seguidores(request):
	usuario=my_user.objects.get(pk=request.user.pk)
	listaSeguidores=my_user.objects.filter(seguidos=usuario)
	context={'listaSeguidores':listaSeguidores, 'usuario':usuario}
	return render(request,'app_myMicroBlogging/listar_seguidores.html',context)

@login_required(login_url='/app/user_login')
def seguidos(request):
	usuario=my_user.objects.get(pk=request.user.pk)
	listaSeguidos=usuario.seguidos.all()
	context={'listaSeguidos':listaSeguidos}
	return render(request,'app_myMicroBlogging/listar_seguidos.html',context)

@login_required(login_url='/app/user_login')
def anyadirSeguidos(request, usuario_id):
	usuario=my_user.objects.get(pk=request.user.pk)
	usuarioAnyadir=my_user.objects.get(pk=usuario_id)
	usuario.seguidos.add(usuarioAnyadir)
	return redirect('/app/seguidos/')

@login_required(login_url='/app/user_login')
def quitarSeguidos(request, usuario_id):
	usuario=my_user.objects.get(pk=request.user.pk)
	usuarioQuitar=my_user.objects.get(pk=usuario_id)
	lista=usuario.seguidos.all()
	usuario.seguidos.remove(usuarioQuitar)
	context={'usuario':usuario, 'usuarioQuitar':usuarioQuitar, 'lista':lista}
	return redirect('/app/seguidos/')

@login_required(login_url='/app/user_login')
def listarTablon(request):
	usuario=my_user.objects.get(pk=request.user.pk)
	listaSeguidos=usuario.seguidos.all()
	listaMensajes=micro_post.objects.filter(usuario=listaSeguidos).order_by("-fecha")
	
	context={'listaMensajes':listaMensajes, 'usuario':usuario}
	return render(request,'app_myMicroBlogging/listarTablon.html', context)

def buscar(request):
	query = request.GET.get('busqueda', '')
	usuario=my_user.objects.get(username=request.user)
	mencion=False
	TT=False

	if query:


		if re.findall('(?:#([^\s]+))+', query): #busqueda de hashtags
			query=query.replace("#","")
			consulta=(Q(nombre__icontains=query))
			resultado = hashtag.objects.filter(consulta)
			TT=True
		elif re.findall('(?:@([^\s]+))+', query):  #busqueda de menciones
			query=query.replace("@","")
			consulta=(Q(contenido__icontains=query))
			resultado = micro_post.objects.filter(consulta)
			mencion=True
		else:
			consulta = (Q(username__icontains=query)) #busqueda de usuarios
			resultado = my_user.objects.filter(consulta)

		context={'resultado':resultado, 'TT':TT, 'mencion':mencion, 'query':query}
		return render(request, 'app_myMicroBlogging/busqueda.html', context)

	else:
		return HttpResponse('mal')



##########################################
##########################################
##########################################
##########################################
# FAVORITOS



@login_required(login_url='/app/user_login')
def anyadirFavorito(request, micro_post_id):
	post=micro_post.objects.get(pk=micro_post_id)
	usuario=my_user.objects.get(pk=request.user.pk)
	fav, created=favorito.objects.get_or_create(micro_post=post, usuarios=usuario)
	return redirect('/app/listarFavoritos/')

@login_required(login_url='/app/user_login')
def listarFavoritos(request):
	usuario=my_user.objects.get(pk=request.user.pk)
	listaFavoritos=favorito.objects.filter(usuarios=usuario)
	context={'listaFavoritos':listaFavoritos, 'usuario':usuario}
	return render(request,'app_myMicroBlogging/listar_favoritos.html', context)

@login_required(login_url='/app/user_login')
def eliminarFavoritos(request, favorito_id):
	fav=favorito.objects.get(pk=favorito_id)
	fav.delete()
	return redirect('/app/listarFavoritos/')

##########################################
##########################################
##########################################
##########################################
# LISTAS

@login_required(login_url='/app/user_login')
def verListas(request):
	usuario=my_user.objects.get(pk=request.user.pk)
	Listas=lista.objects.filter(usuario=usuario)
	context={'Listas':Listas}
	return render(request,'app_myMicroBlogging/ver_listas.html', context)	

@login_required(login_url='/app/user_login')
def mostrarLista(request,lista_id):
	Lista=lista.objects.get(pk=lista_id)
	usuarios=Lista.listaUsuarios.all()
	listaMensajes=micro_post.objects.filter(usuario=usuarios)
	context={'listaMensajes':listaMensajes, 'Lista':Lista}
	return render(request, 'app_myMicroBlogging/mostrar_lista.html', context)

@login_required(login_url='/app/user_login')
def elegirLista(request,usuario_id):
	usuario=my_user.objects.get(pk=request.user.pk)
	Listas=lista.objects.filter(usuario=usuario)
	usuarioParaLista=my_user.objects.get(pk=usuario_id)
	context={'Listas':Listas, 'usuarioParaLista':usuarioParaLista}
	return render(request,'app_myMicroBlogging/elegir_lista.html', context)

@login_required(login_url='/app/user_login')
def anyadirUsuarioLista(request, lista_id, usuario_id):
	usuario=my_user.objects.get(pk=usuario_id)
	Lista=lista.objects.get(pk=lista_id)
	Lista.listaUsuarios.add(usuario)
	return redirect('/app/verListas/')

@login_required(login_url='/app/user_login')
def eliminarLista(request, lista_id ):
	Lista=lista.objects.get(pk=lista_id)
	Lista.delete()
	return redirect('/app/verListas/')


@login_required(login_url='/app/user_login')
def crearLista(request):
	usuario=my_user.objects.get(pk=request.user.pk)
	if request.method == 'POST':
		form =lista_form(request.POST, request.FILES)
		if form.is_valid():
			name=request.POST['nombre']
			lista.objects.get_or_create(nombre=name, usuario=usuario)
			return redirect('/app/verListas/')
	else:
		form= lista_form()
	context = {'form':form}
	return render(request, 'app_myMicroBlogging/crear_lista.html', context)

##########################################
##########################################
##########################################
##########################################
# OTROS
@login_required(login_url='/app/user_login')
def verTT(request):
	hashtags=hashtag.objects.all().order_by("-repeticiones")
	TT=hashtags[:5]
	context={'hashtags':TT}
	return render(request, 'app_myMicroBlogging/ver_TT.html',context)
@login_required(login_url='/app/user_login')
def verMicroPostTT(request, hashtag_id):
	h=hashtag.objects.get(pk=hashtag_id)
	listaMensajes=micro_post.objects.filter(hashtag__id=hashtag_id)
	context={'listaMensajes':listaMensajes, 'h':h}
	return render(request, 'app_myMicroBlogging/ver_micro_post_TT.html', context)
@login_required(login_url='/app/user_login')
def menciones (request):
	usuario=my_user.objects.get(pk=request.user.pk)
	usuario="@"+usuario.username
	consulta=(Q(contenido__icontains=usuario))
	resultado = micro_post.objects.filter(consulta)
	context={'resultado':resultado}
	return render(request, 'app_myMicroBlogging/mis_menciones.html', context)

@login_required(login_url='/app/user_login')
def verSeguidos(request, usuario_id):
	usuario=my_user.objects.get(pk=usuario_id)
	listaSeguidos=usuario.seguidos.all()
	context={'listaSeguidos':listaSeguidos}
	return render(request,'app_myMicroBlogging/listar_seguidos.html',context)

@login_required(login_url='/app/user_login')
def verSeguidores(request, usuario_id):
	usuario=my_user.objects.get(pk=usuario_id)
	listaSeguidores=my_user.objects.filter(seguidos=usuario)
	context={'listaSeguidores':listaSeguidores, 'usuario':usuario}
	return render(request,'app_myMicroBlogging/listar_seguidores.html',context)










