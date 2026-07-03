from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import GalleryImage

@cache_page(60 * 60 * 24)
def index(request):
    return render(request, 'core/index.html')

@cache_page(60 * 60 * 24)
def how_to_play(request):
    return render(request, 'core/how_to_play.html')

@cache_page(60 * 60 * 24)
def preview(request):
    return render(request, 'core/preview.html')

@cache_page(60 * 60 * 24)
def order(request):
    return render(request, 'core/order.html')

@cache_page(60 * 60 * 24)
def contact(request):
    return render(request, 'core/contact.html')

@cache_page(60 * 60 * 24)
def about(request):
    return render(request, 'core/about.html')

def gallery(request):
    images = GalleryImage.objects.all().order_by('order', '-created_at')
    return render(request, 'core/gallery.html', {'images': images})

@cache_page(60 * 60 * 24)
def privacy(request):
    return render(request, 'core/privacy.html')

@cache_page(60 * 60 * 24)
def terms(request):
    return render(request, 'core/terms.html')
