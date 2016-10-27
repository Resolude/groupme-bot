from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from scoot.message_handler import receive

import json


# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        receive(body)

    return HttpResponse()
