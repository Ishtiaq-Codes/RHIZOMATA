from django.shortcuts import render
from django.views.decorators.cache import cache_page

@cache_page(60 * 60 * 24) # Cache the landing page for 24 hours
def index(request):
    return render(request, 'core/index.html')
