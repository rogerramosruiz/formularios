from django.shortcuts import render, redirect
from .models import Usuario, Dispositivo
from .forms import UsuarioForm, DispositivoForm, EncuestaForm
from django.contrib.auth.decorators import login_required
from .utils import log
import copy

# Create your views here.
@login_required()
def listar_personal(request):
    query = request.GET.get('query')
    usuarios = Usuario.objects.all()
    if query:
        usuarios = Usuario.objects.filter(nombre__icontains=query)
    usuarios = usuarios[0:20]
    return render(request, 'listar_u.html', context={'usuarios': usuarios})

@login_required()
def editar_usuario(request, pk):
    usuario = Usuario.objects.get(pk = pk)
    form = UsuarioForm(request.POST or None, instance = usuario)
    usuario_before = copy.copy(usuario)
    if request.method == 'POST':
            if form.is_valid():                
                edited_user = form.save()
                log(request, f'USUARIO EDITADO | ANTES: {usuario_before} | DESPUES: {edited_user}')
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
            log(request, f'NUEVO DISPOSITIVO: {dispositivo} | PARA: {usuario}')
            usuario.save()

    return render(request, 'dispositvios.html', context={"usuario_id": usuario.id,'dispositivos': dispositivos, 'form':form})

@login_required()
def removeDispositivo(request, upk, dpk):
    usuario = Usuario.objects.get(pk = upk)
    dispositivo = Dispositivo.objects.get(pk = dpk)
    usuario.dispositivos.remove(dispositivo)
    usuario.save()
    log(request, f'DISPOSITIVO BORRADO: {dispositivo} | DE: {usuario.id} {usuario.nombre}')
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
                log(request, f'ENCUESTA LLENADA: {encuesta} |PARA {usuario.id} {usuario.nombre}')
                return redirect('home')
        
    return render(request, 'encuesta.html', context={'form':form})
