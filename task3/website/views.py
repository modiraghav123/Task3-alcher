from django.shortcuts import render

def home(request):
     return  render(request, 'website/index.html')
 
 
def page1(request):
     return  render(request, 'website/page1.html')
 
def page2(request):
     return  render(request, 'website/page2.html')