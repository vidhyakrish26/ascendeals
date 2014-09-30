from django.contrib import admin

from stores.models import Store, StoreProfile

class StoreAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	list_display = ["title", "active", "created"]
	list_filter = ["title", "created"]
	search_filter = ["title"]
	readonly_fields = ["created", "updated"]
	prepopulated_fields = {"slug": ("title",)}

	class Meta:
		model = Store


class StoreProfileAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	list_display = ["store", "city", "zipcode", "active", "created"]
	list_filter = ["store", "city", "zipcode"]
	search_filter = ["store", "city", "zipcode"]
	readonly_fields = ["created", "updated"]

	class Meta:
		model = StoreProfile

admin.site.register(Store, StoreAdmin)		
admin.site.register(StoreProfile, StoreProfileAdmin)