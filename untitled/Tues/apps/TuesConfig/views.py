from django.shortcuts import render
from django.http import *
from .models import *
from django.views.generic import TemplateView

def load_index(request):
    q = Test.objects.get(id=2)
    q1 = Test.objects.get(id=1)
    return HttpResponse(""+ q.Message +"    "+ q1.Message)

class IndexView(TemplateView):
    template_name = "Submit.html"

def post_data(request):
    if request.method == 'POST':
        print(request.POST.get("Keyword", "Message") )
        q = Test.objects.create()
        q.Keyword=request.POST.get("Keyword", "null")
        q.Message=request.POST.get("Message", "null")
        q.save()
    return HttpResponse("ok")



# Create your views here.
