from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ScheduledServiceRequest
from .serializers import ScheduledServiceRequestSerializer

@api_view(['GET'])
def getRequests(request):
    service_requests = ScheduledServiceRequest.objects.all()
    serializer = ScheduledServiceRequestSerializer(service_requests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRequest(request, pk):
    service_request = ScheduledServiceRequest.objects.get(id = pk)
    serializer = ScheduledServiceRequestSerializer(service_request, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createRequest(request):
    data = request.data
    service_request = ScheduledServiceRequest.objects.create(
        service_type = data['service_type'],
        char_info = data['char_info'],
        location= data['location'],
        scheduled_date = data['scheduled_date']
    )

    serializer = ScheduledServiceRequestSerializer(service_request, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateRequest(request, pk):
    data = request.data
    service_request = ScheduledServiceRequest.objects.get(id = pk)

    serializer = ScheduledServiceRequestSerializer(service_request, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def discardRequest(request, pk):
    service_request = ScheduledServiceRequest.objects.get(id = pk)
    service_request.delete()

    return Response("Request Deleted")



