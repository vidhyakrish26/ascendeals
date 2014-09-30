from django.db import models

from catalogs.models import Category
from stores.models import Store


class Product(models.Model):
	category = models.ForeignKey(Category, null=True)
	store = models.ForeignKey(Store, null=True)
	title = models.CharField(max_length=120)
	description = models.TextField()
	slug = models.SlugField(unique=True)
	price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
	sales_price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
	featured = models.BooleanField(default=False)
	coupon = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		unique_together = ("title", "slug")


class ProductImage(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to="products/images")		
	thumbnail = models.BooleanField(default=False)
	featured = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.product.title


class VariationCategory(models.Model):
	title = models.CharField(max_length=120)			
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.title


class AttributeCategory(models.Model):	
	title = models.CharField(max_length=120)			
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.title


class ProductVariation(models.Model):
	product = models.ForeignKey(Product)
	variation = models.ForeignKey(VariationCategory)		
	variant = models.CharField(max_length=120)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.product.title	