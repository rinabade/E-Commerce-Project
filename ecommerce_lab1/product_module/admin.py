from django.contrib import admin
from .models import Brand, Category, Product

class BrandAdmin(admin.ModelAdmin):
    list_display = ["name",]
    search_fields = ["name",]

    class Meta:
        model = Brand
admin.site.register(Brand, BrandAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "brand", "category",]
    search_fields = ["name", "price", "brand__name", "category__name",]
    list_filter = ["brand","category","price",]
    readonly_fields = []
    
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name",]
    search_fields = ["name",]

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)
