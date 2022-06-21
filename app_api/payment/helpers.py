import requests
import random
from django.conf import settings

def send_otp_to_phone(phone_no1, phone_no2):
    try:
        otp = random.randint(1000, 9999)
        url1 = f'https://2factor.in/API/V1/293832-67745-11e5-88de-5600000c6b13/SMS/{phone_no1}/{otp}'
        url2 = f'https://2factor.in/API/V1/293832-67745-11e5-88de-5600000c6b13/SMS/{phone_no2}/{otp}'

        res1 = requests.get(url1)
        res2 = requests.get(url2)

        return otp

    except Exception as e:
        return None
