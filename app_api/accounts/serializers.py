from rest_framework import serializers
from .models import Mechanic, Customer


class CustomerSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    phoneno = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super(CustomerSerializer, self).get_cleaned_data()
        extra_data = {
            'phoneno': self.validated_data.get('phoneno','')
        }

        data.update(extra_data)
        return data

    def save(self, request):
        user = super(CustomerSerializer, self).save(request)
        user.is_customer = True
        user.save()
        customer = Customer(customer = user, phoneno = self.cleaned_data.get('phoneno'))
        customer.save()
        return user


class AddMechanicSerializer(serializers.ModelSerializer):
    mechanic = serializers.PrimaryKeyRelatedField(read_only=True)
    phoneno = serializers.CharField(required=True)
    specialization = serializers.CharField(required=True)
    education = serializers.CharField(required=True)
    docs = serializers.FileField(required=True)
    pic = serializers.FileField(required=True)

    def get_cleaned_data(self):
        data = super(AddMechanicSerializer, self).get_cleaned_data()
        extra_data = {
            'phoneno': self.validated_data.get('phoneno', ''),
            'specialization': self.validated_data.get('specialization', ''),
            'education': self.validated_data.get('education', ''),
            'docs': self.validated_data.get('docs', ''),
            'pic': self.validated_data.get('pic', '')
        }

        data.update(extra_data)
        return data

    def save(self, request):
        user = super(AddMechanicSerializer, self).save(request)
        user.is_mechanic = True
        user.save()
        mechanic = Mechanic(mechanic = user, phoneno = self.cleaned_data.get('phoneno'), specialization = self.cleaned_data.get('specialization'), education = self.cleaned_data.get('education'), docs = self.cleaned_data.get('docs'), pic = self.cleaned_data.get('pic'))

        mechanic.save()
        return user


class AdminSerializer(serializers.ModelSerializer):
    customadmin = serializers.PrimaryKeyRelatedField(read_only=True)

    def get_cleaned_data(self):
        data = super(AdminSerializer, self).get_cleaned_data()  
        return data

    def save(self, request):
        user = super(AdminSerializer, self).save(request)
        user.is_admin = True
        user.save()
        return user


class TRManagerSerializer(serializers.ModelSerializer):
    trmanager = serializers.PrimaryKeyRelatedField(read_only=True)

    def get_cleaned_data(self):
        data = super(TRManagerSerializer, self).get_cleaned_data()  
        return data

    def save(self, request):
        user = super(TRManagerSerializer, self).save(request)
        user.is_trmanager = True
        user.save()
        return user        