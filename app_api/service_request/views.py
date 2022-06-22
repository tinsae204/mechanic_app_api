from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from django.shortcuts import HttpResponse
import folium
import geocoder
from accounts.models import Mechanic, Customer

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
    # if serializer.is_valid():
    #     serializer.save()
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

#successful requests
@api_view(['GET'])
def successful_requests(request):
    requests = ServiceRequest.objects.filter(status = True)
    count = requests.count()
    return HttpResponse(count)

#un_successful requests
@api_view(['GET'])
def un_successful_requests(request):
    requests = ServiceRequest.objects.filter(is_canceled = True)
    count = requests.count()
    return HttpResponse(count)

#pending requests
@api_view(['GET'])
def pending_requests(request):
    requests = ServiceRequest.objects.filter(status = False)
    count = requests.count()
    return HttpResponse(count)

#count requests
@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def count_requests(request):
    requests = ServiceRequest.objects.all()
    count = requests.count()
    return HttpResponse(count)

#count customer
@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def count_customer(request):
    customers = Customer.objects.all()
    count = customers.count()
    return HttpResponse(count)

#count mechanic
@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def count_mechanic(request):
    mechanics = Mechanic.objects.all()
    count = mechanics.count()
    return Response(count)

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

