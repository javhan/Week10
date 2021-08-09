from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

class Cat(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    colour = models.CharField(max_length=10)

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"