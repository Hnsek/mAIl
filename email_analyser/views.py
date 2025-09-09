from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
import requests
from services import AI

# Create your views here.
def form(request):
    return render(request,"form.html")
    
def send(request):

    text = ''
    uploaded = request.FILES.get('file')

    if not request.POST.get('text') and not uploaded:
        return HttpResponseBadRequest('Data not send')

    
    if uploaded:
        raw = uploaded.read()
        try:
            text = raw.decode('utf-8')
        except UnicodeDecodeError:
            text = raw.decode('latin-1', errors='ignore')
    else:
        text = request.POST.get('text')

    prompt = 'Considerando um ambiente de trabalho, classifique de forma concisa o seguinte texto em: produtivo ou improdutivo. /n ' + text
    
    response = AI.get_response(prompt)
    
    return HttpResponse(response)

