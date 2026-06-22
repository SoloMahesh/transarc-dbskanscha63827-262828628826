import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update Header CTA
content = content.replace(
    '''<a href="#contact" class="hidden md:block bg-primary text-on-primary font-label-caps text-label-caps uppercase tracking-[0.2em] px-8 py-3 rounded-full hover:bg-secondary transition-colors duration-300 text-center">
                Consultation
            </a>''',
    '''<a href="#contact" class="hidden md:block bg-primary text-on-primary font-label-caps text-label-caps uppercase tracking-[0.2em] px-8 py-3 rounded-full hover:bg-secondary transition-colors duration-300 text-center">
                Get a Free Estimate
            </a>'''
)

# 2. Update Hero CTA
content = content.replace(
    '''<a href="#contact" class="border border-on-primary text-on-primary font-label-caps text-label-caps uppercase tracking-[0.2em] px-10 py-4 rounded-full hover:bg-on-primary hover:text-primary transition-all duration-300">
                    Schedule Consultation
                </a>''',
    '''<a href="#contact" class="border border-on-primary text-on-primary font-label-caps text-label-caps uppercase tracking-[0.2em] px-10 py-4 rounded-full hover:bg-on-primary hover:text-primary transition-all duration-300">
                    Request Project Quote
                </a>'''
)

# 3. Replace the entire #contact section
contact_regex = r'<!-- 6\. Contact & Maps Integration -->\s*<section class="py-stack-xl bg-surface border-t border-technical" id="contact">.*?</section>'

