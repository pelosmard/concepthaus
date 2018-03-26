from django import forms
from .models import Talumnos, Tcalificaciones, Tmaterias


# Create your models here.


class AlumnosForm(forms.ModelForm):
    """Clase para manejo de los campos de la forma de alumnos."""

    def __init__(self, *args, **kwargs):
        super(AlumnosForm, self).__init__(*args, **kwargs)

    class Meta:
        """Clase Meta para manejo de los campos de la forma de Alumnos."""
        model = Talumnos

        fields = [
            'nombre',
            'ap_paterno',
            'ap_materno',
            'activo',
        ]

        labels = {
            'nombre': 'Coloque el nombre',
            'ap_paterno': 'Coloque el apellido paterno',
            'ap_materno': 'Coloque el apellido materno',
            'activo': 'Escoga si está activo o no',
        }

        help_texts = {
            'nombre': 'Coloque el nombre',
            'ap_paterno': 'Coloque el apellido paterno',
            'ap_materno': 'Coloque el apellido materno',
            'activo': 'Escoga si está activo o no',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'size': 80,
                'placeholder': 'Nombre',
                'required': 'True',
            }),
            'ap_paterno': forms.TextInput(attrs={
                'class': 'form-control',
                'size': 80,
                'placeholder': 'apellido paterno',
                'required': 'True',
            }),
            'ap_materno': forms.TextInput(attrs={
                'class': 'form-control',
                'size': 80,
                'placeholder': 'apellido materno',
                'required': 'True',
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-control',
            }),
        }


class MateriasForm(forms.ModelForm):
    """Clase para manejo de los campos de la forma de Materias."""

    def __init__(self, *args, **kwargs):
        super(MateriasForm, self).__init__(*args, **kwargs)

    class Meta:
        """Clase Meta para manejo de los campos de la forma de Materias."""
        model = Tmaterias

        fields = [
            'nombre',
            'activo',
        ]

        labels = {
            'nombre': 'Coloque el nombre',
            'activo': 'Escoja si está activo o no',
        }

        help_texts = {
            'nombre': 'Coloque el nombre',
            'activo': 'Escoga si está activo o no',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'size': 80,
                'placeholder': 'Nombre',
                'required': 'True',
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-control',
            }),
        }


class CalificacionesForm(forms.ModelForm):
    """Clase para manejo de los campos de la forma de calificaciones de alumnos."""

    def __init__(self, *args, **kwargs):
        super(CalificacionesForm, self).__init__(*args, **kwargs)

    class Meta:
        """Clase Meta para manejo de los campos de la formade calificaciones de alumnos."""
        model = Tcalificaciones

        fields = [
            'id_tmaterias',
            'id_t_usuarios',
            'calificacion',
            'fecha_registro',
        ]

        labels = {
            'id_tmaterias': 'Escoja la materia',
            'id_t_usuarios': 'Escoja el alumnos',
            'calificacion': 'Coloque el apellido materno',
            'fecha_registro': 'Escriba la fecha de registro',
        }

        help_texts = {
            'id_tmaterias': 'Escoja la materia',
            'id_t_usuarios': 'Escoja el alumnos',
            'calificacion': 'Coloque el apellido materno',
            'fecha_registro': 'Escriba la fecha de registro',
        }

        widgets = {
            'id_tmaterias': forms.ModelChoiceField(queryset=Tmaterias.objects.all(), to_field_name="nombre", attrs={
                'class': 'form-control',
                'required': 'True',
            }),
            'id_t_usuarios': forms.ModelChoiceField(queryset=Talumnos.objects.all(), to_field_name="nombre", attrs={
                'class': 'form-control',
                'required': 'True',
            }),
            'calificacion': forms.DecimalField(attrs={
                'class': 'form-control',
                'size': 80,
                'placeholder': 'calificacion',
                'required': 'True',
            }),
            'fecha_registro': forms.DateField(attrs={
                'class': 'form-control',
                'placeholder': 'Y-m-d',
                'required': 'True',
            }),
        }
