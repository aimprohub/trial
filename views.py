from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views her
def index(request):
	return render(request,'index1.html', {'name','ganesh'})


