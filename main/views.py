from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from .choices import price_choices, bedroom_choices, state_choices
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages, auth
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import re
from django.db.models import Q,Count
from .models import Listing,ListingRecord,Labourer

@login_required
def index(request):
    listings = Listing.objects.order_by('-due_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
      'listings': paged_listings
       }
    return render(request, 'listings/listings.html', context)



def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('main')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')
          
def listing(request,listing_id):
  print(listing_id)
  current_user = request.user
  print(current_user)
  disp = Labourer.objects.filter(projects__name=listing_id,user=current_user)
  if disp:
    print("...................")
  listing = ListingRecord.objects.filter(title__name=listing_id)

  
  return render(request, 'listings/listing.html',  {'listing': listing,'disp':disp})      


def editrec(request,rec_id):
  print(rec_id)
  if request.method == 'POST':
    category = request.POST.get('category')
    name = request.POST['name']
    date = request.POST['date']
    activities = request.POST['activities']
    method = request.POST['method']
    cost = request.POST['cost']
    photo = request.POST['photo']

    order_items = ListingRecord.objects.all().filter(pk = rec_id)
    
    order_items.update(category=category, name=name, date=date, activities=activities, method=method, cost=cost, photo=photo )
 
    return render(request, 'listings/listing.html')
    

def addrec(request,rec_id):
  if request.method == 'POST':
    category = request.POST.get('category')
    name = request.POST['name']
    date = request.POST['date']
    activities = request.POST['activities']
    method = request.POST['method']
    cost = request.POST['cost']
    photo = request.POST['photo']
