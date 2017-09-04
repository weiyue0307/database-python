__author__ = 'weiyue'
from django.http import HttpResponse
from myapp.models import user
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from PJ1.forms import LoginForm

def identity(req):
	return render_to_response("identity.html")

def login(request):
    if request.method == 'POST':
        uf = LoginForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            users = user.objects.filter(username__exact = username,password__exact = password)
            if users:
                return render_to_response('success.html',{'username':username})
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = LoginForm()
    return render_to_response('login.html',{'uf':uf})

def select_all(request):
	rusers=user.objects.all()
	return render_to_response("select.html",{'users':rusers})

def select(request):
	rusers=user.objects.filter(account=1)
	return render_to_response("select.html",{'users':rusers})


def search_form(request):
    return render_to_response("search_form.html")

def search(request):
    if 'q' in request.GET and request.GET['q']:
		rusers=user.objects.filter(username__icontains=request.GET['q'])
		return render_to_response("select.html",{'users':rusers})
        #message = 'You searched for: %r' % request.GET['q']
    else:
	    #return HttpResponse("You submitted an empty form.")
        return render_to_response("search_form.html")

