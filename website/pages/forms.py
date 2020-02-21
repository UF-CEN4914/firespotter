from django import forms

class SigninForm(forms.Form):
    email = forms.CharField(
        max_length = 200,
        label = "Email",
        required = True,
        widget = forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "username@domain.com"
        })
    )
    password = forms.CharField(
        label = "Password",
        required = True,
        widget = forms.PasswordInput(attrs = {
            "class": "form-control"
        })
    )

class SignupForm(forms.Form):
    COUNTRY_CHOICES = (
        ("US", "United States"),
        ("BR", "Brazil")
    )
    DEFAULT_REGIONS = (
        ("California", "California"),
        ("Midwest", "Midwest")
    )
    org_name = forms.CharField(
        max_length = 200,
        label = "Name",
        required = True,
        widget = forms.TextInput(attrs= {
            "class": "form-control",
            "placeholder": "Company, LLC"
        })
    )
    org_email = forms.CharField(
        max_length = 200,
        label = "Email",
        required = True,
        widget = forms.TextInput(attrs = {
            "class": "form-control",
            "placeholder": "company@domain.com"
        })
    )
    org_phone_num = forms.CharField (
        max_length = 20,
        label = "Phone Number",
        widget = forms.TextInput(attrs = {
            "class": "form-control",
            "placeholder": "+12344567890"
        })
    )
    org_country = forms.ChoiceField (
        choices = COUNTRY_CHOICES,
        label = "Country",
        initial = "US", 
        required = True,
        widget = forms.Select(attrs = {
            "class": "form-control",
            "id": "countries"
        })
    )
    org_region = forms.ChoiceField (
        choices = DEFAULT_REGIONS,
        label = "Region",
        initial = "California",
        required = True,
        widget = forms.Select(attrs = {
            "class": "form-control",
            "id": "region"
        })
    )
    admin_first_name = forms.CharField(
        max_length = 200,
        label = "First Name",
        required = True,
        widget = forms.TextInput(attrs = {
            "class": "form-control",
            "placeholder": "Jane"
        })
    )
    admin_last_name = forms.CharField(
        max_length = 200,
        label = "Last Name",
        required = True,
        widget = forms.TextInput(attrs = {
            "class": "form-control",
            "placeholder": "Smith"
        })
    )
    admin_email = forms.CharField(
        max_length = 200,
        label = "Admin Email",
        required = True,
        widget = forms.TextInput(attrs = {
            "class": "form-control",
            "placeholder": "username@domain.com"
        })
    )
    admin_password = forms.CharField(
        label = "Password",
        required = True,
        widget = forms.PasswordInput(attrs = {
            "class": "form-control"
        })
    )
    admin_password_confirmation = forms.CharField(
        label = "Password Confirmation",
        required = True,
        widget = forms.PasswordInput(attrs = {
            "class": "form-control"
        })
    )