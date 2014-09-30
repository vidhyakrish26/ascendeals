from django.contrib import admin

from .models import Product, ProductImage, VariationCategory, AttributeCategory, ProductVariation


class ProductAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	list_display = ["title", "price", "coupon", "featured", "active", "created"]
	search_fields = ["title", "categories", "price"]
	list_filter = ["price", "coupon", "featured"]
	prepopulated_fields = {"slug": ("title",)}
	readonly_fields = ["created", "updated"]

	class Meta:
		model = Product

class ProductImageAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	list_display = ["product", "featured", "created"]
	search_fields = ["product"]
	list_filter = ["product", "featured"]
	readonly_fields = ["created", "updated"]

	class Meta:
		model = ProductImage


class VariationCategoryAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	list_display = ["title", "active", "created"]
	search_fields = ["title"]
	list_filter = ["created", "title"]
	readonly_fields = ["created", "updated"]

	class Meta:
		model = VariationCategory		


class AttributeCategoryAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	list_display = ["title", "active", "created"]
	search_fields = ["title"]
	list_filter = ["created", "title"]
	readonly_fields = ["created", "updated"]

	class Meta:
		model = AttributeCategory		


class ProductVariationAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	list_display = ["product", "variation", "created"]
	search_fields = ["product", "variation"]
	list_filter = ["product", "variation"]
	readonly_fields = ["created", "updated"]

	class Meta:
		model = ProductVariation		


admin.site.register(Product, ProductAdmin)		
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(VariationCategory, VariationCategoryAdmin)
admin.site.register(AttributeCategory, AttributeCategoryAdmin)
admin.site.register(ProductVariation, ProductVariationAdmin)