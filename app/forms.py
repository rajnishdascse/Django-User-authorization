from .models import User
from django.contrib.auth.forms import UserCreationForm
# from ckeditor.fields import RichTextField
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
