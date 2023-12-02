from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError

from .models import PrankCall
from .api_helpers import make_eleven_labs_prank_call

@require_http_methods(["POST"])
def prank_call(request):
    try:
        phone_number = request.POST.get('phone_number')
        prank_message = request.POST.get('prank_message')
        if not phone_number or not prank_message:
            raise ValidationError('Missing phone number or prank message')
        prank_call = PrankCall(
            caller_number=phone_number,
            prank_message=prank_message
        )
        prank_call.save()
        # Make the API call to Eleven Labs
        response = make_eleven_labs_prank_call(phone_number, prank_message)
        if response.status_code == 200:
            prank_call.status = 'success'
        else:
            prank_call.status = 'failed'
        prank_call.save()
        return JsonResponse({
            'status': prank_call.status,
            'message': 'Prank call made successfully' if prank_call.status == 'success' else 'Prank call failed'
        })
    except ValidationError as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': 'An error occurred while making the prank call'}, status=500)