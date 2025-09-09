from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

# Create your views here.
def form(request):
    return render(request,"form.html")
    
def send(request):

    text = ''
    uploaded = request.FILES.get('file')

    if not text and not uploaded:
        return HttpResponseBadRequest('Data not send')

    
    if uploaded:
        for chunk in uploaded.chunks():
            text += chunk.decode('cp1252', errors='ignore')
    else:
        text = request.POST.get('text')

    return HttpResponse(text)

