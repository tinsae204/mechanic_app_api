from rest_framework.response import Response
from .serializers import CarInfoSerializer
from .models import CarInfo
from rest_framework.decorators import api_view


@api_view(['GET'])
def getCarInfos(request):
    cars = CarInfo.objects.all()
    serializer = CarInfoSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCarInfo(request, pk):
    car = CarInfo.objects.get(id = pk)
    serializer = CarInfoSerializer(car, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addCarInfo(request):
    data = request.data
    car = CarInfo.objects.create(
        maker = data['maker'],
        model = data['model'],
        year= data['year']
    )

    serializer = CarInfoSerializer(car, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateCarInfo(request, pk):
    data = request.data
    car = CarInfo.objects.get(id = pk)

    serializer = CarInfoSerializer(car, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteCarInfo(request, pk):
    car = CarInfo.objects.get(id = pk)
    car.delete()
    return Response("Car Deleted")


# class CarInfoViews(APIView):
#     def post(self, request):
#         serializer_class = CarInfoSerializer(data = request.data)
#         serializer_class.is_valid(raise_exception=True)
#         # serializer_class.save()
#         return Response(serializer_class.data)

#     def get(self, request):

#         car_info = [car.maker for car in CarInfo.objects.all()]
#         return Response({
#             "car_info": car_info
#         })
