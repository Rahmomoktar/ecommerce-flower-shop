from django.db import models

# Create your models here.


class Contact_Us(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200)
    Message=models.TextField()


    def __str__(self):
        return self.Name
    



class SpecialFlower(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    rating = models.CharField(max_length=12)
    ch_image = models.ImageField(upload_to='images',blank=True,null=True)

    def __str__(self):
        return self.name
    


class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    Quentity_Od = models.PositiveIntegerField()
    date = models.DateTimeField()
    time = models.TimeField()
    

    def __str__(self):
        return self.name
    


# orders

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.product_name}"


