from django import  forms


class RegistrationForm(forms.Form):
    Nama_UKM = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={'class':'form-control',
                                                             'placeholder':'Name UKM'}))
    Username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Username'}))
    Password = forms.CharField(max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Password'}))
    Email = forms.CharField(max_length=50,
                            widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Email'}))
    No_HP = forms.CharField(max_length=20,
                            widget=forms.NumberInput(attrs={'class': 'form-control',
                                                            'placeholder': 'No Hp'}))
    Alamat = forms.CharField(max_length=100,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Alamat'}))


