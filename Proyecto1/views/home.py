from django.http import HttpResponse

def home(request):
    return HttpResponse("Te amo Patsy")