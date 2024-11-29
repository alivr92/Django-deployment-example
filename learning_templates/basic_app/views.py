from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("hello Ali")
    return render(request, 'basic_app/index.html', {'text': 'Hello world!', 'number': 100})

def base(request):
    return render(request, 'basic_app/base.html',)

def other(request):
    return render(request, 'basic_app/other.html',)

def relative(request):
    return render(request, 'basic_app/relative_url_template.html',)