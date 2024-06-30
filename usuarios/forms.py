from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserEditForm(UserChangeForm):
    data_nascimento = forms.DateField(
        widget=forms.NumberInput(
            attrs={
                'type': 'date',  
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'cpf', 'data_nascimento', 'endereco')

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        # self.fields['username'].disabled = True
        # Remover o campo de senha
        if 'password' in self.fields:
            del self.fields['password']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    data_nascimento = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    endereco = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'cpf', 'data_nascimento', 'endereco')
