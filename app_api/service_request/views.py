from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from django.shortcuts import HttpResponse
import folium
import geocoder

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
    service = None
    service_request = ServiceRequest.objects.create(
        service_type = data['service_type'],
        char_info = data['char_info'],
        location= data['location']
    )

    serializer = ServiceRequestSerializer(service_request, many=False)

    # notify(data['service_type'])

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

@api_view(['GET'])
def show_location(request):

    # location = geocoder.osm(data['location'])
    m_latitude = request.data['m_latitude']
    m_longitude = request.data['m_longitude']

    c_latitude = request.data['c_latitude']
    c_longitude = request.data['c_longitude']
    #create map
    map_object = folium.Map(location=[19, -12], zoom_start=2)
    folium.Marker([m_latitude, m_longitude]).add_to(map_object)
    folium.Marker([c_latitude, c_longitude]).add_to(map_object)
    map_object = map_object._repr_html_()
    context={
        'map object': map_object
    }
    return HttpResponse(context)

# def notify(service_type):
#     pn_client = PushNotifications(
#         instance_id= '',
#         secret_key=''
#     )

#     response = pn_client.publish(
#         interests=['hello'],
#         publish_body={'apns': {'aps': {'alert': 'New service request!!!'}},
#                       'fcm': {'notification': {'title': 'Request','body': str(service_type + ' has been requested.')}}}
#     )

#     return Response({'Response': response})

