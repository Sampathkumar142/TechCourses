from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)

class Courses(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    playtime = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class UserQuery(models.Model):
    email = models.EmailField(max_length=50)
    message = models.TextField()