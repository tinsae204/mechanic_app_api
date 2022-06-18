from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer

@api_view(['GET'])
def getRequests(request):
    service_requests = ServiceRequest.objects.all()
    serializer = ServiceRequestSerializer(service_requests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRequest(request, pk):
    service_request = ServiceRequest.objects.get(id = pk)
    serializer = ServiceRequestSerializer(service_request, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createRequest(request):
    data = request.data
    service_request = ServiceRequest.objects.create(
        service_type = data['service_type'],
        char_info = data['char_info'],
        location= data['location']
    )

    serializer = ServiceRequestSerializer(service_request, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateRequest(request, pk):
    data = request.data
    service_request = ServiceRequest.objects.get(id = pk)

    serializer = ServiceRequestSerializer(service_request, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def discardRequest(request, pk):
    service_request = ServiceRequest.objects.get(id = pk)
    service_request.delete()

    return Response("Request Deleted")




