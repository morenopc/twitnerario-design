# -*- coding: UTF8 -*-

from django import forms
from django.forms import ModelForm
from form_utils.forms import BetterModelForm
from registros.models import Registros

class RegistrosForm(BetterModelForm):
    class Meta:
        model=Registros
        #exclude=['benef']
        widgets = {
            #'nome_pesq':forms.TextInput(attrs={'readonly': 'readonly'}),
            #'possui_perfil':forms.Select(attrs={'readonly': 'readonly'}),
            #'baixa_renda':forms.CheckboxInput(attrs={'style': 'display:none'}),
            #'benef': forms.HiddenInput(),
        }
        fieldsets=[
                   ('Registro', {
                   'fields': [
                              'twitter',
                              'ponto',
                              'linha',
                              'horas',
                              'minutos',
                              ],
                   'classes': ['registro']
                   })
                 ]
        row_attrs = {
        #'data': {'class':'data'},
        }
        
