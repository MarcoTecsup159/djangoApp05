from django.contrib import admin

# Register your models here.
from .models import Categoria
from .models import Producto
from .models import Cliente

def incrementar_stock(modeladmin, request, queryset):
    for producto in queryset:
        producto.stock += 20
        producto.save()

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')
    actions = [incrementar_stock]

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente)
