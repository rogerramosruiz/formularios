from django import forms
from .models import Usuario, Encuesta, TipoDispositivo, Dispositivo, Nivel, Ofimatica, SitemaOperativo, Unidad, Edificio, Cargo

class UsuarioForm(forms.ModelForm):
    
    nombre = forms.CharField(label="Nombre completo", widget=forms.widgets.TextInput(
    attrs={"placeholder": "Juan Perez Perez", "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700", }))
    carnet = forms.CharField(max_length=10, widget=forms.widgets.NumberInput(attrs={"placeholder": "123456789", "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700"}))
    extension = forms.CharField(max_length=5, label="Extension",widget=forms.widgets.TextInput(attrs={"placeholder": "LP", "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700"}))
    unidad  = forms.ModelChoiceField(queryset=Unidad.objects.all().order_by("nombre"), widget=forms.Select(attrs={'class': 'text-white bg-sky-500 hover:bg-sky-600 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-0 py-2.5 text-center inline-flex items-center'}))
    edificio  = forms.ModelChoiceField(queryset=Edificio.objects.all().order_by("nombre"), widget=forms.Select(attrs={'class': 'text-white bg-sky-500 hover:bg-sky-600 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center'}))
    cargo = forms.ModelChoiceField(queryset=Cargo.objects.all().order_by("nombre"), widget=forms.Select(attrs={'class': 'text-white bg-sky-500 hover:bg-sky-600 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-0 py-2.5 text-center inline-flex items-center'}))
    class Meta:
        model = Usuario
        fields = ('nombre', 'carnet', 'extension', 'unidad', 'edificio', 'cargo') 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['readonly'] = True

class DispositivoForm(forms.ModelForm):
    tipo = forms.ModelChoiceField(queryset=TipoDispositivo.objects.all(), widget=forms.Select(attrs={'class': 'text-white bg-emerald-500 hover:bg-emerald-600 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center'}))
    modelo = forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={"placeholder": "Epson L3250", "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700"}))
    fecha_fabricacion = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 
        "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}))
    
    class Meta:
        model = Dispositivo
        fields = ('tipo', 'modelo', 'fecha_fabricacion') 


class EncuestaForm(forms.ModelForm):
    software_libre = forms.ModelChoiceField(label="Conocimiento de Sotware Libre",queryset=Nivel.objects.all(), widget=forms.Select(attrs={'class': 'text-white bg-sky-500 hover:bg-sky-600 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center'}))
    estandares_abiertos = forms.ModelChoiceField(label="Conocimiento de Estándares abiertos", queryset=Nivel.objects.all(), widget=forms.Select(attrs={'class': 'text-white bg-sky-500 hover:bg-sky-600 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center'}))
    ofimatica = forms.ModelChoiceField(queryset=Ofimatica.objects.all(), widget=forms.Select(attrs={'class': 'text-white bg-sky-500 hover:bg-sky-600 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center'}))
    sistema_operativo = forms.ModelChoiceField(queryset=SitemaOperativo.objects.all(), widget=forms.Select(attrs={'class': 'text-white bg-sky-500 hover:bg-sky-600 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center'}))

    descripcion_caracteristicas = forms.CharField(label="Descripción y características (Opcional)", required=False, max_length=500, widget=forms.widgets.TextInput(attrs={"class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700"}))    
    otros = forms.CharField(label="Otros software que necesiten licencia (Opcional)", required=False, max_length=100, widget=forms.widgets.TextInput(attrs={"placeholder": "Adobe Photoshop, Adobe Premiere", "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700"}))


    nombre_equipo = forms.CharField(max_length=200, widget=forms.widgets.TextInput(attrs={"class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700"}))
    nombre_usuario = forms.CharField(label="Login del usuario", max_length=50, widget=forms.widgets.TextInput(attrs={"class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700"}))
    numero_tag = forms.CharField(label="Número de tag (Opcional)", max_length=100, required=False, widget=forms.widgets.TextInput(attrs={"class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700"}))
    # portatil o escritorio

    portatil_escritorio = forms.ChoiceField(label="Tipo de dispositivo",widget=forms.RadioSelect() ,choices=(("PORTATIL", "Portátil"),("ESCCRITORIO", "Escritorio") ))
    dominio = forms.BooleanField(widget=forms.widgets.CheckboxInput(attrs={"class": "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"}), required=False)
    antivirus = forms.BooleanField(widget=forms.widgets.CheckboxInput(attrs={"class": "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"}), required=False)

    class Meta:
        model = Encuesta
        fields = ('software_libre', 'estandares_abiertos', 'ofimatica', 'sistema_operativo', 'descripcion_caracteristicas', 'otros', 'nombre_equipo', 'nombre_usuario',
                  'numero_tag', 'portatil_escritorio', 'dominio', 'antivirus') 

class EdificioForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={"class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700"}))
    
    class Meta:
        model = Edificio
        fields = ('nombre', ) 
