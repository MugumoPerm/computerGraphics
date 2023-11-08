from django import forms

class AdditionForm(forms.Form):
    number1 = forms.IntegerField(label="Number 1")
    number2 = forms.IntegerField(label="Number 2")
    number3 = forms.IntegerField(label="Number 3")
    number4 = forms.IntegerField(label="Number 4")


    
