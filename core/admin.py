from django.contrib import admin
from .models import SiteSettings, GalleryImage

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Prevent adding multiple instances
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at')
    list_editable = ('order',)
    search_fields = ('title',)
