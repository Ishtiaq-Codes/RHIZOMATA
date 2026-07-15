from django.db import models
from django.core.exceptions import ValidationError

class SiteSettings(models.Model):
    # Singleton Model to hold global settings
    
    # Hero Section
    hero_eyebrow = models.CharField(max_length=100, default="A Tabletop Board Game Design by Amna Noor")
    hero_title = models.CharField(max_length=100, default="RHIZOMATA")
    hero_subtitle = models.TextField(default="Destiny is not given. It is chosen.\nThe tension is not informational. It is moral.")
    
    # Concept / Philosophy Section
    concept_label = models.CharField(max_length=100, default="The Philosophy")
    concept_title = models.CharField(max_length=200, default="Destiny is not given.<br /><span class=\"gradient-text\">It is chosen.</span>")
    concept_text_1 = models.TextField(default="Most games use chance - dice, card draws, random events - as the primary engine of excitement. <strong>Rhizomata</strong> proposes a different approach: <strong>all consequences are visible before every choice is made.</strong>")
    concept_text_2 = models.TextField(default="There are no hidden reveals, no dice, no luck in the result of any decision. The tension is not informational. It is moral. Every person is a hostage to what they have earned.")
    concept_author = models.CharField(max_length=100, default="— Created by Amna Noor")
    
    # Stats Section
    stat_1_number = models.CharField(max_length=10, default="102")
    stat_1_label = models.CharField(max_length=50, default="Unique Cards")
    stat_2_number = models.CharField(max_length=10, default="4")
    stat_2_label = models.CharField(max_length=50, default="Elemental Realms")
    stat_3_number = models.CharField(max_length=10, default="4")
    stat_3_label = models.CharField(max_length=50, default="Max Players")
    stat_4_number = models.CharField(max_length=50, default='<span data-count="60" id="stat-time-num">60</span><span style="font-size:0.55em;opacity:0.7;">-90</span>')
    stat_4_label = models.CharField(max_length=50, default="Minutes of Play")

    # Identity Section
    identity_label = models.CharField(max_length=100, default="The Elements")
    identity_title = models.CharField(max_length=200, default="Identity <span class=\"gradient-text\">Cards</span>")
    identity_text = models.TextField(default="In classical philosophy, your element is assigned at birth — fixed, inherited, and beyond your control. Rhizomata challenges this. The element is dealt randomly at the start of the game, but what you do with it is entirely a matter of choice. It is a starting condition, not a sentence.<br><br><span style=\"color: var(--accent); font-style: italic;\">Click a card to reveal its true identity.</span>")
    
    # Situation Section
    situation_label = models.CharField(max_length=100, default="The Dilemmas")
    situation_title = models.CharField(max_length=200, default="Situation <span class=\"gradient-text\">Cards</span>")
    situation_text = models.TextField(default="The tension between who we want to be and who we actually become in moments of pressure is the core of the game. You will face 60 unique moral decisions. Both options display their full consequences before you decide. No dice. No luck. <br><br><span style=\"color: var(--accent); font-style: italic;\">Click to face your fate.</span>")
    
    # Context Section
    context_label = models.CharField(max_length=100, default="The Variables")
    context_title = models.CharField(max_length=200, default="Context <span class=\"gradient-text\">Cards</span>")
    context_text = models.TextField(default="But choices are rarely made in a vacuum. The Context Cards shift the environment, forcing players to adapt to external pressures beyond their control. A decision that seemed easy in times of peace becomes devastating during a famine or a plague.")
    
    # Pawns Section
    pawns_label = models.CharField(max_length=100, default="The Duality")
    pawns_title = models.CharField(max_length=200, default="The <span class=\"gradient-text\">Pawns</span>")
    pawns_text = models.TextField(default="Every player controls two interconnected pawns, representing the fundamental duality of human nature: Ambition and Stability. One reaches for greatness at great cost. The other seeks security, but risks stagnation.")

    # Board Game Section
    board_label = models.CharField(max_length=100, default="The Arena")
    board_title = models.CharField(max_length=200, default="The <span class=\"gradient-text\">Board</span>")
    board_text = models.TextField(default="The game board is a cyclical track representing the life cycle of a civilization, moving from the Golden Age to the Iron Age. As the eras change, the fundamental rules of survival shift with them.")
    board_image = models.ImageField(upload_to='settings/', blank=True, null=True)

    # How To Play Page
    how_to_play_label = models.CharField(max_length=100, default="Rules of the Realm")
    how_to_play_title = models.CharField(max_length=200, default="How to Play")
    rulebook_image = models.ImageField(upload_to='settings/', blank=True, null=True)
    rule_1_title = models.CharField(max_length=200, default="1. The Dual-Self")
    rule_1_text = models.TextField(default="You control two pawns simultaneously. The <strong>Stability Pawn</strong> moves ahead for grounded, restrained choices. The <strong>Ambition Pawn</strong> moves ahead for bold, risky decisions.")
    rule_2_title = models.CharField(max_length=200, default="2. Visible Consequences")
    rule_2_text = models.TextField(default="There are no dice. Every Situation Card and Context Card shows the <em>exact consequences</em> of both options before you choose. The tension is not informational—it is moral.")
    rule_3_title = models.CharField(max_length=200, default="3. The Token Economy")
    rule_3_text = models.TextField(default="Your choices reward you with Balance or Pressure tokens. These tokens are a permanent record of the kind of actions you took. Choose wisely; they cannot be undone.")
    conclusion_title = models.CharField(max_length=200, default="No Winners, No Losers")
    conclusion_text = models.TextField(default="Rhizomata does not end with a score. After tallying your tokens and pawn positions across the two-axis matrix, the game ends with the <strong>Archetype Reveal</strong>.")
    sub_conclusion_text = models.TextField(default="You leave the table with a character, not a number: <em>The Sage, The Guardian, The Wanderer, The Rebel,</em> or <em>The Opportunist</em>. The game does not judge you; it simply reflects the record of your own choices.")

    # About Section
    about_quote = models.TextField(default="Khudi ko kar buland itna ke har taqdeer se pehle,\nKhuda bande se khud poochhe, bata teri raza kya hai.\n— Allama Muhammad Iqbal")
    about_intro = models.TextField(default="Rhizomata is a tabletop board game built around a single design question: what happens when a player can see the full consequence of every choice before making it?\n\nThe game draws on the elemental philosophy of Empedocles (circa 490-430 BCE), who proposed that all reality is composed of four fundamental roots — fire, water, air, and earth — governed by Love and Strife.\n\nThere are no dice. No hidden reveals. The tension is entirely moral. You define yourself through what you choose.")
    
    # Contact & Social
    contact_email = models.EmailField(default="info@rhizomata.net")
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


class GameCard(models.Model):
    CATEGORY_CHOICES = (
        ('identity', 'Identity Card'),
        ('situation', 'Situation Card'),
        ('context', 'Context Card'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    front_image = models.ImageField(upload_to='cards/')
    back_image = models.ImageField(upload_to='cards/')
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order']
        
    def __str__(self):
        return f"{self.get_category_display()} - {self.name}"

class GamePawn(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pawns/')
    title_color_class = models.CharField(max_length=50, default="text-orange-400")
    glow_color = models.CharField(max_length=50, default="rgba(209,104,52,0.15)")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return self.name

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

class PreviewImage(models.Model):
    title = models.CharField(max_length=200, help_text="Title or description of the preview")
    image = models.ImageField(upload_to='previews/')
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return self.title
