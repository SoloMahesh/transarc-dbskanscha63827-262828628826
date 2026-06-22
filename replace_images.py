import re

with open('index.html', 'r') as f:
    content = f.read()

images = [
    'assets/images/img-000.jpg', # Hero
    'assets/images/img-072.jpg', # Ramoji
    'assets/images/img-074.jpg', # HTC
    'assets/images/img-076.jpg', # Tata
    'assets/images/img-031.jpg', # Philosophy
    'assets/images/img-071.jpg', # PTFE
    'assets/images/img-073.jpg', # ETFE
    'assets/images/img-075.jpg', # PVC
    'assets/images/img-000.jpg', # any remaining fallback
]

def repl(match):
    global images
    if images:
        return f"url('{images.pop(0)}')"
    return match.group(0)

new_content = re.sub(r"url\('https://lh3.googleusercontent.com/[^']+'\)", repl, content)

with open('index.html', 'w') as f:
    f.write(new_content)

