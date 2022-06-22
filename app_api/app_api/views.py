from django.http import JsonResponse
from fcm_django.models import FCMDevice
from accounts.models import Mechanic


def notify(request):
    # devices = FCMDevice.objects.filter(mechanic)
    mechanics = Mechanic.objects.all()
    for mechanic in mechanics:
        mechanic.send_message(title="New Request", body="service has been requested", data={"test": "test"})
        break

    return JsonResponse({"status": "ok"})