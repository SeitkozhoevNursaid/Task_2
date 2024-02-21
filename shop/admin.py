from django.contrib import admin
from .models import Category,Product,Orders,Title
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","code","category")
    list_filter = ("name","code")
    search_fields = ("name","category")

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user']
    filter_horizontal = ['order_product']

admin.site.register(Orders, OrdersAdmin)
admin.site.register(Title)