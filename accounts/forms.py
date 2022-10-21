from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# from validate_email import validate_email
from django.contrib import messages
from .models import Signup
from django.contrib.auth.forms import UserCreationForm
# class SignupForm(UserCreationForm):
class SignupForm(forms.ModelForm):
    password = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    address = forms.CharField(required=True)

    def clean(self):

            cleaned_data = super().clean()

            email= cleaned_data.get("email")
            phone_number= cleaned_data.get("phone_number")
            password = cleaned_data.get("password")
            password2 = cleaned_data.get("password2")

            usr= User.objects.filter(email=email)
            if usr:
                print("<!!!!!!!!!!!!!!!!!!!>")
                raise ValidationError(
                    "email already exist"
                )
            if password != password2:
                raise ValidationError(
                    "password incorrect"
                )

            if not phone_number.isdigit():
                print("***********")
                error_messages = {
                    'required': "Please Enter your valid phone number"
                }
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

# class SignupForm(forms.Form):
#
#     # phone_number=forms.CharField(required=True)
#     # address=forms.CharField(required=True)
#     # first_name=forms.CharField(required=True)
#     # last_name=forms.CharField(required=True)
#     # email=forms.EmailField(required=True)
#     # password=forms.IntegerField(required=True)
#     # password2=forms.IntegerField(required=True)
#     # username=forms.CharField(required=True)
#     class Meta:
#         model = Signup
#         fields=['phone_number']
#         # exclude = ('last_login')
#
#
#
#     def clean(self):
#         cleaned_data = super().clean()
#
#         email= cleaned_data.get("email")
#         phone_number= cleaned_data.get("phone_number")
#         password=cleaned_data.get("password")
#         password2= cleaned_data.get('password2')
#
#
#         if password != password2:
#             print("#######")
#             raise  ValidationError(
#                     "password incorrect"
#                 )
#         usr= User.objects.filter(email=email).first()
#         if usr:
#             print("<!!!!!!!!!!!!!!!!!!!>")
#             raise ValidationError(
#                 "user already exist"
#             )
#         if not phone_number.isdigit():
#             print("***********")
#             error_messages = {
#                 'required': "Please Enter your valid phone number"
#             }




        # if email and phone_number and password:
        #
        #     # if not phone_number.is_valid_number():
        #     #     raise forms.ValidationError("Number not in this format")
        #     #     return phone_number
        #     if User.objects.filter(email=email).exists():
        #             raise forms.ValidationError("Invalid email")
        #             messages.warning(request, 'email already exists.')
        #     if not phone_number.isdigit():
        #         error_messages = {
        #             'required': "Please Enter your valid phone number"
        #         }
        #     if password!=password2:
        #         raise  ValidationError(
        #                     "password incorrect"
        #                 )




