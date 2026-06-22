import os

base_dir = "assets/images/client"

renames = {
    "1.jpeg": "project-temple-walkway.jpeg",
    "2.jpeg": "project-conical-entrance.jpeg",
    "new t1.jpeg": "project-stage-arch-1.jpeg",
    "new ten2.jpeg": "project-building-conical.jpeg",
    "WhatsApp Image 2026-05-14 at 2.05.33 PM (1).jpeg": "project-scalloped-shell.jpeg",
    "WhatsApp Image 2026-05-14 at 2.05.36 PM (1).jpeg": "project-stage-arch-2.jpeg",
    "WhatsApp Image 2026-05-16 at 10.22.32 PM.jpeg": "project-night-arch.jpeg",
    "WhatsApp Image 2026-05-16 at 10.22.35 PM.jpeg": "project-night-conical.jpeg",
    "WhatsApp Image 2026-05-16 at 10.31.53 PM.jpeg": "project-multibay-parking-1.jpeg",
    "WhatsApp Image 2026-05-16 at 10.31.55 PM (1).jpeg": "project-multibay-framework.jpeg",
    "WhatsApp Image 2026-05-16 at 10.31.55 PM.jpeg": "project-rooftop-conical.jpeg",
    "WhatsApp Image 2026-05-16 at 10.31.57 PM.jpeg": "project-driveway-cantilever.jpeg",
    "WhatsApp Image 2026-05-16 at 10.32.15 PM (2).jpeg": "project-garden-arch-frame.jpeg",
    "WhatsApp Image 2026-05-16 at 10.32.16 PM.jpeg": "project-street-shade.jpeg",
}

for old_name, new_name in renames.items():
    old_path = os.path.join(base_dir, old_name)
    new_path = os.path.join(base_dir, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)

# For any remaining WhatsApp images, give them generic descriptive numbers
count = 1
for filename in os.listdir(base_dir):
    if filename.startswith("WhatsApp Image"):
        old_path = os.path.join(base_dir, filename)
        new_path = os.path.join(base_dir, f"project-installation-view-{count}.jpeg")
        os.rename(old_path, new_path)
        count += 1

