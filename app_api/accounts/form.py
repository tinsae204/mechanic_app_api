from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from app_api.accounts.models import Mechanic, Customer, TRmanager, CustomAdmin, User


# mechanic and customer login form

class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField(required=True)
    phone_no = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.username = self.cleaned_data.get('username')
        user.password = self.cleaned_data.get('password')
        user.save()
        customer = Customer.objects.create(user = user)
        customer.phoneno = self.cleaned_data.get('phoneno')
        return user

# class 
        



# Customer auth
# class CustomerSignUpForm(UserCreationForm):
#     fullname = forms.CharField(required=True)
#     phoneno = forms.CharField(required=True)
#     username = forms.CharField(required=True)
#     password1 = forms.Field(required=True)
#     password2 =  forms.Field(required=True)

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ('fullname','phoneno', 'username', 'password1', 'password2')




# mechanic auth
# class AddMechanicForm(UserCreationForm): 
#     firstname = forms.CharField(required=True)
#     lastname = forms.CharField(required=True)
#     phoneno = forms.CharField(required=True)
#     specialization = forms.CharField(required=True)
#     education = forms.CharField(required=True)
#     docs = forms.FileField(required=True)

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ('firstname', 'lastname', 'phoneno','specialization', 'education', 'docs', 'is_mechanic')
    
#     @transaction.atomic
#     def data_save(self):
#         user = super().save(commit=False)
#         user.is_mechanic = True
#         user.save()
#         mechanic = Mechanic.objects.create(user = user)
#         mechanic.firstname = self.cleaned_data.get('firstname')
#         mechanic.lastname = self.cleaned_data.get('lastname')
#         mechanic.phoneno = self.cleaned_data.get('phoneno')
#         mechanic.specialization = self.cleaned_data.get('specialization')
#         mechanic.education = self.cleaned_data.get('education')
#         mechanic.docs = self.cleaned_data.get('docs')
#         mechanic.save()
#         return user

# class CreateMechanicAccountForm(UserCreationForm):
#     username = forms.CharField(required=True)
#     password1 = forms.CharField(required=True)
#     password2 = forms.CharField(required=True)

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ('username', 'password1', 'password2', 'is_mechanic')
    
#     @transaction.atomic
#     def data_save(self):
#         user = super().save(commit=False)
#         user.is_mechanic = True
#         user.username = self.cleaned_data.get('username')
#         user.password = self.cleaned_data.get('password')
#         user.save()
#         return user


    

