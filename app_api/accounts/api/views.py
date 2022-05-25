from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, CustomerSignUpSerializer

class CustomerSignUpView(generics.GenericAPIView):
    serializer_class = CustomerSignUpSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context = self.get_serializer_context()).data,
            # "token": Token.object.get(user = user).key,
            "message": "customer account created"
        })