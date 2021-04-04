from django.contrib import admin

# Register your models here.
from listings.models import Category, Product, Review


class OrderReviewInline(admin.TabularInline):
    model = Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug":("name",),}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','price',
                    'available')
    list_filter = ('category','available')
    list_editable = ('price','available')
    prepopulated_fields = {"slug":("name",),}

    inlines = [OrderReviewInline]



