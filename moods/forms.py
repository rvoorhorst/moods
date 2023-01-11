from django import forms


class CityNameForm(forms.Form):
    user_location = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "A CITY NEAR ME ", "class": "textinput"}
        ),
    )
