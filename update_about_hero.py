import re

with open('about.html', 'r') as f:
    content = f.read()

# Match the entire hero section
# The old hero section starts at <!-- 1. Hero — Glassmorphism --> and ends before <!-- 2. Our Journey — Curved Timeline -->

pattern = re.compile(r'<!-- 1\. Hero — Glassmorphism -->.*?<!-- 2\. Our Journey — Curved Timeline -->', re.DOTALL)

new_hero = """<!-- 1. Hero — Editorial Layout -->
<section class="relative min-h-[90vh] flex items-center justify-center overflow-hidden bg-[#F9F9F8] dark:bg-gray-900 pt-28 pb-16 lg:py-0">
<!-- Abstract Graphic Map Pattern -->
<div class="absolute inset-0 opacity-[0.03] dark:opacity-5 z-0" style="background-image: radial-gradient(#000 1px, transparent 1px); background-size: 40px 40px;"></div>

<div class="max-w-7xl mx-auto px-6 relative z-10 w-full h-full flex flex-col lg:flex-row items-center gap-12 lg:gap-20">
    <!-- Left Column: Typography & Content -->
    <div class="w-full lg:w-1/2 flex flex-col items-start text-left order-2 lg:order-1 relative z-20">
        <span class="text-accent font-bold tracking-widest uppercase text-sm mb-4 inline-flex items-center gap-2">
            <span class="w-8 h-[2px] bg-accent"></span> Our Heritage
        </span>
        <h1 class="text-5xl md:text-6xl lg:text-7xl font-serif font-bold text-brand-900 dark:text-white leading-[1.1] mb-6">
            Pioneering the modern expedition.
        </h1>
        <p class="text-xl md:text-2xl text-gray-700 dark:text-gray-300 mb-8 max-w-xl font-light">
            We don't just book trips. We curate transformative experiences for the world's most discerning travelers.
        </p>
        
        <!-- Primary CTA -->
        <a href="destinations.html" class="inline-flex items-center gap-3 px-8 py-4 bg-brand-900 dark:bg-white text-white dark:text-brand-900 font-bold rounded-full hover:shadow-2xl hover:scale-105 transition-all mb-12 lg:mb-16 group">
            Plan Your Journey
            <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
        </a>

        <!-- Supporting Statistics -->
        <div class="grid grid-cols-3 gap-4 sm:gap-6 w-full border-t border-gray-200 dark:border-gray-800 pt-8">
            <div class="flex flex-col">
                <span class="text-3xl md:text-4xl font-black text-brand-900 dark:text-white mb-1">15+</span>
                <span class="text-[10px] sm:text-xs text-gray-500 uppercase tracking-widest font-bold">Years<br class="sm:hidden"> Experience</span>
            </div>
            <div class="flex flex-col">
                <span class="text-3xl md:text-4xl font-black text-brand-900 dark:text-white mb-1">50+</span>
                <span class="text-[10px] sm:text-xs text-gray-500 uppercase tracking-widest font-bold">Countries<br class="sm:hidden"> Covered</span>
            </div>
            <div class="flex flex-col">
                <span class="text-3xl md:text-4xl font-black text-brand-900 dark:text-white mb-1">10k+</span>
                <span class="text-[10px] sm:text-xs text-gray-500 uppercase tracking-widest font-bold">Happy<br class="sm:hidden"> Travelers</span>
            </div>
        </div>
    </div>

    <!-- Right Column: Editorial Visual -->
    <div class="w-full lg:w-1/2 order-1 lg:order-2 relative mt-8 lg:mt-0">
        <!-- Abstract Background Blobs behind image -->
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-[120%] bg-blue-400/20 rounded-full mix-blend-multiply filter blur-[100px] animate-blob"></div>
        <div class="absolute top-1/2 right-0 -translate-y-1/2 w-3/4 h-[120%] bg-accent/20 rounded-full mix-blend-multiply filter blur-[100px] animate-blob animation-delay-2000"></div>
        
        <!-- Image Container with offset framing -->
        <div class="relative w-full aspect-[4/5] md:aspect-square lg:aspect-[4/5] rounded-[2rem] md:rounded-[3rem] overflow-hidden shadow-2xl">
            <!-- Using the existing image asset -->
            <img src="assets/hero_about_1784697342278.png" alt="Travelers on an expedition" class="w-full h-full object-cover transform hover:scale-105 transition-transform duration-700">
            
            <!-- Glass Overlay Play Button -->
            <div class="absolute bottom-6 left-6 right-6 p-4 sm:p-6 bg-white/20 dark:bg-gray-900/40 backdrop-blur-md rounded-3xl border border-white/30 hidden md:flex items-center gap-4 cursor-pointer hover:bg-white/30 transition-colors">
                <div class="w-12 h-12 bg-white rounded-full flex items-center justify-center shrink-0 shadow-lg">
                    <svg class="w-6 h-6 text-brand-900 ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                </div>
                <div class="text-white text-sm font-medium">Watch our story <br><span class="opacity-80 text-xs font-light">A short film by Trek.</span></div>
            </div>
        </div>
        
        <!-- Decorative geometric shape -->
        <div class="absolute -bottom-8 -left-8 w-32 h-32 border-2 border-accent rounded-full opacity-50 hidden lg:block"></div>
        <div class="absolute top-12 -right-6 w-24 h-24 bg-brand-900 dark:bg-white rounded-full opacity-10 hidden lg:block"></div>
    </div>
</div>
</section>
<!-- 2. Our Journey — Curved Timeline -->"""

content = pattern.sub(new_hero, content)

with open('about.html', 'w') as f:
    f.write(content)

print("Done")