new_contact = """<!-- 6. Contact & Maps Integration -->
        <section class="py-stack-xl bg-surface border-t border-technical" id="contact">
            <div class="max-w-container-max mx-auto px-6 md:px-margin-desktop grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16">
                
                <!-- Left Side: Trust & Info -->
                <div class="lg:col-span-7 fade-up flex flex-col justify-center">
                    <span class="font-label-caps text-label-caps text-secondary uppercase tracking-[0.2em] mb-4 block">Request A Quote</span>
                    <h2 class="font-display-lg text-4xl md:text-5xl text-primary mb-6">Let's Build The Next Landmark.</h2>
                    <p class="font-body-lg text-body-lg text-on-surface-variant mb-10 max-w-xl">
                        Get a free engineering assessment and transparent pricing for your project. Our experts respond within 2 hours.
                    </p>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-10">
                        <div class="flex items-start gap-4">
                            <span class="material-symbols-outlined text-secondary text-2xl" data-icon="location_on">location_on</span>
                            <p class="font-body-md text-on-surface-variant">#:12A02B, 13th Floor, Manjeera Trinity Corporate,<br/>JNTU-Hitech City Road, KPHB Phase 3,<br/>Kukatpally, Hyderabad.</p>
                        </div>
                        <div class="flex flex-col gap-5">
                            <div class="flex items-start gap-4">
                                <span class="material-symbols-outlined text-secondary text-2xl" data-icon="call">call</span>
                                <div class="font-body-md text-on-surface-variant flex flex-col gap-1">
                                    <a href="tel:+918978657768" class="hover:text-primary transition-colors font-medium">+91 89786-57768</a>
                                    <a href="tel:+919666614700" class="hover:text-primary transition-colors font-medium">+91 96666-14700</a>
                                </div>
                            </div>
                            <div class="flex items-start gap-4">
                                <span class="material-symbols-outlined text-secondary text-2xl" data-icon="mail">mail</span>
                                <a href="mailto:info.tensarc@gmail.com" class="font-body-md text-on-surface-variant hover:text-primary transition-colors font-medium">info.tensarc@gmail.com</a>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Trusted By Strip inside Contact -->
                    <div class="border-t border-outline-variant/20 pt-8 mb-10">
                        <p class="font-label-caps text-xs text-on-surface-variant mb-6 uppercase tracking-widest font-bold">Trusted by Industry Leaders</p>
                        <div class="flex flex-wrap items-center gap-6 md:gap-10 opacity-70 grayscale">
                            <span class="font-display-md text-xl md:text-2xl text-primary font-bold tracking-tight">RAMOJI <span class="font-normal text-on-surface-variant">FILM CITY</span></span>
                            <span class="font-display-md text-xl md:text-2xl text-primary font-bold tracking-tight">TATA <span class="font-normal text-on-surface-variant">ADVANCED</span></span>
                            <span class="font-display-md text-xl md:text-2xl text-primary font-bold tracking-tight">HTC <span class="font-normal text-on-surface-variant">GLOBAL</span></span>
                        </div>
                    </div>

                    <div class="h-[200px] w-full rounded-2xl overflow-hidden shadow-inner border border-outline-variant/20">
                        <iframe 
                            src="https://maps.google.com/maps?q=Manjeera+Trinity+Corporate,+KPHB+Phase+3,+Kukatpally,+Hyderabad&t=&z=15&ie=UTF8&iwloc=&output=embed" 
                            width="100%" 
                            height="100%" 
                            style="border:0;" 
                            allowfullscreen="" 
                            loading="lazy">
                        </iframe>
                    </div>
                </div>
                
                <!-- Right Side: Lead Capture Form -->
                <div class="lg:col-span-5 fade-up" style="transition-delay: 100ms;">
                    <div class="bg-surface-container-low border border-outline-variant/30 rounded-3xl p-8 shadow-[0_20px_50px_rgba(0,0,0,0.1)] dark:shadow-[0_20px_50px_rgba(0,0,0,0.5)] relative overflow-hidden h-full flex flex-col justify-center">
                        <!-- Decorative glow -->
                        <div class="absolute top-0 right-0 w-64 h-64 bg-secondary/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2 pointer-events-none"></div>
                        
                        <h3 class="font-headline-sm text-3xl text-primary mb-3 relative z-10">Get Your Estimate</h3>
                        <p class="font-body-md text-on-surface-variant mb-8 relative z-10">Fill out the details below and an engineer will contact you shortly.</p>
                        
                        <form class="space-y-6 relative z-10">
                            <div>
                                <label class="block font-label-caps text-xs text-primary uppercase tracking-widest mb-2 font-bold">Full Name</label>
                                <input type="text" placeholder="John Doe" class="w-full bg-surface border border-outline-variant/50 rounded-xl px-4 py-3.5 text-primary placeholder-on-surface-variant/50 focus:outline-none focus:border-secondary focus:ring-1 focus:ring-secondary transition-all">
                            </div>
                            <div>
                                <label class="block font-label-caps text-xs text-primary uppercase tracking-widest mb-2 font-bold">Phone Number *</label>
                                <input type="tel" placeholder="+91 90000 00000" class="w-full bg-surface border border-outline-variant/50 rounded-xl px-4 py-3.5 text-primary placeholder-on-surface-variant/50 focus:outline-none focus:border-secondary focus:ring-1 focus:ring-secondary transition-all">
                            </div>
                            <div class="grid grid-cols-2 gap-4">
                                <div>
                                    <label class="block font-label-caps text-xs text-primary uppercase tracking-widest mb-2 font-bold">Project Type</label>
                                    <select class="w-full bg-surface border border-outline-variant/50 rounded-xl px-4 py-3.5 text-primary focus:outline-none focus:border-secondary transition-all">
                                        <option>Tensile Canopy</option>
                                        <option>PEB Shed / Roof</option>
                                        <option>Main Gates</option>
                                        <option>Pergola</option>
                                        <option>Other</option>
                                    </select>
                                </div>
                                <div>
                                    <label class="block font-label-caps text-xs text-primary uppercase tracking-widest mb-2 font-bold">Approx. Area</label>
                                    <input type="text" placeholder="e.g. 5000 sqft" class="w-full bg-surface border border-outline-variant/50 rounded-xl px-4 py-3.5 text-primary placeholder-on-surface-variant/50 focus:outline-none focus:border-secondary transition-all">
                                </div>
                            </div>
                            <div>
                                <label class="block font-label-caps text-xs text-primary uppercase tracking-widest mb-2 font-bold">Message (Optional)</label>
                                <textarea placeholder="Tell us about your requirements..." rows="3" class="w-full bg-surface border border-outline-variant/50 rounded-xl px-4 py-3.5 text-primary placeholder-on-surface-variant/50 focus:outline-none focus:border-secondary transition-all resize-none"></textarea>
                            </div>
                            <button type="button" class="w-full bg-primary text-on-primary font-label-caps uppercase tracking-widest py-4.5 rounded-xl hover:bg-secondary transition-all duration-300 shadow-lg hover:shadow-secondary/25 mt-4 flex items-center justify-center gap-2 font-bold text-[13px]">
                                Request Estimate <span class="material-symbols-outlined text-sm">arrow_forward</span>
                            </button>
                            <p class="text-center font-body-sm text-xs text-on-surface-variant/80 mt-4">🔒 Your information is 100% secure.</p>
                        </form>
                    </div>
                </div>
            </div>
        </section>"""

content = re.sub(contact_regex, new_contact, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)

