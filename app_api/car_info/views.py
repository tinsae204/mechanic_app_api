from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CarInfoSerializer
from .models import CarInfo

class CarInfoViews(APIView):
    def post(self, request):
        serializer_class = CarInfoSerializer(data = request.data)
        serializer_class.is_valid(raise_exception=True)
        # serializer_class.save()
        return Response(serializer_class.data)

    def get(self, request):

        car_info = [car.maker for car in CarInfo.objects.all()]
        return Response({
            "car_info": car_info
        })