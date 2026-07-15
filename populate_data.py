import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rhizomata_project.settings')
django.setup()

from django.core.files import File
from django.conf import settings
from core.models import GameCard, GamePawn, SiteSettings, PreviewImage, GalleryImage

asset_dir = os.path.join(settings.BASE_DIR, 'core', 'static', 'core', 'assets')

def get_file(filename):
    path = os.path.join(asset_dir, filename)
    if os.path.exists(path):
        return File(open(path, 'rb'), name=filename)
    return None

def run():
    print("Populating SiteSettings...")
    site = SiteSettings.objects.first()
    if not site:
        site = SiteSettings.objects.create()
        
    if not site.board_image:
        f = get_file('game board.webp')
        if f: site.board_image = f
    if not site.rulebook_image:
        f = get_file('rulebook.webp')
        if f: site.rulebook_image = f
    site.save()
    
    print("Populating Identity Cards...")
    if GameCard.objects.filter(category='identity').count() == 0:
        elements = ['air', 'earth', 'fire', 'water']
        for elem in elements:
            front_f = get_file(f'identity card front ({elem}).webp')
            back_f = get_file('identity card back.webp')
            card = GameCard.objects.create(name=f'Identity Card - {elem.capitalize()}', category='identity')
            if front_f: card.front_image = front_f
            if back_f: card.back_image = back_f
            card.save()

    print("Populating Situation Cards...")
    if GameCard.objects.filter(category='situation').count() == 0:
        elements = [('air', 'stiuation'), ('earth', 'situation'), ('fire', 'situation'), ('water', 'situation')] # Note typo in air file name
        for elem, typo in elements:
            front_f = get_file(f'{elem} {typo} card front.webp')
            back_f = get_file(f'{elem} situation card back.webp')
            card = GameCard.objects.create(name=f'Situation Card - {elem.capitalize()}', category='situation')
            if front_f: card.front_image = front_f
            if back_f: card.back_image = back_f
            card.save()
            
    print("Populating Context Cards...")
    if GameCard.objects.filter(category='context').count() == 0:
        front_f = get_file('context card front.webp')
        back_f = get_file('context card back.webp')
        card = GameCard.objects.create(name='Context Card', category='context')
        if front_f: card.front_image = front_f
        if back_f: card.back_image = back_f
        card.save()
        
    print("Populating Game Pawns...")
    if GamePawn.objects.count() == 0:
        amb = GamePawn.objects.create(name='Ambition', title_color_class='text-orange-400', glow_color='rgba(209,104,52,0.3)')
        amb_f = get_file('ambition_pawn.webp')
        if amb_f: amb.image = amb_f
        amb.save()
        
        stab = GamePawn.objects.create(name='Stability', title_color_class='text-blue-400', glow_color='rgba(59,130,246,0.3)')
        stab_f = get_file('stability_pawn.webp')
        if stab_f: stab.image = stab_f
        stab.save()
        
    print("Populating Preview Images & Gallery...")
    
    # We will list out everything in assets that ends with .webp to add them
    all_files = [
        'game board.webp',
        'identity card back.webp',
        'identity card front (air).webp',
        'identity card front (earth).webp',
        'identity card front (fire).webp',
        'identity card front (water).webp',
        'fire situation card front.webp',
        'water situation card front.webp',
        'earth situation card front.webp',
        'air stiuation card front.webp', # typo in file name
        'fire situation card back.webp',
        'water situation card back.webp',
        'earth situation card back.webp',
        'air situation card back.webp',
        'context card front.webp',
        'context card back.webp',
    ]
    
    if PreviewImage.objects.count() == 0:
        for i, fname in enumerate(all_files):
            p = PreviewImage.objects.create(title=fname.replace('.webp', '').replace('_', ' ').title(), order=i)
            p_f = get_file(fname)
            if p_f: p.image = p_f
            p.save()
            
    if GalleryImage.objects.count() == 0:
        for i, fname in enumerate(all_files):
            g = GalleryImage.objects.create(title=fname.replace('.webp', '').replace('_', ' ').title(), order=i)
            g_f = get_file(fname)
            if g_f: g.image = g_f
            g.save()
        
    print("Data Migration Complete!")

if __name__ == "__main__":
    run()
