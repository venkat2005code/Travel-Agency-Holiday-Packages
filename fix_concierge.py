import re

with open('contact.html', 'r') as f:
    content = f.read()

old_html_pattern = re.compile(r'<!-- 1\. Hero — Minimal Luxury -->.*?</section>', re.DOTALL)

new_html = """<!-- 1. Hero — Minimal Luxury -->
<section class="relative h-[80vh] min-h-[600px] flex items-center justify-center pt-24 overflow-hidden">
<!-- Floating Imagery (Absolute) -->
<div class="absolute top-20 md:top-32 left-4 md:left-12 lg:left-24 w-32 md:w-56 lg:w-64 h-48 md:h-72 lg:h-80 rounded-[2rem] overflow-hidden shadow-2xl animate-float-1 z-0 hidden sm:block">
<img class="w-full h-full object-cover" src="assets/bf2d3c11-44f6-43f9-abae-a453a858c5ed.jpeg"/>
</div>
<div class="absolute bottom-16 md:bottom-24 right-4 md:right-12 lg:right-24 w-36 md:w-64 lg:w-72 h-36 md:h-64 lg:h-72 rounded-full overflow-hidden shadow-2xl animate-float-2 z-0 hidden sm:block">
<img class="w-full h-full object-cover" src="assets/d729e81c-1c0a-428f-8c66-a38b28ee5568.jpeg"/>
</div>
<!-- Central Typography -->
<div class="relative z-10 text-center px-8 py-12 md:py-16 md:px-16 max-w-3xl mx-auto bg-white/70 dark:bg-gray-900/70 backdrop-blur-xl rounded-[3rem] shadow-[0_20px_60px_rgba(0,0,0,0.05)] dark:shadow-[0_20px_60px_rgba(255,255,255,0.02)] border border-white/50 dark:border-white/10 mx-6 sm:mx-auto">
<span class="text-accent font-bold tracking-widest uppercase text-sm block mb-4">Concierge Support</span>
<h1 class="text-5xl md:text-6xl lg:text-7xl font-serif font-bold text-brand-900 dark:text-white leading-tight">
                    How can we<br/>assist you?
                </h1>
<p class="mt-6 text-lg md:text-xl text-gray-600 dark:text-gray-300 max-w-lg mx-auto">
                    Whether you are planning a new journey or need assistance while abroad, our global team is available 24/7.
                </p>
<div class="mt-10">
    <a href="#" class="inline-block bg-brand-900 dark:bg-white text-white dark:text-brand-900 font-bold px-8 py-4 rounded-full hover:bg-accent dark:hover:bg-accent hover:text-brand-900 transition-colors shadow-lg hover:shadow-xl transform hover:-translate-y-1">Contact Concierge</a>
</div>
</div>
</section>"""

content = old_html_pattern.sub(new_html, content)

with open('contact.html', 'w') as f:
    f.write(content)

print("Done")
