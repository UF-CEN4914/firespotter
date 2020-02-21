from django import forms

class UserForm(forms.Form):
    YES_NO = (
        (0, "No"),
        (1, "Yes")
    )
    first_name = forms.CharField(
        max_length = 200,
        label = "First Name",
        required = True,
        widget = forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Jane"
        })
    )
    last_name = forms.CharField(
        max_length = 200,
        label = "Last Name",
        required = True,
        widget = forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Smith"
        })
    )
    email = forms.CharField(
        max_length = 200,
        label = "Email",
        required = True,
        widget = forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "username@domain.com",
            "autocomplete": "email"
        })
    )
    password = forms.CharField(
        label = "Password",
        required = True,
        widget = forms.PasswordInput(attrs = {
            "class": "form-control",
            "autocomplete": "new-password"
        })
    )
    password_confirmation = forms.CharField(
        label = "Password Confirmation",
        required = True,
        widget = forms.PasswordInput(attrs = {
            "class": "form-control",
            "autocomplete": "new-password"
        })
    )
    admin_select = forms.ChoiceField (
    choices = YES_NO,
    label = "Is Admin",
    initial = "No",
    required = True,
        widget = forms.Select(attrs = {
            "class": "form-control",
            "id": "admin-select"
        })
    )