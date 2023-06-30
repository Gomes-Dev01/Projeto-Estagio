from django import forms
from .models import Usuario, NivelAcesso, MenuEntrada

class InsereUsuarioForm(forms.ModelForm):
    class Meta:
       model = Usuario
       fields = "__all__"


class criaNivel(forms.ModelForm):
    class Meta:
        model = NivelAcesso
        fields = "__all__"


class criaMenu(forms.ModelForm):
    class Meta:
        model = MenuEntrada
        fields = "__all__"


class UsuarioLoginForm(forms.Form):
    usuario = forms.CharField(required=True, max_length=255)
    senha = forms.CharField(widget=forms.PasswordInput())


