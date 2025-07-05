from django.shortcuts import render

# Create your views here.

def DonePage(request):
    return render(request, 'donepage.html')
