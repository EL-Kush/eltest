from dataclasses import fields
import imp
from django import forms
from minio_api.models import FileUpload

class Doucument(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = '__all__'