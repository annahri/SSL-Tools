from django import forms

key_choices = [('2048', '2048-bit'), ('4096', '4096-bit')]

class CSRForm(forms.Form):
    common_name = forms.CharField(label='Common Name')
    country = forms.CharField(label='Country', max_length=2, help_text='Enter the Country Code.')
    state = forms.CharField(label='State')
    localty = forms.CharField(label='Localty', help_text="City.")
    organization = forms.CharField(label='Organization')
    organizational_unit = forms.CharField(label='Organizational Unit')
    key_size = forms.ChoiceField(choices=key_choices, widget=forms.RadioSelect)
