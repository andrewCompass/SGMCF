from django.http import JsonResponse
import random
from .models import Logs

def getTemperatura(request, id = None):

    if id == None:
        temperatura = random.randint(0, 35)
    else:
        temperatura = id

    status = 'ok'
    if temperatura < 20 or temperatura > 28:
        status = 'alerta'
        log = Logs(temperatura=temperatura, status=status)
        log.save()

        print('Temperatura fora do padrão, log salvo no banco de dados')

    context = {
        'temperatura': temperatura,
        'status': status,
    }

    return JsonResponse(context)
