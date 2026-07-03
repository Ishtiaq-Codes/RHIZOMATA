from django.db import models
from django.core.exceptions import ValidationError

class SiteSettings(models.Model):
    # Singleton Model to hold global settings
    
    # Hero Section
    hero_eyebrow = models.CharField(max_length=100, default="A Tabletop Board Game Design Project by Amna Noor")
    hero_title = models.CharField(max_length=100, default="RHIZOMATA")
    hero_subtitle = models.TextField(default="Destiny is not given. It is chosen.\nThe tension is not informational. It is moral.")
    
    # About Section
    about_quote = models.TextField(default="Khudi ko kar buland itna ke har taqdeer se pehle,\nKhuda bande se khud poochhe, bata teri raza kya hai.\n— Allama Muhammad Iqbal")
    about_intro = models.TextField(default="Rhizomata is a tabletop board game built around a single design question: what happens when a player can see the full consequence of every choice before making it?\n\nThe game draws on the elemental philosophy of Empedocles (circa 490-430 BCE), who proposed that all reality is composed of four fundamental roots — fire, water, air, and earth — governed by Love and Strife.\n\nThere are no dice. No hidden reveals. The tension is entirely moral. You define yourself through what you choose.")
    
    # Contact & Social
    contact_email = models.EmailField(default="info@rhizomata.com")
    instagram_url = models.URLField(blank=True, null=True, help_text="Link to your Instagram profile")
    
    # Order Info
    core_set_price = models.DecimalField(max_digits=6, decimal_places=2, default=79.00)
    
    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SiteSettings.objects.exists():
            raise ValidationError('There can be only one SiteSettings instance')
        return super(SiteSettings, self).save(*args, **kwargs)
        
    def __str__(self):
        return "Global Site Settings"


class GalleryImage(models.Model):
    title = models.CharField(max_length=200, help_text="Description for the caption and alt text")
    image = models.ImageField(upload_to='gallery/')
    order = models.PositiveIntegerField(default=0, help_text="Order in which it appears (lower numbers first)")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
        
    def __str__(self):
        return self.title
