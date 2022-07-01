
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#def home_view(request,*args,**kwargs):
    #print(args,kwargs)
    #print(request.user)
    #return HttpResponse("<h1>hell0</h1>" )

def home_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
   # return HttpResponse("<h1>hell0</h1>" )
    return render(request,"home.html",{})


def contact_view(request,*args,**kwargs):
     return render(request,"contact.html",{})

def about_view(request,*args,**kwargs):
    my_context = {
        "title":"abc this is about us",
        "this_is_true":True,
        "my_number":123,
        "my_list": [123,4242,312,"Abc"],
        "my_html": "<h1>hello world</h1>"
    }
    return render(request,"about.html",my_context)