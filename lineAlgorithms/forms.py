from django import forms

class AdditionForm(forms.Form):
    number1 = forms.IntegerField(label="X1")
    number2 = forms.IntegerField(label="X2")
    number3 = forms.IntegerField(label="Y1")
    number4 = forms.IntegerField(label="Y2")


    
