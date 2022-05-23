from django.urls import path
from .views import aPage

urlpatterns = [
    path('', aPage)
    # path('signUp/', ),
    # path('login/'),
    # path('login_/'),
    # path('addMech/'),
    # path('addTM/')
]