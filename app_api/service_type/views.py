# from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ServiceTypeSerializer
from .models import ServiceType
from rest_framework.decorators import api_view

@api_view(['GET'])
def getServices(request):
    services = ServiceType.objects.all()
    serializer = ServiceTypeSerializer(services, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getService(request, pk):
    service = ServiceType.objects.get(id = pk)
    serializer = ServiceTypeSerializer(service, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addService(request):
    data = request.data
    service = ServiceType.objects.create(
        name = data['name'],
        min_price = data['min_price'],
        max_price= data['max_price']
    )

    serializer = ServiceTypeSerializer(service, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateService(request, pk):
    data = request.data
    service = ServiceType.objects.get(id = pk)

    serializer = ServiceTypeSerializer(service, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteService(request, pk):
    service = ServiceType.objects.get(id = pk)

    service.delete()

    return Response("Service Deleted")

# class ServiceTypeViews(APIView):
#     def post(self, request):
#         serializer_class = ServiceTypeSerializer(data = request.data)
#         serializer_class.is_valid(raise_exception=True)
#         # serializer_class.save()
#         return Response(serializer_class.data)

#     def get(self, request):

#         service_type = ServiceType.objects.all()
#         serializer = ServiceTypeSerializer(service_type, many=True)
#         return Response(serializer.data)