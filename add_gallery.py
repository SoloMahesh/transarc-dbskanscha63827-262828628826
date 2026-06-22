import re

with open('index.html', 'r') as f:
    content = f.read()

gallery_html = """
                <!-- Real-time Site Installations -->
                <div class="text-center mb-10 mt-20 fade-up">
                    <span class="font-label-caps text-label-caps text-on-surface-variant uppercase tracking-[0.2em] mb-4 block">Real-time Progress & Installations</span>
                    <h3 class="font-display-md text-3xl text-primary mb-6">Our Work In Action</h3>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 pb-10">
                    <div class="flex flex-col gap-4">
                        <div class="overflow-hidden rounded-xl border border-outline-variant/20 shadow-sm fade-up">
                            <img src="assets/images/client/project-scalloped-shell.jpeg" alt="Scalloped Shell Canopy" class="w-full h-auto hover:scale-105 transition-transform duration-500">
                        </div>
                        <div class="overflow-hidden rounded-xl border border-outline-variant/20 shadow-sm fade-up">
                            <img src="assets/images/client/project-temple-walkway.jpeg" alt="Temple Walkway Canopy" class="w-full h-auto hover:scale-105 transition-transform duration-500">
                        </div>
                    </div>
                    <div class="flex flex-col gap-4">
                        <div class="overflow-hidden rounded-xl border border-outline-variant/20 shadow-sm fade-up">
                            <img src="assets/images/client/project-stage-arch-1.jpeg" alt="Stage Arch Canopy" class="w-full h-auto hover:scale-105 transition-transform duration-500">
                        </div>
                        <div class="overflow-hidden rounded-xl border border-outline-variant/20 shadow-sm fade-up">
                            <img src="assets/images/client/project-rooftop-conical.jpeg" alt="Rooftop Conical Canopy" class="w-full h-auto hover:scale-105 transition-transform duration-500">
                        </div>
                    </div>
                    <div class="flex flex-col gap-4">
                        <div class="overflow-hidden rounded-xl border border-outline-variant/20 shadow-sm fade-up">
                            <img src="assets/images/client/project-night-arch.jpeg" alt="Illuminated Night Canopy" class="w-full h-auto hover:scale-105 transition-transform duration-500">
                        </div>
                        <div class="overflow-hidden rounded-xl border border-outline-variant/20 shadow-sm fade-up">
                            <img src="assets/images/client/project-driveway-cantilever.jpeg" alt="Cantilever Driveway Canopy" class="w-full h-auto hover:scale-105 transition-transform duration-500">
                        </div>
                    </div>
                    <div class="flex flex-col gap-4">
                        <div class="overflow-hidden rounded-xl border border-outline-variant/20 shadow-sm fade-up">
                            <img src="assets/images/client/project-multibay-parking-1.jpeg" alt="Multi-bay Parking Structure" class="w-full h-auto hover:scale-105 transition-transform duration-500">
                        </div>
                        <div class="overflow-hidden rounded-xl border border-outline-variant/20 shadow-sm fade-up">
                            <img src="assets/images/client/project-conical-entrance.jpeg" alt="Conical Entrance Canopy" class="w-full h-auto hover:scale-105 transition-transform duration-500">
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

# Replace the closing tags of the projects section
new_content = re.sub(r'(\s+)</div>\s*</section>\s*<!-- 6\. Contact & Maps Integration -->', r'\1' + gallery_html + r'\n        <!-- 6. Contact & Maps Integration -->', content)

with open('index.html', 'w') as f:
    f.write(new_content)
