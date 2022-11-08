from django.shortcuts import render
from .models import *
# Create your views here.
def IT(request):
    if request.method=='POST':
        heading_title1=request.POST['heading_title1']
        heading_title2=request.POST['heading_title2']

        data=Home(heading_title1=heading_title1,heading_title2=heading_title2)
        data.save()
    return render(request,"it.html")