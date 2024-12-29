from django.contrib import admin
from .models import Product, Category


# Registering admin panel for Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name',
                    'product_description',
                    'product_image',
                    'category',
                    'product_price',
                    'created_at',
                    'updated_at'
                    )

    list_filter = ('product_name',
                    'product_description',
                    'product_image',
                    'category',
                    'product_price',
                    'created_at',
                    'updated_at'
                   )

    search_fields = ('product_name',
                    'product_description',
                    'category',
                    )


# Registering admin panel for Category
@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category_name',
                    'category_description',
                    )

    list_filter = ('category_name',
                   )

    search_fields = ('category_name',
                    'category_description',
                    )
