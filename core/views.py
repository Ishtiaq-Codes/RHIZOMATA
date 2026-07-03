from django.shortcuts import render
from .models import GalleryImage

def index(request):
    return render(request, 'core/index.html')

def how_to_play(request):
    return render(request, 'core/how_to_play.html')

def preview(request):
    return render(request, 'core/preview.html')

def order(request):
    return render(request, 'core/order.html')

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def gallery(request):
    images = GalleryImage.objects.all().order_by('order', '-created_at')
    return render(request, 'core/gallery.html', {'images': images})

def privacy(request):
    return render(request, 'core/privacy.html')

def terms(request):
    return render(request, 'core/terms.html')
