from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('category/<cui>',views.cat,name="category"),
    path('signup',views.signup),
    path('signin',views.signin),
    path('signout',views.signout),
    path('wishlist/<int:id>',views.wish_list),
    path('show_wishlist',views.show_wishlist),
    path('delete_wishlist/<int:id>',views.delete_wishlist),
    path('cart/<int:id>',views.cart),
    path('show_cart',views.show_cart),
    path('delete_cart/<int:id>',views.delete_cart),
    path('move_wishlist/<int:id>',views.move_wishlist),
    path('type',views.type),
    path('buy_cartElements/<int:sum>',views.buy_cart),
    path('myorders',views.orders),
]
