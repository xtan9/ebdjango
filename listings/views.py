from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'listings/index.html')

def greetings(request):
    return render(request, 'listings/greetings.html')
