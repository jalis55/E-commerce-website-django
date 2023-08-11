from django.db import models

# Create your models here.

class Catergory(models.Model):
    title=models.CharField(max_length=100)
    created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='categories'

class Product(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    mini_img=models.ImageField(upload_to='media/products',blank=False)
    catergory=models.ForeignKey(Catergory,on_delete=models.CASCADE,related_name='category')
    preview_text=models.TextField(max_length=150)
    details_text=models.TextField(max_length=300)
    price=models.FloatField()
    old_price=models.FloatField(default=0.00)
    created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering=['-created']
