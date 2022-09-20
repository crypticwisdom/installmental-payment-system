from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    try:
        return HttpResponse("Home page")
    except (Exception, ) as err:
        return HttpResponse(err)
