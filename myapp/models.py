from django.db import models

class Image(models.Model):
    photo=models.ImageField(upload_to="my_image")
    date=models.DateTimeField(auto_now_add=True)
