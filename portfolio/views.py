from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action (in django , it's called a view) (templates)



# pull data form db,transform the data, send emails 
# This is test perfose
# def index(request):
#     return HttpResponse("<h1>Hello World</h1>")


# starting page
def index(request):
    return render(request,'hello.html',{'name':'JEEVA'})