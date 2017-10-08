from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	return render(request, 'platoweb/index.html')

def about(request):
	return render(request, 'platoweb/about.html')

def causes(request):
	return render(request, 'platoweb/causes.html')