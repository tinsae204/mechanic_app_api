from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from django.shortcuts import HttpResponse
import folium
import geocoder
import jwt
from accounts.models import Mechanic, Customer
from car_info.models import CarInfo
from service_type.models import ServiceType

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
    token = request.headers.get('jwt')

    payload = jwt.decode(jwt=token, key='secret', algorithms=['HS256'])
    customer = Customer.objects.filter(customer_id = payload['id']).first()
    service_type = ServiceType.objects.filter(id = 2).first()
    car_info = CarInfo.objects.filter(id = 1).first()

    service_request = ServiceRequest.objects.create(
        customer = customer,
        service_type = service_type,
        car_info = car_info,
        customer_lat= data['customer_lat'],
        customer_lon= data['customer_lon']
    )

    serializer = ServiceRequestSerializer(service_request, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def accept_request(request, pk):
    data = request.data
    token = request.headers.get('jwt')

    payload = jwt.decode(jwt=token, key='secret', algorithms=['HS256'])
    mechanic = Mechanic.objects.filter(mechanic_id = payload['id']).first()

    service_request = ServiceRequest.objects.filter(id = pk).first()
    service_request.mechanic = mechanic
    service_request.mechanic_lat = data['mechanic_lat']
    service_request.mechanic_lon = data['mechanic_lon']
    service_request.is_accepted = True

    service_request.save()

    serializer = ServiceRequestSerializer(service_request, data = request.data)
    if serializer.is_valid():
        serializer.save()

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
    service_request.is_canceled = True

    return Response("Request Discarded")

@api_view(['GET'])
def show_location(request):

    # location = geocoder.osm(data['location'])
    m_latitude = request.data['mechanic_lat']
    m_longitude = request.data['mechanic_lon']

    c_latitude = request.data['customer_lat']
    c_longitude = request.data['customer_lon']
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

