from django.shortcuts import render
from django.http import HttpResponseBadRequest
from services import AI
from services import files

# Create your views here.
def form(request):
    return render(request,"form.html")
    
def send(request):

    text = ''
    uploaded = request.FILES.get('file')

    if not request.POST.get('text') and not uploaded:
        return HttpResponseBadRequest('Data not send')

    
    
    if uploaded:

        if uploaded.content_type != 'text/plain' and uploaded.content_type != 'application/pdf': 
            return HttpResponseBadRequest('Format not accepted')

        if uploaded.content_type == 'application/pdf':
            text = files.extract_text_from_pdf(uploaded)
        if uploaded.content_type == 'text/plain':
            text = files.extract_text_from_txt(uploaded)
        
    else:
        text = request.POST.get('text')

    prompt = 'Considerando um ambiente de trabalho, classifique de forma concisa o seguinte texto em: produtivo ou improdutivo. /n ' + text
    
    result = AI.get_response(prompt)
    context = { "result": result }

    return render(request,'result.html', context)

