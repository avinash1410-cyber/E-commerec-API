from django.http import HttpResponse

def home(request):
    return HttpResponse("In the Home page")