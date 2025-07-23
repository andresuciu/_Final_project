"""
URL configuration for Book_Store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop.views import MainPage, CustomLoginView, RegisterView, logout_view, CustomLogoutView
from django.contrib.auth.views import LoginView, LogoutView

from shop.views import BookView, AuthorView, CategoryView, BookListView, AddToCart, Cart, Checkout, CheckoutSuccess
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('logout_confirmation/',CustomLogoutView.as_view(),name='logout_confirmation'),
    path('register/',RegisterView.as_view(),name='register'),
    path('',BookListView.as_view(),name='book-list'),
    path('authors/',AuthorView.as_view(),name='authors'),
    path('book/<int:pk>/',BookView.as_view(),name='book-detail'),
    path('books/',BookListView.as_view(),name='book-list'),
    path('category/',CategoryView.as_view(),name='category'),
    path('add_to_cart/<int:book_id>/', AddToCart.as_view(), name='add_to_cart'),
    path('cart/', Cart.as_view(), name='cart'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('checkout/success/', CheckoutSuccess.as_view(template_name='checkout_success.html'), name='checkout_success'),
    #
 
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)