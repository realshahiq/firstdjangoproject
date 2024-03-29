from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import products
from .forms import productForm,productRawForm

# Create your views here.
#Django Model Forms
def products_create_view(request):
  form = productForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect("/products")
  context = {
  'form':form
  }
  return render(request,'products/product_create.html',context)

def products_render_data_view(request,id):
	try:
		product = products.objects.get(id=id)
	except products.DoesNotExist:
		return redirect("/products")
	form = productForm(request.POST or None,instance=product)
	if form.is_valid():
		form.save()
		return redirect("/products")
	context = {
	'form':form
	}
	return render(request,'products/product_create.html',context)

# Raw HTML form

# def products_create_view(request):
# 	if request.method == 'POST':
# 		title = request.POST.get('title')
# 		description = request.POST.get('description')
# 		summary = request.POST.get('summary')
# 		price = request.POST.get('price')
# 		print(title)
# 		products.objects.create(title=title,description=description,summary=summary,price=price)
# 		# return http.HttpResponseRedirect('/add-products')
# 		# products.objects.create
# 	context = {}
# 	return render(request,'products/product_create.html',context)

#Pure Django Form

# def products_create_view(request):
# 	form = productRawForm()
# 	if request.method == 'POST':
# 		form = productRawForm(request.POST)
# 		if form.is_valid():
# 			print(form.cleaned_data)
# 			products.objects.create(**form.cleaned_data)
# 	context = {
# 		'form': form
# 	}
# 	return render(request,'products/product_create.html',context)
def products_view_page(request):
	product = products.objects.all()
	context = {
	'product':product
	}
	return render(request,'products/product_detail.html',context)
def dynamic_lookup_views(request,id):
	try:
		product = products.objects.get(id=id)
	except products.DoesNotExist:
		return redirect("/products")
	context = {
	'product':product
	}
	return render(request,'products/product_lookup.html',context)

# def delete_product(request,id):
# 	try:
# 		product = products.objects.get(id=id)
# 	except products.DoesNotExist:
# 		return redirect("/products")
# 	if request.method == "POST":
# 		product.delete()
# 		return redirect("/products")
# 	context = {
# 	'product':product
# 	}
# 	return render(request,'products/product_delete.html',context)

def delete_product(request,id):
	print(request.method)
	query = products.objects.get(id=id)
	query.delete()
	return redirect("/products")