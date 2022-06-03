from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomerSerializer, AddMechanicSerializer, TRManagerSerializer
from rest_framework.exceptions import AuthenticationFailed
from .models import User, Customer, Mechanic
import jwt, datetime

#customer registration
class CustomerSignupView(APIView):
    
    def post(self, request):
        serializer_class = CustomerSerializer(data = request.data)
        serializer_class.is_valid(raise_exception=True)
        # serializer_class.save()
        return Response(serializer_class.data)

#add_ mechanic
class AddMechanicView(APIView):
    def post(self, request):
        serializer_class = AddMechanicSerializer(data = request.data)
        serializer_class.is_valid(raise_exception=True)
        # serializer_class.save()
        return Response(serializer_class.data)

#add_ trmanager
class AddTRManagerView(APIView):
    def post(self, request):
        serializer_class = TRManagerSerializer(data = request.data)
        serializer_class.is_valid(raise_exception=True)
        # serializer_class.save()
        return Response(serializer_class.data)

#customer/mechanic login
class CustomerLoginView(APIView):
    def post(self, request):
        phoneno = request.data['phoneno']
        password = request.data['password']

        customer = Customer.objects.filter(phoneno = phoneno).first()

        if customer is None:
            raise AuthenticationFailed('User not found')

        if not customer.check_password(password):
            raise AuthenticationFailed('incorrect password')

        payload = {
            'id': customer.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response 

#get customer data
class CustomerView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated user')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated user')

        customer = Customer.objects.filter(id = payload['id']).first()

        return Response({
            "User": customer
        })

#customer/mechanic login
class MechanicLoginView(APIView):
    def post(self, request):
        phoneno = request.data['phoneno']
        password = request.data['password']

        mechanic = Mechanic.objects.filter(phoneno = phoneno).first()

        if mechanic is None:
            raise AuthenticationFailed('User not found')   

        if not mechanic.check_password(password):
            raise AuthenticationFailed('incorrect password') 

        payload = {
            'id': mechanic.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response  

#get mechanic data 
class MechanicView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated user')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated user')

        mechanic = Mechanic.objects.filter(id = payload['id']).first()

        return Response({
            "User": mechanic
        })           

#admin login
class AdminLoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username = username).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response 

#get admin data
class AdminView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated user')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated user')

        user = User.objects.filter(id = payload['id']).first()

        return Response({
            "User": user
        }) 

#signing out
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'logged out'
        }

        return response