from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Product name')
    category_description = models.TextField()

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['category_name']


# Create class Product
class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Product name')
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='images/', verbose_name='Saved image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_price = models.IntegerField(help_text='Insert price for the product')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['product_name']

