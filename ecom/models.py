from django.db import models
from django.shortcuts import  reverse

class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    description = models.TextField()
    img = models.ImageField(upload_to='imgProduct')
    def __str__(self):
        return self.name
    

class Transaction(models.Model):
    firstname = models.CharField("first name", max_length=20)
    lastname = models.CharField("last name", max_length=20)
    address = models.TextField("Address", max_length=300)
    phone = models.CharField("Phone Number", max_length=10)
    id_trans = models.IntegerField("id_trans")
    message = models.TextField("Message", max_length=300)
    Order = models.ManyToManyField(Product, through='Order')
    def __str__(self):
        return self.lastname
    def sumCount(self):
        tong = 0
        for i in Order:
            tong += i.orderPrice()
        return tong

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete = models.CASCADE)
    amount = models.IntegerField("amout", default=1)
    priceOrder = models.IntegerField()
    def __str__(self):
        return f"{self.amount} of {self.product.name}"
    def orderPrice(self):
        self.priceOrder = self.amount*self.product.price
        return priceOrder
