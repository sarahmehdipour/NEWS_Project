from django.db import models

from django.db import models
from django.contrib.auth import get_user_model


User=get_user_model()

class News(models.Model):
  title=models.CharField(max_length=254)
  description=models.TextField()
  active=models.BooleanField(default=False)
  updated_time=models.DateTimeField(auto_now=True)
  created_time=models.DateTimeField(auto_now_add=True)

  author=models.ForeignKey(User,on_delete=models.CASCADE,blank=False)
#   image=models.ImageField(upload_to='news/images/',default="news/images/1.png")
  category=models.ManyToManyField("Category")
  Tag=models.ManyToManyField("Tag")
  breif_description=models.CharField(max_length=80,null=True,blank=True)
  


  def __str__(self):
    return self.title

  class Meta:
    verbose_name="new  "
    verbose_name_plural="news "
    ordering=['created_time']




class Category(models.Model):
  title=models.CharField(max_length=80)

  def __str__(self):
    return self.title
  
  
  class Meta:
    verbose_name="category  "
    verbose_name_plural="categories "
  

  



# class Comment(models.Model):
#   post=models.ForeignKey(Post,on_delete=models.CASCADE)
#   name=models.CharField(max_length=90)
#   email=models.EmailField(max_length=150)
#   subject=models.CharField(max_length=254)
#   message=models.TextField()
#   created_time=models.DateTimeField(auto_now_add=True)
#   active=models.BooleanField(default=False)

#   def __str__(self):
#     return self.name

#   class Meta:
#     ordering=['-created_time',]





class Tag(models.Model):
  title=models.CharField(max_length=80)

  def __str__(self):
    return self.title