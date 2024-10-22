from django.db import models


class Contact (models.Model):
    name =models.CharField( max_length=250,blank=True,null=True)
    email = models.EmailField( max_length=254)
    phone =models.IntegerField()
    subject =models.CharField(max_length=250)
    message =models.TextField()

    def __str__(self):
        return self.name
    


    