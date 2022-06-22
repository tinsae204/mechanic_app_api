from django.urls import path
from .views import make_rating, get_bad_rating_mechanic

urlpatterns = [
    path('make_rating/', make_rating),
    path('get_mechanic/', get_bad_rating_mechanic),
]