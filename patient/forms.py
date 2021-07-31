from django.forms import ModelForm
from .models import Benhnhan

class BenhnhanForm(ModelForm):
    class Meta:
        model =Benhnhan
        fields = '__all__'
