from django.shortcuts import render, redirect
from .models import Usuario, Dispositivo
from .forms import UsuarioForm, DispositivoForm, EncuestaForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view():
    pass 

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
    if request.method == 'POST':
            form.save()
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

    return render(request, 'dispositvios.html', context={"usuario_id": usuario.id,'dispositivos': dispositivos, 'form':form})

@login_required()
def removeDispositivo(request, upk, dpk):
    usuairo = Usuario.objects.get(pk = upk)
    dispositivo = Dispositivo.objects.get(pk = dpk)
    usuairo.dispositivos.remove(dispositivo)
    usuairo.save()
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
                return redirect('home')
        
    return render(request, 'encuesta.html', context={'form':form})
