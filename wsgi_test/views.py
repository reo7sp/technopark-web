import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    output = ['привет, мир']

    if request.method == 'GET':
        output.append('GET request')
        for k, v in request.GET.items():
            output.append('{} = {}'.format(k, v))

    if request.method == 'POST':
        output.append('POST request')
        for k, v in request.POST.items():
            output.append('{} = {}'.format(k, v))

    output.append('')
    return HttpResponse("\n".join(output), content_type='text/plain; charset=utf-8')
