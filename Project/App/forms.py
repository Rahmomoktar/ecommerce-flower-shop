from django import forms
from .models import Contact_Us,Booking

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))



    # class CreateUserForm



class ContactUsForm(forms.ModelForm):
        class Meta:
            model = Contact_Us
            fields = ['Name', 'Email', 'Message']
            widgets = {
                'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}), 
                'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                'Message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
            }


# Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'Quentity_Od','date','time']



# order


from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'product_name', 'quantity']











# class loginform(forms.Form):
#     username = forms.CharField(max_length=55)
#     password = forms.CharField(widget=forms.PasswordInput)
