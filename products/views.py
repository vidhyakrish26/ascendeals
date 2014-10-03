from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Product, ProductImage
from catalogs.models import Catalog, Category
from stores.models import Store


def home(request):
	catalogs = Catalog.objects.filter(active=True)
	latest_coupons = Product.objects.filter(active=True, coupon=False)
	latest_products = Product.objects.filter(active=True)
	featured_products = Product.objects.filter(active=True, featured=True)
	context = {"catalogs" : catalogs, "latest_coupons": latest_coupons, "latest_products": latest_products, "featured_products": featured_products}
	template = "products/home.html"
	return render(request, template, context)

def productsview(request, category, store):
	catalogs = Catalog.objects.filter(active=True)
	basecategory = Category.objects.get(slug=category, active=True)
	store = Store.objects.get(slug=store, active=True)
	products = Product.objects.filter(store=store, category=basecategory)
	context = {"products":products, "catalogs":catalogs, "store":store, "category":basecategory}
	template = "products/all.html"
	return render(request, template, context)

def preview(request, slug):
	catalogs = Catalog.objects.filter(active=True)
	product = Product.objects.get(slug=slug, active=True)
	products = Product.objects.filter(store=product.store, category=product.category)	
	context = {"product": product, "catalogs":catalogs, "products": products}
	template = "products/preview.html"
	return render(request, template, context)	

def search(request):
	term = request.GET.get("q")
	catalogs = Catalog.objects.filter(active=True)
	if(term):
		products = Product.objects.filter(active=True, title__icontains=term)
		context = {"products":products, "catalogs":catalogs, "term":term}
		template = "products/search.html"
	else:
		return HttpResponseReditect(reverse('product_home'))

	return render(request, template, context)