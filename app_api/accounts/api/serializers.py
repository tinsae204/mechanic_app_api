from rest_framework import serializers
from accounts.models import User, Mechanic, Customer, CustomAdmin, TAmanager


class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['username','is_admin', 'is_trmanager', 'is_customer', 'is_mechanic']


class CustomerSignUpSerializer(serializers.ModelSerializer):

    username = serializers.CharField(style={'input_type': 'text'}, write_only=True)
    fullname = serializers.CharField(style={'input_type': 'text'}, write_only=True)
    phoneno = serializers.CharField(style={'input_type': 'text'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['username','fullname', 'phoneno', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username = self.validated_data['username']
        )
        fullname = self.validated_data['fullname']
        phoneno = self.validated_data['phoneno']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'error': 'password do not match!!!'})
        user.set_password(password)    
        user.is_customer = True    
        user.save()
        Customer.objects.create(user = user)
        return user
