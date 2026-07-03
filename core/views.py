from django.shortcuts import render

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
    return render(request, 'core/gallery.html')
