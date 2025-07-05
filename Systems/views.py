from django.shortcuts import render

# Create your views here.
def Systemspage(request):
    return render(request, 'oursystems.html')
