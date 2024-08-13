from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from usuarios.models import Usuario

class UserEditForm(UserChangeForm):
    data_nascimento = forms.DateField(
        widget=forms.NumberInput(
            attrs={
                'type': 'date',
                'class': 'form-control' 
            }
        )
    )

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name', 'cpf', 'data_nascimento', 'endereco')

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        # Iterar sobre os campos para adicionar classes
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'username':
                field.help_text = None  # Removendo o texto de ajuda para 'username'

        # Remover o campo de senha
        if 'password' in self.fields:
            del self.fields['password']

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2 text-white'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-2 text-white'}))

class UserRegistrationForm(UserCreationForm):
    data_nascimento = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control mb-2 text-white'}))
    endereco = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control mb-2 text-white'}))

    class Meta:
        model = Usuario
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'cpf', 'data_nascimento', 'endereco')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs.update({'class': 'form-control mb-2 text-white'})