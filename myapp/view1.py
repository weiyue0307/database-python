__author__ = 'weiyue'
from myapp.models import user,administrator,dessert,dessert_shop,comment
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from PJ1.forms import LoginForm,CommentForm,ShopForm
from django.template import RequestContext
from django.shortcuts import render

def index(req):
    #username = req.COOKIES.get('username','')
    username = req.session.get('username',False)
    return render_to_response('index.html' ,{'username':username})

def myself(req):

    comments = comment.objects.filter(user_name =req.session.get('username',False)).order_by("-comment_date")
    return render_to_response("userself_select.html", {'comments':comments})

def useradd(req):
    if req.method =='POST':
        uf= CommentForm(req.POST)
        if uf.is_valid():

            mycomment =comment()
            #mycomment.commentid = uf.cleaned_data['commentid']
            mycomment.content = uf.cleaned_data['content']
            mycomment.dessert_name = uf.cleaned_data['dessert_name']
            mycomment.user_name = req.session.get('username',False)
            #mycomment.user_name = uf.cleaned_data['user_name']
            mycomment.dessert_shop_name = uf.cleaned_data['dessert_shop_name']
            #mycomment.comment_date =
            mycomment.save()
            return render_to_response('add_success.html')
    else:
        uf= CommentForm()
    #ctx = {
        #'form':form,
        #'ties':comment.objects.all()
    #}
    #return render_to_response('allcomment.html',ctx)
    return render_to_response('allcomment.html',{'uf':uf})

def deletedessert(req):

    deid=req.GET.get('did')
    #return HttpResponse(deid)
    rcomment = comment.objects.filter(commentid=deid)
    rcomment.delete()
    return HttpResponseRedirect('/myapp/index/')

def update(req):
    rcommentid=req.GET.get('rcommentid')
    rcontent=req.GET.get('rcontent')
    rdessert=req.GET.get('rdessert')
    rshop=req.GET.get('rshop')
    if req.method =='POST':
        uf= CommentForm(req.POST)
        if uf.is_valid():

            mycomment =comment.objects.filter(commentid=rcommentid)
            mycomment.update(
            content = uf.cleaned_data['content'],
            dessert_name = uf.cleaned_data['dessert_name'],
            user_name = req.session.get('username',False),
            dessert_shop_name = uf.cleaned_data['dessert_shop_name'])
            return render_to_response('update_success.html')
    else:
        uf= CommentForm(
            initial={'commentid': rcommentid,'content': rcontent ,'dessert_name':rdessert,'dessert_shop_name':rshop}
        )
    return render_to_response('updatecomment.html',{'uf':uf})

def delete(req):
    rcommentid=req.GET.get('rcommentid')
    rcontent=req.GET.get('rcontent')
    rdessert=req.GET.get('rdessert')
    rshop=req.GET.get('rshop')
    mycomment =comment.objects.filter(commentid=rcommentid)
    mycomment.delete()
    return render_to_response("delete_success.html")

def enter(req):
    rcomment=comment.objects.all()
    return render_to_response("enter.html",{'rcomment':rcomment})

def userenter(req):
    rcomment=comment.objects.all()
    return render_to_response("userenter.html",{'rcomment':rcomment})

def deleteshop(req):
    rphonenumber=req.GET.get('rphonenumber')
    myshop=dessert_shop.objects.filter(phonenumber=rphonenumber)
    myshop.delete()
    return render_to_response("deleteshop_success.html")

def updateshop(req):
    rphonenumber=req.GET.get('rphonenumber')
    rname=req.GET.get('rname')
    rshopid=req.GET.get('rshopid')
    if req.method =='POST':
        uf= ShopForm(req.POST)
        if uf.is_valid():

            myshop =dessert_shop.objects.filter(phonenumber=rphonenumber)
            myshop.update(phonenumber = uf.cleaned_data['phonenumber'],
            name = uf.cleaned_data['name'],)
            return render_to_response('addshop_success.html')
    else:
        uf= ShopForm(
            initial={'shopid': rshopid,'name': rname ,'phonenumber':rphonenumber}
        )
    return render_to_response('updateshop.html',{'uf':uf})