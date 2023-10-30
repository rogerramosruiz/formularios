from django.shortcuts import render, redirect
from .models import Usuario, Dispositivo, Log
from .forms import UsuarioForm, DispositivoForm, EncuestaForm
from django.contrib.auth.decorators import login_required
from .utils import logger
import copy


# Create your views here.
@login_required()
def listar_personal(request):
    query = request.GET.get('query')
    usuarios = Usuario.objects.all()
    if query:
        query = query.strip()
        usuarios = Usuario.objects.filter(nombre__icontains=query)
    usuarios = usuarios[0:20]
    usuarios_dic = []
    for i in usuarios:
        data = {}
        data['id'] = i.id
        data['nombre'] = i.nombre
        data['codigo'] = i.codigo
        data['carnet'] = i.carnet
        data['extension'] = i.extension
        data['cargo'] = i.cargo
        data['unidad'] = i.unidad
        data['encuesta'] = i.encuesta
        data['numdisp'] = len(i.dispositivos.all())
        usuarios_dic.append(data)

    return render(request, 'listar_u.html', context={'usuarios': usuarios_dic})

@login_required()
def editar_usuario(request, pk):
    usuario = Usuario.objects.get(pk = pk)
    form = UsuarioForm(request.POST or None, instance = usuario)
    usuario_before = copy.copy(usuario)
    if request.method == 'POST':
            if form.is_valid():                
                edited_user = form.save()
                logger(request,accion="USUARIO EDITADO",usuario = edited_user, messagedb= f'ANTES: {usuario_before}', messagetxt=f'USUARIO EDITADO | ANTES: {usuario_before} | DESPUES: {edited_user}')
                return redirect('home')

    return render(request, 'editarUsuario.html', context={'form': form})

@login_required()
def dispositivos(request, pk):
    usuario = Usuario.objects.get(pk = pk)
    dispositivos = usuario.dispositivos.all()
    form = DispositivoForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            dispositivo = form.save()
            usuario.dispositivos.add(dispositivo)
            usuario.save()
            logger(request,accion="NUEVO DISPOSITIVO:",usuario = usuario, messagedb= f'NUEVO DISPOSITIVO: {dispositivo}', messagetxt=f'NUEVO DISPOSITIVO: {dispositivo}')
            form  = DispositivoForm(None)

    return render(request, 'dispositvios.html', context={"usuario_id": usuario.id,'dispositivos': dispositivos, 'form':form})

@login_required()
def removeDispositivo(request, upk, dpk):
    usuario = Usuario.objects.get(pk = upk)
    dispositivo = Dispositivo.objects.get(pk = dpk)
    usuario.dispositivos.remove(dispositivo)
    usuario.save()
    logger(request, accion="DISPOSITIVO BORRADO:", usuario = usuario, messagedb= f'{dispositivo}', messagetxt=f'DISPOSITIVO BORRADO: {dispositivo} | DE: {usuario.id} {usuario.nombre}')
    return redirect('dispositivos', pk= upk)

@login_required()
def encuesta(request, pk):
    usuario = Usuario.objects.get(pk = pk)
    encuesta = usuario.encuesta
    form = EncuestaForm(request.POST or None, instance=encuesta)
    
    if request.method == 'POST':
        if form.is_valid():
            if form.is_valid():
                encuesta = form.save()
                usuario.encuesta = encuesta
                usuario.save()
                logger(request, accion="ENCUESTA LLENADA:", usuario = usuario, messagedb= f'{encuesta}', messagetxt=f'ENCUESTA LLENADA: {encuesta} |PARA {usuario.id} {usuario.nombre}')
                return redirect('home')
                    
    return render(request, 'encuesta.html', context={'form':form})
