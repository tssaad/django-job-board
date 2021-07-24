from django import forms
from django.forms import fields, models

from .models import Applicatiion

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Applicatiion
        fields = ['APPName','APPEmail','APPurl','APPCV','APPCOver_letter']