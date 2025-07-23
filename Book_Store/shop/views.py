from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.views.generic.detail import DetailView
from django.views import View
from .models import Book, Author, Category, Order, Order_Line, Status
from django.db.models import DO_NOTHING, CASCADE
from shop.forms import SignUpForm


def logout_view(request):
    logout(request)
    return redirect('login')


# Class based view
class MainPage(TemplateView):
    template_name = 'main_page.html'


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('book-list')


class CustomLogoutView(TemplateView):
    template_name='logout_confirmation.html' 


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')


class BookView(DetailView):
    model = Book
    template_name = 'book.html' 
    context_object_name = 'book' 


class AuthorView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'author.html', {'authors': authors})


class CategoryView(View):
    def get(self,request):
        category=Category.objects.all()
        return render(request, 'category.html',{"category": Category})
    
    
class BookListView(View):
    def get(self, request):
        books = Book.objects.select_related('author', 'category').all()
        return render(request, 'book_list.html', {'books': books})


class AddToCart(View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        order_item, created = Order_Line.objects.get_or_create(order=order, book=book)
        if created:
            order_item.quantity = 1 
        else:
            order_item.quantity += 1  
        order_item.save()
        return redirect('cart')
    

class Cart(View):
    def get(self, request):
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        items = order.items.all()
        
        for item in items:
            item.subtotal = item.quantity * item.book.price  # total per articol

        total_general = sum(item.subtotal for item in items)  # total general
        order.total_cost = total_general
        order.save()

        return render(request, 'cart.html', {
            'items': items,
            'order': order,
            'total_general': total_general
        })


class Checkout(View):
    def get(self, request):
        order = Order.objects.filter(user=request.user, complete=False).first()

        if not order:
            return redirect('cart')

        total_general = sum(item.quantity * item.book.price for item in order.items.all())
        order.total_cost = total_general

        return render(request, 'checkout.html', {
            'order': order,
            'total_general': total_general,
        })

    
class CheckoutSuccess(TemplateView):
    template_name = 'checkout_success.html'


