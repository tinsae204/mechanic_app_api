from rest_framework import serializers
from .models import CustomAdmin, Mechanic, Customer, TRmanager


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    first_name = serializers.CharField(required=True)
    # last_name = serializers.CharField(required=False)
    # username = serializers.CharField()
    password = serializers.CharField(required=True)
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
        user.save()
        customer = Customer(customer = user, phoneno = self.cleaned_data.get('phoneno'))
        customer.save()
        return user


class AddMechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = '__all__'

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
        user.save()
        mechanic = Mechanic(mechanic = user, phoneno = self.cleaned_data.get('phoneno'), specialization = self.cleaned_data.get('specialization'), education = self.cleaned_data.get('education'), docs = self.cleaned_data.get('docs'), pic = self.cleaned_data.get('pic'))
        mechanic.save()
        return user


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAdmin
        fields = '__all__'

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

    class Meta:
        model = TRmanager
        fields = '__all__'

    trmanager = serializers.PrimaryKeyRelatedField(read_only=True)

    def get_cleaned_data(self):
        data = super(TRManagerSerializer, self).get_cleaned_data()  
        return data

    def save(self, request):
        user = super(TRManagerSerializer, self).save(request)
        user.save()
        return user        