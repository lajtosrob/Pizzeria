from django.db import models

# Create your models here.

class Topping(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def serializer(self):
        return {"id":self.id, "name":self.name}

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    toppings = models.ManyToManyField(Topping)
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.name
    
    def serializer(self):
        serialized_toppings = []

        for topping in self.toppings.all():
            serialized_toppings.append(topping.serializer())

        return {
            'name':self.name, 
            'price':self.price, 
            'toppings':serialized_toppings,
            'image' : str(self.image),
        }
