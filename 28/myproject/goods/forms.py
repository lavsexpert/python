from django import forms


class AddToBasket(forms.Form):
    id = forms.IntegerField()
    count = forms.IntegerField()