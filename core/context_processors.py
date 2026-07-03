from .models import SiteSettings

def site_settings(request):
    settings = SiteSettings.objects.first()
    if not settings:
        # Create default if it doesn't exist
        settings = SiteSettings.objects.create()
    return {'site': settings}
