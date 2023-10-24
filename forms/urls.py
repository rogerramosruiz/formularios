from django.urls import path
from forms import views

urlpatterns = [
    path('', views.listar_personal, name='home'),
    path('actualizar/<int:pk>', views.editar_usuario, name='editar_usuario'),
    path('dispositivos/<int:pk>', views.dispositivos, name='dispositivos'),
    path('deletedispositivo/<int:upk>/<int:dpk>', views.removeDispositivo, name='deletedispositivo'),
    path('encuesta/<int:pk>', views.encuesta, name='encuesta'),
]
