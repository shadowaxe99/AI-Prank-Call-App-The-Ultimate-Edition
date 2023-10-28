
from django.shortcuts import render
from django.http import JsonResponse

from .models import PrankCall

def prank_call(request):
    if request.method == 'POST':
        # Get the phone number and prank message from the request
        phone_number = request.POST.get('phone_number')
        prank_message = request.POST.get('prank_message')

        # Create a new PrankCall object
        prank_call = PrankCall(phone_number=phone_number, prank_message=prank_message)
        prank_call.save()

        # Perform the prank call using the Eleven Labs API
        # (code for making the API call goes here)

        # Return a JSON response with the result of the prank call
        return JsonResponse({'status': 'success', 'message': 'Prank call successful'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

