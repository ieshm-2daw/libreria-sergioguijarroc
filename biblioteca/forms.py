from django import forms
from .models import Libro, Valoracion


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = "__all__"
        widgets = {
            "fecha_publicacion": forms.DateInput(attrs={"type": "date"}),
        }


class ValoracionForm(forms.ModelForm):
    review = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Escribe tu valoración aquí"})
    )

    class Meta:
        model = Valoracion
        fields = ["rating", "review"]
