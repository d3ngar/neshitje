from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from .models import Listing, ListingImage, CategoryTree
from .forms import ListingMainForm, ListingImageForm

def listing(request):
    return render(request, 'listing/listing.html', {})

def edit_listing(request):
    if request.user.is_authenticated():
        user_id = request.user
        #check if this is about a particular product
        if request.method == 'GET' and request.GET.get('item_id'):
            listing = request.GET.get('item_id', None)
            prod = Listing.objects.get(id=listing)
            form = ListingMainForm(instance=prod)

            return render(request, 'listing/edit-listing.html', {'form':form})

        #for a new product
        elif request.method == 'POST':
            form = ListingMainForm(request.POST)
            if form.is_valid():
                print "Listing addition a success"
                form.save(user_id)
                return redirect('user_details:account')
            else:
                print "Listing addition failed"
                return render(request, 'listing/edit-listing.html', {'form':form})

        else:
            form = ListingMainForm()
            return render(request, 'listing/edit-listing.html', {'form':form})

    else:
        request.session['direct_url'] = 'listing:edit-listing'
        response = redirect('user_details:logging')
        return response


def view_listing(request, listing_id):
    print "finding listing"

    return render(request, 'listing/listing.html', {})

def image_upload(request):
    if request.user.is_authenticated():
        user_id = request.user

        if request.method == 'POST':
            #form = ProductImageForm(request.POST, request.FILES)
            #if form.is_valid():
            image = request.FILES['image']
            prod = Listing.objects.get(id=1)
            pi = ListingImage(listing=prod, user=user_id, image=image)
            pi.save()
            print "image upload successful"
            #form.save(request.POST.get('product'))
            return redirect('user_details:account')

        form = ListingImageForm()
        return render (request, 'listing/add-image.html', {'form':form, 'list_id':Listing.objects.get(id=1)})

    else:
        request.session['direct_url'] = 'listing:image-upload'
        response = redirect('user_details:logging')
        return response

def category_tree(request):
    return render(request, "listing/categories.html", {'nodes':CategoryTree.objects.all()})
