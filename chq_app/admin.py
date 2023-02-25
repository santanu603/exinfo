from django.contrib import admin
from .models import master, order, replacement
admin.site.register(master)
admin.site.register(order)
admin.site.register(replacement)


# Register your models here.
class BookOption(admin.ModelAdmin):
    readonly_fields=['date']