import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace the broken button classes with a perfect, consistent button
old_button_pattern = r'<button type="button" class="w-full bg-primary text-on-primary font-label-caps uppercase tracking-widest py-4\.5 rounded-xl hover:bg-secondary transition-all duration-300 shadow-lg hover:shadow-secondary/25 mt-4 flex items-center justify-center gap-2 font-bold text-\[13px\]">'
new_button = '<button type="button" class="w-full bg-primary text-on-primary font-label-caps text-label-caps uppercase tracking-[0.2em] py-4 rounded-full hover:bg-secondary transition-all duration-300 shadow-[0_8px_30px_rgba(var(--color-primary),0.3)] hover:shadow-[0_8px_30px_rgba(var(--color-secondary),0.4)] hover:-translate-y-1 mt-4 flex items-center justify-center gap-3">'

content = re.sub(old_button_pattern, new_button, content)

with open('index.html', 'w') as f:
    f.write(content)
