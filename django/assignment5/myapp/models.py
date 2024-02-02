from django.db import models

# Create your models here.




class product_mst(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50)



    def __str__(self):
        return self.product_name
    

class product_sub_cat(models.Model):
    product=models.ForeignKey(product_mst,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    photo=models.ImageField(upload_to="myimage")
    modal=models.CharField(max_length=100)
    ram=models.CharField(max_length=100)




    def __str__(self):
        return self.product.product_name