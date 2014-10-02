from django.shortcuts import render

from .models import Catalog, Category

def preview(request, slug):
	catalogs = Catalog.objects.filter(active=True)
	catalog = Catalog.objects.get(slug=slug, active=True)
	context = {"catalogs":catalogs,"catalog":catalog}
	template = "catalogs/preview.html"
	return render(request, template, context)


def categoryview(request, catalog, slug):
	basecatalog = Catalog.objects.get(slug=catalog, active=True)
	catalogs = Catalog.objects.filter(active=True)
	category = Category.objects.get(slug=slug, active=True)	
	context = {"catalog": basecatalog, "catalogs":catalogs,"category":category}
	template = "catalogs/categoryview.html"
	return render(request, template, context)	
