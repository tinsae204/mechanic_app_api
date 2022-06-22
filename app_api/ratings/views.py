from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Rating
from .serializers import RatingSerializer
import jwt
from accounts.models import Mechanic


@api_view(['POST'])
def make_rating(request):
    token = request.COOKIES.get('jwt')
    payload = jwt.decode(jwt=token, key='secret', algorithms=['HS256'])
    mechanic_ = Mechanic.objects.filter(mechanic_id = payload['id']).first()

    data = request.data
    if(data['rating'] > 0):
        rating = Rating.objects.create(
            mechanic = mechanic_.mechanic_id,
            rating = data['rating'],
            is_submitted = True
        )

    serializer = RatingSerializer(rating, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_bad_rating_mechanic(request):
    ratings = Rating.objects.all()
    for rate in ratings:
        if(rate.rating < 3):
            mechanics = Mechanic.objects.filter(mechanic_id = rate.mechanic)
   
    return Response(mechanics)
