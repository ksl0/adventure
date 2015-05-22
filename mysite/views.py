from django.http import HttpResponse,HttpResponseRedirect, HttpResponse

def home(request):
   return HttpResponse("Thanks!")
