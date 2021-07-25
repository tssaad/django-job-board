from django import forms
from django.forms import fields, models

from .models import Applicatiion, Job

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Applicatiion
        fields = ['APPName','APPEmail','APPurl','APPCV','APPCOver_letter']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['JOBSlug', 'JOBowner']
