from django import forms
from myfile.models import Uploads
class UploadsForms(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = '__all__'