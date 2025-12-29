from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .services import chatbot_response

@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message")

        response = chatbot_response(message)

        return JsonResponse({
            "response": response
        })
