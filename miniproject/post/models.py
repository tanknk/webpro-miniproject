from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    create_by = models.ForeignKey(User, on_delete = models.PROTECT)
    create_date = models.DateTimeField(auto_now=True)
    text_book = models.CharField(max_length=200)
    TYPE = (
        ("S", "sell"),
        ("B", "buy")
    )
    type = models.CharField(max_length=1 , choices=TYPE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to="picture/")
    STATUS = (
        ("OPEN", "open"),
        ("CLOSE", "close")
    )
    status = models.CharField(max_length=5, choices=STATUS)

class Message(models.Model):
    message = models.TextField()
    post_id = models.ForeignKey(Post, on_delete= models.PROTECT)
    create_by = models.ForeignKey(User, on_delete = models.PROTECT)
    create_date = models.DateTimeField(auto_now=True)