from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import menu_data,wishlist,cart_data,order_data
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    category_list=menu_data.objects.all()[:8]
    return render(request,"category.html",{"category_list":category_list})

def type(request):
    if request.method=='POST':
         type_name=request.POST.get('type_name')
         typesearch_list=menu_data.objects.filter(mono=type_name)
         return render(request,"type.html",{"typesearch_list":typesearch_list})

def cat(request,cui):
    category_list=menu_data.objects.filter(category=cui)
    return render(request,"category.html",{"category_list":category_list})

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('mail')
        pwd=request.POST.get('pwd')
        cpwd=request.POST.get('cpwd')
        check=User.objects.filter(username = uname)
        if check:
            return render (request,'signup.html', {'error':'Username is already taken!'})
        if pwd==cpwd:
            my_user=User.objects.create_user(username=uname,email=email,password=pwd)
            my_user.save()
            return  render(request,"category.html")
        else:
             return render(request,'signup.html',{'error':'Password does not match!'})
      
    return render(request,'signup.html')
    # return HttpResponse("Hello")

def signin(request):
     if request.method=='POST':
         uname=request.POST.get('username')
         pwd=request.POST.get('pwd')
         user=authenticate(request,username=uname,password=pwd)
         if user is not None:
             auth.login(request,user)
             return  render(request,"category.html")
         else:
             return render(request,'signin.html',{'error':'Username or password is wrong!'})
         
     return render(request,'signin.html')

@login_required(login_url='/ClicknEat/signin')
def signout(request):
    auth.logout(request)
    return render(request,"category.html")

@login_required(login_url='/ClicknEat/signin')
def wish_list(request,id):
    search_wish=wishlist.objects.filter(p_id_id=id)
    if search_wish:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        username=request.user.username
        wishlist_data=wishlist(user_name=username,p_id_id=id)
        wishlist_data.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/ClicknEat/signin')
def show_wishlist(request):
    username=request.user.username
    curuser_wishlist=wishlist.objects.filter(user_name=username).values('p_id_id')
    final_wishlist=[]
    for item in curuser_wishlist:
        wishlist_menu=list(menu_data.objects.filter(id=item['p_id_id']).values())
        final_wishlist.append(wishlist_menu)

   
    # return HttpResponse(final_wishlist)
    return render(request,"wishlist.html",{"final_wishlist":final_wishlist})

def delete_wishlist(request,id):
    wishlist.objects.filter(p_id_id=id).delete()
    return HttpResponseRedirect('/ClicknEat/show_wishlist')

@login_required(login_url='/ClicknEat/signin')
def cart(request,id):

        search_cart=cart_data.objects.filter(p_id_id=id)
        # qty=request.POST.get('qty')
        if search_cart:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            username=request.user.username
            cart_list=cart_data(user_name=username,p_id_id=id)
            cart_list.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/ClicknEat/signin')
def show_cart(request):
    username=request.user.username
    curuser_cart=cart_data.objects.filter(user_name=username).values('p_id_id')
    final_cart=[]
    sum=0
    for item in curuser_cart:
        cart_menu=list(menu_data.objects.filter(id=item['p_id_id']).values())
        final_qty=cart_data.objects.filter(user_name=username,p_id_id=item['p_id_id']).values('qty')
        sum=sum+cart_menu[0]['price']*final_qty[0]['qty']  # sum calculated is correct,qty is also taken care of
        final_cart.append(cart_menu)

    context = {"final_cart":final_cart,"sum":sum}
    print(context)
    total={'sum':sum}
    return render(request,"cart.html",context)

def delete_cart(request,id):
    cart_data.objects.filter(p_id_id=id).delete()
    return HttpResponseRedirect('/ClicknEat/show_cart')

def move_wishlist(request,id):

    cart_data.objects.filter(p_id_id=id).delete()
    username=request.user.username
    wishlist_data=wishlist(user_name=username,p_id_id=id)
    wishlist_data.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def buy_cart(request,sum):
    if request.method=='POST':
        add=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        elements_in_cart=cart_data.objects.all()
        for item in elements_in_cart:
            user_name=item.user_name
            p_id_id=item.p_id_id
            qty=item.qty
            order_data.objects.create(user_name=user_name,p_id_id=p_id_id,qty=qty,address=add,city=city,state=state)
            cart_data.objects.filter(p_id_id=p_id_id).delete()
    if sum:
      return render(request,"buy.html")
    else:
      return render(request,"cart.html")  
    
    
def orders(request):
    username=request.user.username
    allorder_menudata=order_data.objects.filter(user_name=username).values('p_id_id')
    allorder_data=order_data.objects.filter(user_name=username)
    final_order=[]
    for item in  allorder_menudata:
        order_menu=list(menu_data.objects.filter(id=item['p_id_id']).values())
        final_order.append(order_menu)

    # final_dict={"final_order":final_order, "allorder_data":allorder_data}
    return render(request,"order.html",{"final_order":final_order})