from django.contrib import admin

from catalogs.models import Catalog, Category

class CatalogAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	list_display = ["title", "active", "created"]
	list_filter = ["title", "created"]
	search_fields = ["title"]
	prepopulated_fields = {"slug" : ("title",)}
	readonly_fields = ("created", "updated")

	class Meta:
		model = Catalog


class CategoryAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	list_display = ["title", "parent", "active", "created"]
	list_filter = ["title", "parent"]
	search_fields = ["title", "parent"]
	prepopulated_fields = {"slug" : ("title",)}
	readonly_fields = ("created", "updated")

	class Meta:
		model = Catalog		


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Category, CategoryAdmin)