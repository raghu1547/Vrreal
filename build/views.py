from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Prop
# Create your views here.
"""
class SiteList(ListView):
    model = Prop
    template_name = 'build/build_list.html'
    """


def search(request):
    prop = Prop.objects.order_by('-date_added')
    # keywords
    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            prop = prop.filter(city__iexact=city)
    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            prop = prop.filter(state__iexact=state)
    # bedrooms
    """
    if 'bedrooms'in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            listings=listings.filter(bedrooms__lte=bedrooms)
    #price
    if 'price'in request.GET:
        price=request.GET['price']
        if price:
            listings=listings.filter(price__lte=price)
    """
    pageCursor = Paginator(prop, 10)
    page = request.GET.get("page")
    try:
        prop_list = pageCursor.page(page)
    except PageNotAnInteger:
        prop_list = pageCursor.page(1)
    except EmptyPage:
        prop_list = pageCursor.page(pageCursor.num_pages)
    context = {'prop_list': prop_list,
               }
    # print(context['request'])
    return render(request, 'build/build_list.html', context)
