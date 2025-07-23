from django.db import models
from django.db.models import Model, DO_NOTHING,CASCADE, DateTimeField, CharField, ForeignKey, IntegerField, TextField, DecimalField
from django.conf import settings
from users.models import User


# Create your models here.

class Author(Model):
    name=CharField(max_length=125)
    surname=CharField(max_length=125)
    
    def __str__(self):
        return self.name


class Category(Model):
    name=CharField(max_length=125)
    
    def __str__(self):
        return self.name


class Book(Model):
    image=models.ImageField(upload_to='book_images/', blank=True, null=True)
    title=CharField(max_length=125)
    author=ForeignKey(Author, on_delete=DO_NOTHING)
    pages=IntegerField()
    category=ForeignKey(Category, on_delete=DO_NOTHING)
    publish_house=CharField(max_length=125)
    summary=TextField(blank=True)
    price=DecimalField(max_digits=6, decimal_places=2)
    stock=IntegerField()
    
    def __str__(self):
        return f"{self.title} by {self.author}"


class PublishHouse(Model):
    name=CharField(max_length=125)
    
    def __str__(self):
        return self.name
    

class Status(Model):
    status_name=CharField()

    def __str__(self):
        return self.status_name
    

class Order(Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    total_cost = DecimalField(max_digits=6, decimal_places=2, default=0)
    date_of_order = DateTimeField(auto_now_add=True)
    status = ForeignKey(Status, on_delete=models.DO_NOTHING, null=True, blank=True)
    complete=models.BooleanField(default=False) 

    def __str__(self):
        return f"Comanda #{self.id} - {self.user.username}"
    

class Order_Line(Model):
    book=ForeignKey(Book,on_delete=DO_NOTHING)
    quantity=IntegerField(default=1)
    total_price=DecimalField(max_digits=6, decimal_places=2, default=0)
    order=ForeignKey(Order, on_delete=CASCADE, related_name='items')

    def __str__(self):
        return f"{self.quantity} x {self.book.title} in Order {self.order.id}"
    

class CartItem(Model):
    user=models.ForeignKey(User, on_delete=DO_NOTHING)
    book=ForeignKey(Book, on_delete=DO_NOTHING)
    qty=IntegerField()
    
    def total_price(self):
        return self.book.price * self.qty
    
    def __str__(self):
        return f"{self.qty} x {self.book.title} in Cart of {self.user.username}"
    

