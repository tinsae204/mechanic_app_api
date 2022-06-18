from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/service_request/(?P<room_name>\w+)/$', consumers.ServiceRequestConsumer.as_asgi())
]
