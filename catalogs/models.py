from django.db import models

from stores.models import Store

class Catalog(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)	
	slug = models.SlugField(unique=True)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		unique_together = ("title", "slug")


class Category(models.Model):
	catalog = models.ForeignKey(Catalog)
	stores = models.ManyToManyField(Store)
	categoryimage = models.ImageField(upload_to="categories/images", blank=True, null=True)
	title = models.CharField(max_length=120)
	parent = models.ForeignKey('self', blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	slug = models.SlugField(unique=True)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)			

	def __str__(self):
		return self.title

	class Meta:
		unique_together = ("title", "slug")



