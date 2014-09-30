from django.shortcuts import render

from .models import Product, ProductImage
from catalogs.models import Catalog, Category


def home(request):
	catalogs = Catalog.objects.filter(active=True)
	latest_coupons = Product.objects.filter(active=True, coupon=False)
	latest_products = Product.objects.filter(active=True)
	featured_products = Product.objects.filter(active=True, featured=True)
	context = {"catalogs" : catalogs, "latest_coupons": latest_coupons, "latest_products": latest_products, "featured_products": featured_products}
	template = "products/home.html"
	return render(request, template, context)
