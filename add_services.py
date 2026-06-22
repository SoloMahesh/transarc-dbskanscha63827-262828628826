import re

with open('index.html', 'r') as f:
    content = f.read()

# Change the id of Material Science from 'services' to 'materials'
content = content.replace('id="services"', 'id="materials"')

# Make sure the Nav links for Services point to #services (they already do)
# But we need to insert the new Services section. 
# Let's insert it right BEFORE the Material Science section (id="materials")

services_html = """
        <!-- 4. Our Services & Offerings -->
        <section class="py-stack-xl bg-surface" id="services">
            <div class="max-w-container-max mx-auto px-6 md:px-margin-desktop">
                <div class="text-center mb-16 fade-up">
                    <span class="font-label-caps text-label-caps text-secondary uppercase tracking-[0.2em] mb-4 block">Capabilities</span>
                    <h2 class="font-display-lg text-4xl md:text-5xl text-primary mb-6">Comprehensive Structural Solutions.</h2>
                    <p class="max-w-2xl mx-auto font-body-lg text-on-surface-variant">End-to-End fabrication, engineering, and installation across a broad spectrum of architectural requirements.</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <!-- Service 1 -->
                    <div class="group bg-surface-container-low border border-outline-variant/30 p-8 rounded-2xl fade-up hover:shadow-xl hover:border-primary/20 transition-all duration-300">
                        <span class="material-symbols-outlined text-secondary text-4xl mb-6" data-icon="architecture">architecture</span>
                        <h3 class="font-headline-sm text-2xl text-primary mb-3">Tensile Membrane Structures</h3>
                        <p class="font-body-md text-on-surface-variant">Custom design, structural planning, and precise tensioning for large-span canopies, stadiums, and airport terminals.</p>
                    </div>
                    
                    <!-- Service 2 -->
                    <div class="group bg-surface-container-low border border-outline-variant/30 p-8 rounded-2xl fade-up hover:shadow-xl hover:border-primary/20 transition-all duration-300" style="transition-delay: 100ms;">
                        <span class="material-symbols-outlined text-secondary text-4xl mb-6" data-icon="warehouse">warehouse</span>
                        <h3 class="font-headline-sm text-2xl text-primary mb-3">PEB Sheds & Roofing</h3>
                        <p class="font-body-md text-on-surface-variant">Pre-Engineered Building (PEB) steel structures and custom truss works with durable, color-coated GI, PPGI, or FRP sheets.</p>
                    </div>

                    <!-- Service 3 -->
                    <div class="group bg-surface-container-low border border-outline-variant/30 p-8 rounded-2xl fade-up hover:shadow-xl hover:border-primary/20 transition-all duration-300" style="transition-delay: 200ms;">
                        <span class="material-symbols-outlined text-secondary text-4xl mb-6" data-icon="door_front">door_front</span>
                        <h3 class="font-headline-sm text-2xl text-primary mb-3">Modern Gates & Doors</h3>
                        <p class="font-body-md text-on-surface-variant">Elevate your exterior with cohesive design concepts. We blend wood and metal to create striking, luxury main gates and doors.</p>
                    </div>

                    <!-- Service 4 -->
                    <div class="group bg-surface-container-low border border-outline-variant/30 p-8 rounded-2xl fade-up hover:shadow-xl hover:border-primary/20 transition-all duration-300">
                        <span class="material-symbols-outlined text-secondary text-4xl mb-6" data-icon="fence">fence</span>
                        <h3 class="font-headline-sm text-2xl text-primary mb-3">Safety Grills & Railings</h3>
                        <p class="font-body-md text-on-surface-variant">Coordinating balcony railings and front door safety grills to ensure visual harmony across your home's facade while maximizing security.</p>
                    </div>

                    <!-- Service 5 -->
                    <div class="group bg-surface-container-low border border-outline-variant/30 p-8 rounded-2xl fade-up hover:shadow-xl hover:border-primary/20 transition-all duration-300" style="transition-delay: 100ms;">
                        <span class="material-symbols-outlined text-secondary text-4xl mb-6" data-icon="stairs">stairs</span>
                        <h3 class="font-headline-sm text-2xl text-primary mb-3">Spiral Stairs & Ramps</h3>
                        <p class="font-body-md text-on-surface-variant">Space-saving architectural spiral stairs and heavy-duty, weather-resistant iron ramps for commercial and residential access transitions.</p>
                    </div>

                    <!-- Service 6 -->
                    <div class="group bg-surface-container-low border border-outline-variant/30 p-8 rounded-2xl fade-up hover:shadow-xl hover:border-primary/20 transition-all duration-300" style="transition-delay: 200ms;">
                        <span class="material-symbols-outlined text-secondary text-4xl mb-6" data-icon="deck">deck</span>
                        <h3 class="font-headline-sm text-2xl text-primary mb-3">Pergolas & Outdoor Living</h3>
                        <p class="font-body-md text-on-surface-variant">Transform traditional open-lattice garden structures into highly functional, all-weather outdoor living spaces with custom roofing.</p>
                    </div>
                </div>
            </div>
        </section>
"""

# Insert before Material Science section
content = content.replace(
    '<!-- 5. Material Science -->\n        <section class="py-stack-xl bg-primary text-on-primary" id="materials">',
    services_html + '\n        <!-- 5. Material Science -->\n        <section class="py-stack-xl bg-primary text-on-primary" id="materials">'
)

with open('index.html', 'w') as f:
    f.write(content)

