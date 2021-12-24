from typing import ClassVar
from django import forms
from .models import *
from django.db.models import fields
from django.forms.widgets import Widget
from django.shortcuts import render

class CodeForm(forms.ModelForm):
    class Meta:
        model= Code
        fields="__all__"

    number=forms.CharField(
        widget=forms.TextInput(

        )
    )


    #  name = forms.CharField(
    #     widget = forms.TextInput(
    #         attrs={
    #             'class' : 'form-control',
    #             'placeholder' : 'enter name of the product'
    #         }
    #     )
    # )