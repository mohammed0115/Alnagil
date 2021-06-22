from django.contrib import admin

# Register your models here.

from django.contrib import admin
from Products.models import Product,Category
# Register your models here.



class ProductAdmin(admin.ModelAdmin):
    list_display=['name','p_type','sale_price','p_cost','serial_number','company','product_created','product_end','category']
    list_filter=['p_cost','sale_price','company','category']
    fieldsets = (
      ('product info', {
          'fields': ('name','p_type','sale_price','p_cost','serial_number')
      }),
      ('creatation info', {
          'fields': ('company', ('product_created', 'product_end'))
      }),
      ('Category  info', {
          'fields':  ('category',)
      }),
   )
class CategoryInLine(admin.ModelAdmin):
    list_display=['name','Description']
    # inlines = [
    #     ProductAdmin
    # ]
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryInLine)