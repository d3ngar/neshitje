from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from .models import Product, ProductImage
from .forms import ProductMainForm, ProductImageForm

def product(request):
    return render(request, 'product/product.html', {})

def edit_product(request):
    if request.user.is_authenticated():
        user_id = request.user
        #check if this is about a particular product
        if request.method == 'GET' and request.GET.get('item_id'):
            product = request.GET.get('item_id', None)
            prod = Product.objects.get(id=product)
            form = ProductMainForm(instance=prod)

            return render(request, 'product/edit-product.html', {'form':form})

        #for a new product
        elif request.method == 'POST':
            form = ProductMainForm(request.POST)
            if form.is_valid():
                print "Product addition a success"
                form.save(user_id)
                return redirect('user_details:account')
            else:
                print "Product addition failed"
                return render(request, 'product/edit-product.html', {'form':form})

        else:
            form = ProductMainForm()
            return render(request, 'product/edit-product.html', {'form':form})

    else:
        request.session['direct_url'] = 'product:edit-product'
        response = redirect('user_details:logging')
        return response


def product_view(request, product_id):
    print "finding product"

    return render(request, 'product/product.html', {})

def image_upload(request):
    if request.user.is_authenticated():
        user_id = request.user

        if request.method == 'POST':
            #form = ProductImageForm(request.POST, request.FILES)
            #if form.is_valid():
            image = request.FILES['image']
            prod = Product.objects.get(id=1)
            pi = ProductImage(product=prod, user=user_id, image=image)
            pi.save()
            print "image upload successful"
            #form.save(request.POST.get('product'))
            return redirect('user_details:account')

        form = ProductImageForm()
        return render (request, 'product/add-image.html', {'form':form, 'prod_id':Product.objects.get(id=1)})

    else:
        request.session['direct_url'] = 'product:image-upload'
        response = redirect('user_details:logging')
        return response
