from django import forms

class AddNewRequest(forms.Form):
    full_name = forms.CharField(label="Full Name", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    University_id = forms.CharField(label="University ID", max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    academic_year = forms.ChoiceField(
        choices=[(1,'First Year'), (2,'Second Year'), (3,'Third Year'), (4,'Fourth Year')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    phone = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telegram_user = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}))
    current_section = forms.IntegerField(min_value=1,widget=forms.NumberInput(attrs={'class': 'form-control'}))
    target_section = forms.IntegerField(min_value=1,widget=forms.NumberInput(attrs={'class': 'form-control'}))

       