from django.shortcuts import render

# Create your views here.
from myapp.models import user,administrator,dessert,dessert_shop,comment
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from PJ1.forms import LoginForm,RegistForm,ShopForm
from django.template import RequestContext
from django.shortcuts import render


def regist(req):
    if req.method == 'POST':
        uf = LoginForm(req.POST)
        if uf.is_valid():

            #account = uf.cleaned_data['account']
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            users=user.objects.filter(username= username)
            if users:
                return render_to_response("wrongregist.html")
            else:
                user.objects.create(username= username,password=password)
                return render_to_response('regist_success.html')
    else:
        uf = LoginForm()
    return render_to_response('regist.html',{'uf':uf})


def adminlogin(req):
    if req.method =='POST':
        uf = LoginForm(req.POST)
        if uf.is_valid():

            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            administrators = administrator.objects.filter(username__exact = username,password__exact = password)
            if administrators:
                    response = HttpResponseRedirect('/myapp/adminindex/')
                    response.set_cookie('username',username,3600)
                    return response
            else:
                return render_to_response("wronglogin.html")
    else:
        uf = LoginForm()
    return render_to_response('adminlogin.html',{'uf':uf})


def adminindex(req):
    username = req.COOKIES.get('username','')
    return render_to_response('adminindex.html' ,{'username':username})


def login(req):
    if req.method == 'POST':
        uf = LoginForm(req.POST)
        if uf.is_valid():

            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            req.session['username'] = username
            req.session['password'] = password


            users = user.objects.filter(username__exact = username,password__exact = password)
            if users:

                response = HttpResponseRedirect('/myapp/index/')

                response.set_cookie('username',username,3600)
                return response
            else:
                return render_to_response("wronglogin.html")

               # return HttpResponseRedirect('/myapp/login/')
    else:
        uf = LoginForm()
    return render_to_response('login.html',{'uf':uf})


def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})


def logout(req):
    response = HttpResponse('logout !!')

    response.delete_cookie('username')
    return HttpResponseRedirect('/')


def search_form(request):
    return render_to_response("search_form.html")


def search(request):
    if 'q' in request.GET and request.GET['q']:
		rusers=user.objects.filter(username__icontains=request.GET['q'])
		return render_to_response("select.html",{'users':rusers})
    else:
        return render_to_response("search_form.html")


def search_choice(req):
    return render_to_response("search_choice.html")

def adminsearch_choice(req):
    return render_to_response("adminsearch_choice.html")


def dessert_search_form(req):
    return render_to_response("dessert_search_form.html")


def dessert_shop_search_form(req):
    return render_to_response("dessert_shop_search_form.html")


def user_search_form(req):
    return render_to_response("user_search_form.html")

def admindessert_search_form(req):
    return render_to_response("admindessert_search_form.html")


def admindessert_shop_search_form(req):
    return render_to_response("admindessert_shop_search_form.html")


def adminuser_search_form(req):
    return render_to_response("adminuser_search_form.html")


def ruser(request):
    if 'q' in request.GET and request.GET['q']:
        rcomment = comment.objects.filter(user_name__icontains=request.GET['q']).order_by("-comment_date")
        return render_to_response("select.html",{'rcomment':rcomment})
    else:
        return render_to_response("user_search_form.html")


def rdessert(request):
    if 'q' in request.GET and request.GET['q']:
        rcomment = comment.objects.filter(dessert_name__icontains=request.GET['q']).order_by("-comment_date")
        return render_to_response("dessert_select.html",{'rcomment':rcomment})
    else:
        return render_to_response("dessert_search_form.html")


def rdessert_shop(request):
    if 'q' in request.GET and request.GET['q']:
        rcomment = comment.objects.filter(dessert_shop_name__icontains=request.GET['q']).order_by("-comment_date")
        return render_to_response("dessert_shop_select.html",{'rcomment':rcomment})
    else:
        return render_to_response("dessert_shop_search_form.html")


def shop(req):
    shopname=req.GET.get('shopname')
    shop=dessert_shop.objects.filter(name=shopname)
    return render_to_response("shop.html",{'shops':shop})


def addshop(req):
    if req.method == 'POST':
        uf = ShopForm(req.POST)
        if uf.is_valid():
            dessertshops=dessert_shop.objects.filter(phonenumber= uf.cleaned_data['phonenumber'])
            if dessertshops:
                return render_to_response("wrongaddshop.html")
            else:
                dessert_shops=dessert_shop()
                #dessert_shop.shopid = uf.cleaned_data['shopid']
                dessert_shops.name = uf.cleaned_data['name']
                dessert_shops.phonenumber = uf.cleaned_data['phonenumber']
                dessert_shops.save()
                return render_to_response('update_shop_success.html')
    else:
        uf = ShopForm()
    return render_to_response('addshop.html',{'uf':uf})


def showshop(req):

    shops=dessert_shop.objects.all()

    return render_to_response("showshop.html",{'shops':shops})

def adminruser(request):
    if 'q' in request.GET and request.GET['q']:
        rcomment = comment.objects.filter(user_name__icontains=request.GET['q']).order_by("-comment_date")
        return render_to_response("adminselect.html",{'rcomment':rcomment})
    else:
        return render_to_response("adminuser_search_form.html")


def adminrdessert(request):
    if 'q' in request.GET and request.GET['q']:
        rcomment = comment.objects.filter(dessert_name__icontains=request.GET['q']).order_by("-comment_date")
        return render_to_response("admindessert_select.html",{'rcomment':rcomment})
    else:
        return render_to_response("admindessert_search_form.html")


def adminrdessert_shop(request):
    if 'q' in request.GET and request.GET['q']:
        rcomment = comment.objects.filter(dessert_shop_name__icontains=request.GET['q']).order_by("-comment_date")
        return render_to_response("admindessert_shop_select.html",{'rcomment':rcomment})
    else:
        return render_to_response("admindessert_shop_search_form.html")








