from django.shortcuts import render
from .models import GalleryImage, GameCard, GamePawn, PreviewImage

def index(request):
    identity_cards = GameCard.objects.filter(category='identity')
    situation_cards = GameCard.objects.filter(category='situation')
    context_cards = GameCard.objects.filter(category='context')
    pawns = GamePawn.objects.all()
    
    return render(request, 'core/index.html', {
        'identity_cards': identity_cards,
        'situation_cards': situation_cards,
        'context_cards': context_cards,
        'pawns': pawns
    })

def how_to_play(request):
    return render(request, 'core/how_to_play.html')

def preview(request):
    preview_images = PreviewImage.objects.all()
    pawns = GamePawn.objects.all()
    return render(request, 'core/preview.html', {'preview_images': preview_images, 'pawns': pawns})

def order(request):
    return render(request, 'core/order.html')

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'core/gallery.html', {'images': images})

def privacy(request):
    return render(request, 'core/privacy.html')

def terms(request):
    return render(request, 'core/terms.html')
