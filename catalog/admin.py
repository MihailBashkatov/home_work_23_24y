from django.contrib import admin
from .models import Product, Category


# Registering admin panel for Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'product_name',
                    'category',
                    'product_price',
                    )

    list_filter = ('category',
                   )

    search_fields = ('product_name',
                    'product_description',
                    )


# Registering admin panel for Category
@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'category_name',
                    )

    list_filter = ('id', 'category_name',
                   )

    search_fields = ('category_name',
                    'category_description',
                    )
