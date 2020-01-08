from django import forms

class CameraForm(forms.Form):
    ip_address = forms.CharField(
        max_length = 200,
        label = "IP Address",
        required = True,
        widget = forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "216.3.128.12"
        })
    )
    refresh_rate = forms.IntegerField(
        required = True,
        label = "Refresh Rate in Minutes",
        widget = forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "1"
        })
    )
    username = forms.CharField(
        max_length = 200,
        label = "Camera Username",
        required = False,
        widget = forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Optional"
        })
    )
    short_name = forms.CharField(
        max_length = 200,
        label = "Short Name",
        required = False,
        widget = forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Camera 1"
        })
    )
    password = forms.CharField(
        label = "Password",
        required = False,
        widget = forms.PasswordInput(attrs = {
            "class": "form-control",
            "placeholder": "Optional"
        })
    )
    password_confirmation = forms.CharField(
        label = "Password Confirmation",
        required = False,
        widget = forms.PasswordInput(attrs = {
            "class": "form-control",
            "placeholder": "Optional"
        })
    )