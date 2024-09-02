import os
from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=50, null=False)
    email= models.EmailField(unique=True,null=False)
    password=models.CharField(max_length=50,null=False)
    address=models.CharField(max_length=150, blank=True,null=True)
    phone=models.IntegerField(blank=True,null=True)
    otp=models.IntegerField(blank=True,null=True)
    def __str__(self) -> str:
        return self.email
    
class main_Category(models.Model):
    category_name=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.category_name


class cupan(models.Model):
    cupan_code=models.CharField(unique=True,max_length=6)
    discount=models.IntegerField()
    aply=models.BooleanField(default=True)
    expier=models.DateTimeField()

    def __str__(self) -> str:
        return self.cupan_code
    
class product(models.Model):
    name=models.CharField(max_length=100,null=False)
    price=models.IntegerField(null=False)
    image=models.ImageField(upload_to="img",null=False)
    category=models.ForeignKey(main_Category,on_delete=models.CASCADE , null=True,blank=True)

    def __str__(self) -> str:
        return self.name

class billing_address(models.Model):
    name=models.CharField(max_length=100,null=False)
    phone=models.IntegerField(null=False)
    email=models.EmailField(max_length=100,null=False)
    address=models.CharField(max_length=200,null=False)
    # country=models.CharField(max_length=100,null=False)
    zipcode=models.IntegerField(null=False)
    
    def __str__(self) -> str:
        return self.address




class add_cart(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE , null=True,blank=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE , null=True,blank=True)
    name=models.CharField(max_length=100,null=False)
    price=models.IntegerField(null=False)
    qty=models.IntegerField(null=True,blank=True )
    t=models.IntegerField(null=True,blank=True)
    image=models.ImageField(upload_to="img",null=False)
    
    def __str__(self) -> str:
        return self.name


class add_wishlist(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE )
    user=models.ForeignKey(user,on_delete=models.CASCADE )
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to="img")

    def __str__(self) -> str:
        return self.name
    

class order(models.Model):
    order_id=models.CharField(max_length=10)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    zipcode=models.IntegerField(null=True,blank=True)
    cupan=models.CharField(max_length=6,null=True,blank=True)
    pname=models.CharField(max_length=10)
    qty=models.IntegerField(null=True,blank=True )
    price=models.IntegerField(null=False)

    def __str__(self) -> str:
        return f"{self.order_id} {self.pname}"




class rateing(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE )
    rate=models.IntegerField()
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    disc=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.product.name