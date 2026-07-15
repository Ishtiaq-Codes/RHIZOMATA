from django.contrib import admin
from .models import SiteSettings, GalleryImage, GameCard, GamePawn, PreviewImage

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Home - Hero Section', {
            'fields': ('hero_eyebrow', 'hero_title', 'hero_subtitle')
        }),
        ('Home - Philosophy Section', {
            'fields': ('concept_label', 'concept_title', 'concept_text_1', 'concept_text_2', 'concept_author')
        }),
        ('Home - Stats Section', {
            'fields': (('stat_1_number', 'stat_1_label'), ('stat_2_number', 'stat_2_label'), 
                       ('stat_3_number', 'stat_3_label'), ('stat_4_number', 'stat_4_label'))
        }),
        ('Home - Identity Cards Section', {
            'fields': ('identity_label', 'identity_title', 'identity_text')
        }),
        ('Home - Situation Cards Section', {
            'fields': ('situation_label', 'situation_title', 'situation_text')
        }),
        ('Home - Context Cards Section', {
            'fields': ('context_label', 'context_title', 'context_text')
        }),
        ('Home - Pawns Section', {
            'fields': ('pawns_label', 'pawns_title', 'pawns_text')
        }),
        ('Home - Board Game Section', {
            'fields': ('board_label', 'board_title', 'board_text', 'board_image')
        }),
        ('How To Play Page', {
            'fields': ('how_to_play_label', 'how_to_play_title', 'rulebook_image',
                       'rule_1_title', 'rule_1_text', 
                       'rule_2_title', 'rule_2_text', 
                       'rule_3_title', 'rule_3_text',
                       'conclusion_title', 'conclusion_text', 'sub_conclusion_text')
        }),
        ('About Page', {
            'fields': ('about_quote', 'about_intro')
        }),
        ('Contact & Order Info', {
            'fields': ('contact_email', 'instagram_url', 'core_set_price')
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(GameCard)
class GameCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order')
    list_filter = ('category',)
    list_editable = ('order',)
    search_fields = ('name',)

@admin.register(GamePawn)
class GamePawnAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at')
    list_editable = ('order',)
    search_fields = ('title',)

@admin.register(PreviewImage)
class PreviewImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
