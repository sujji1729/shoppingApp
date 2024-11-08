from django.db import models
from datetime import datetime

# Create your models here.
class ProductModel(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=20, unique=True)
    product_price = models.TextField()
    product_discription = models.TextField()
    product_color = models.TextField()
    product_quantity = models.TextField()
    product_category = models.TextField()
    product_image = models.FileField(upload_to="assets/product_image/")
    product_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.product_name


