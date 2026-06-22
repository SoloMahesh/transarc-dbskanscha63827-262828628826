import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Fix Mobile Header Spacing (add w-full to the inner div)
content = content.replace(
    'class="flex justify-between items-center px-margin-desktop h-[80px] max-w-container-max mx-auto px-6 md:px-margin-desktop"',
    'class="flex justify-between items-center w-full h-[80px] max-w-container-max mx-auto px-6 md:px-margin-desktop"'
)

# 2. Fix 'View All' Link
# Find the exact View All anchor tag and replace its href.
content = re.sub(
    r'<a[^>]*?href="[^"]*"[^>]*?>\s*View All \s*<span[^>]*?>arrow_forward</span>\s*</a>',
    r'<a href="#real-time-gallery" class="font-label-caps text-label-caps uppercase tracking-[0.1em] text-primary hover:text-secondary transition-colors flex items-center gap-2">View All <span class="material-symbols-outlined text-sm">arrow_forward</span></a>',
    content
)
# Add the ID 'real-time-gallery' to the gallery heading area so it scrolls there
content = content.replace(
    '<div class="text-center mb-10 mt-20 fade-up">',
    '<div class="text-center mb-10 mt-20 fade-up" id="real-time-gallery">'
)

# 3. Restructure Gallery Images for perfect alignment (replace h-auto with fixed aspect ratio/height and object-cover)
content = content.replace(
    'class="w-full h-auto hover:scale-105 transition-transform duration-500"',
    'class="w-full h-64 object-cover hover:scale-105 transition-transform duration-500"'
)

# 4. Remove Contact Form completely
# The form starts with <form class="space-y-6 pt-6 border-t border-outline-variant/20"> and ends with </form>
content = re.sub(r'<form class="space-y-6 pt-6 border-t border-outline-variant/20">.*?</form>', '', content, flags=re.DOTALL)

# 5. Fix Location Mark on Map
content = re.sub(
    r'src="https://www\.google\.com/maps/embed\?pb=[^"]+"',
    r'src="https://maps.google.com/maps?q=Manjeera+Trinity+Corporate,+KPHB+Phase+3,+Kukatpally,+Hyderabad&t=&z=15&ie=UTF8&iwloc=&output=embed"',
    content
)

with open('index.html', 'w') as f:
    f.write(content)
