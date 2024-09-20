from django.db import models
from datetime import datetime
  

# Create your models here.
class menu_data(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    mono=models.CharField(max_length=50)
    price=models.IntegerField()
    
class wishlist(models.Model):
    user_name=models.CharField(max_length=100)
    p_id=models.ForeignKey(menu_data,null=True,on_delete=models.CASCADE)

class cart_data(models.Model):
    user_name=models.CharField(max_length=100)
    p_id=models.ForeignKey(menu_data,null=True,on_delete=models.CASCADE)
    qty=models.IntegerField(default=1)

class order_data(models.Model):
    user_name=models.CharField(max_length=100)
    p_id=models.ForeignKey(menu_data,null=True,on_delete=models.CASCADE)
    qty=models.IntegerField(default=1)
    date_time=models.DateTimeField(default=datetime.now())
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
   

