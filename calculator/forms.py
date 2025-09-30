from django import forms

class InputForm(forms.Form):
    a = forms.FloatField(label='Value A')
    b = forms.FloatField(label='Value B')
    c = forms.FloatField(label='Value C')
