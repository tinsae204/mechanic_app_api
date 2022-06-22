from rest_framework.views import APIView
from rest_framework.response import Response
from urllib3 import HTTPResponse
from .serializers import CustomerSerializer, AddMechanicSerializer, TRManagerSerializer
from rest_framework.exceptions import AuthenticationFailed
from .models import TRmanager, User, Customer, Mechanic
import jwt, datetime
from rest_framework.decorators import api_view
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import HttpResponse
from pusher_push_notifications import PushNotifications
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet


#customer signup
@api_view(['POST'])
def customer_signup(request):
    data = request.data
    user = User.objects.create(
        first_name = data['first_name'],
        last_name = data['last_name'],
        username = data['username'],
        password = data['password'],
        is_customer = True
    )
    customer = Customer.objects.create(
        customer_id = user.id,
        phoneno = data['phoneno']
    )
    serializer = CustomerSerializer(customer, user)
    serializer.is_valid(raise_exception=True)
    return Response("user saved")

#add_ mechanic
@api_view(['POST'])
def add_mechanic(request):
    data = request.data
    user = User.objects.create(
        first_name = data['first_name'],
        last_name = data['last_name'],
        username = user.first_name,
        is_mechanic = True,
    )

    mechanic = Mechanic.objects.create(
        mechanic_id = user.id,
        phoneno = data['phoneno'],
        specialization = data['specialization'],
        education = data['education'],
        docs = data['docs'],
        pic = data['pic'],
        is_mechanic = True,
    )
    serializer = AddMechanicSerializer(user, mechanic)
    serializer.is_valid(raise_exception=True)
    return Response("user saved")

#add_ trmanager
@api_view(['POST'])
def add_trmanager(request):
    data = request.data
    user = User.objects.create(
        username = data['username'],
        password = data['password'],
        is_trmanager = True,
    )
    tr_manager = TRmanager.objects.create(
        tr_manager_id = user.id
    )

    serializer = TRManagerSerializer(user, tr_manager)
    serializer.is_valid(raise_exception=True)
    return Response("user saved")

#customer login
@api_view(['POST'])
def customer_login(request):
    data = request.data
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

#get authorized customer data
@api_view(['GET'])
def get_auth_customer(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated user')

    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated user')

    customer = Customer.objects.filter(id = payload['id']).first()
    user = User.objects.get(id = customer.customer_id)

    return Response({
        "Customer": customer,
        "User": user
    })

#mechanic_login
@api_view(['POST'])
def mechanic_login(request):
    data = request.data
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

#get authorized mechanic data
@api_view(['GET'])
def get_auth_mechanic(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated user')

    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated user')

    mechanic = Mechanic.objects.filter(id = payload['id']).first()
    user = User.objects.get(id = mechanic.mechanic_id)

    return Response({
         "Mechanic": mechanic,
         "User": user
    })

#admin login
@api_view(['POST'])
def admin_login(request):
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

#getting authorized admins data
@api_view(['GET'])
def get_auth_admin(request):
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

#logout
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'logged out'
    }

    return response   



#notify_mechanic
def notify(request):
    pass










# #signing out
# class LogoutView(APIView):
#     def post(self, request):
#         response = Response()
#         response.delete_cookie('jwt')
#         response.data = {
#             'message': 'logged out'
#         }

#         return response


#customer registration
# class CustomerSignupView(APIView):   
#     def post(self, request):
#         serializer_class = CustomerSerializer(data = request.data)
#         serializer_class.is_valid(raise_exception=True)
#         # serializer_class.save()
#         return Response(serializer_class.data)

#add_ mechanic
# class AddMechanicView(APIView):
#     def post(self, request):
#         serializer_class = AddMechanicSerializer(data = request.data)
#         serializer_class.is_valid(raise_exception=True)
#         # serializer_class.save()
#         return Response(serializer_class.data)

#add_ trmanager
# class AddTRManagerView(APIView):
#     def post(self, request):
#         serializer_class = TRManagerSerializer(data = request.data)
#         serializer_class.is_valid(raise_exception=True)
#         # serializer_class.save()
#         return Response(serializer_class.data)

#customer/mechanic login
# class CustomerLoginView(APIView):
#     def post(self, request):
#         phoneno = request.data['phoneno']
#         password = request.data['password']

#         customer = Customer.objects.filter(phoneno = phoneno).first()

#         if customer is None:
#             raise AuthenticationFailed('User not found')

#         if not customer.check_password(password):
#             raise AuthenticationFailed('incorrect password')

#         payload = {
#             'id': customer.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow()
#         }

#         token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

#         response = Response()
#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             'jwt': token
#         }

#         return response

#get customer data
# class CustomerView(APIView):
#     def get(self, request):
#         token = request.COOKIES.get('jwt')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated user')

#         try:
#             payload = jwt.decode(token, 'secret', algorithm=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated user')

#         customer = Customer.objects.filter(id = payload['id']).first()

#         return Response({
#             "User": customer
#         })

#mechanic login
# class MechanicLoginView(APIView):
#     def post(self, request):
#         phoneno = request.data['phoneno']
#         password = request.data['password']

#         mechanic = Mechanic.objects.filter(phoneno = phoneno).first()

#         if mechanic is None:
#             raise AuthenticationFailed('User not found')   

#         if not mechanic.check_password(password):
#             raise AuthenticationFailed('incorrect password') 

#         payload = {
#             'id': mechanic.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow()
#         }

#         token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

#         response = Response()
#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             'jwt': token
#         }

#         return response 

#get mechanic data 
# class MechanicView(APIView):
#     def get(self, request):
#         token = request.COOKIES.get('jwt')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated user')

#         try:
#             payload = jwt.decode(token, 'secret', algorithm=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated user')

#         mechanic = Mechanic.objects.filter(id = payload['id']).first()

#         return Response({
#             "User": mechanic
#         })

#admin login
# class AdminLoginView(APIView):
#     def post(self, request):
#         username = request.data['username']
#         password = request.data['password']

#         user = User.objects.filter(username = username).first()

#         if user is None:
#             raise AuthenticationFailed('User not found')

#         if not user.check_password(password):
#             raise AuthenticationFailed('incorrect password')

#         payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow()
#         }

#         token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

#         response = Response()
#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             'jwt': token
#         }

#         return response 


#get admin data
# class AdminView(APIView):
#     def get(self, request):
#         token = request.COOKIES.get('jwt')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated user')

#         try:
#             payload = jwt.decode(token, 'secret', algorithm=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated user')

#         user = User.objects.filter(id = payload['id']).first()

#         return Response({
#             "User": user
#         }) 