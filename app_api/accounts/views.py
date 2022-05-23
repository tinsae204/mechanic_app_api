from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse


def aPage(req):
    return JsonResponse({
        "username": "user1",
        "password": "password1"
    })