# app/api_helpers.py

import requests
from django.conf import settings

def make_eleven_labs_prank_call(phone_number, prank_message):
    """
    This function makes a prank call using the Eleven Labs API.
    It takes in a phone number and a prank message as parameters.
    It returns the response from the API call.
    """
    response = requests.post(
        'https://api.elevenlabs.io/makeCall',
        data={
            'phone_number': phone_number,
            'prank_message': prank_message
        },
        headers={'Authorization': f'Bearer {settings.ELEVEN_LABS_API_KEY}'}
    )
    return response