from django.db import models

class Store(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	slug = models.SlugField(unique=True)
	logo = models.ImageField(upload_to="stores/logos")
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)	

	def __str__(self):
		return self.title

	class Meta:
		unique_together = ("title", "slug")


class StoreProfile(models.Model):
	store = models.ForeignKey(Store)
	address1 = models.CharField(max_length=120)
	address2 = models.CharField(max_length=120)
	city = models.CharField(max_length=120)
	country = models.CharField(max_length=120)
	zipcode = models.CharField(max_length=120)
	mobile = models.CharField(max_length=12)
	telephone = models.CharField(max_length=12)
	email = models.EmailField(blank=False, null=False)
	website = models.URLField(blank=False, null=False)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.store.title



