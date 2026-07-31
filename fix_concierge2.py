import re

with open('contact.html', 'r') as f:
    content = f.read()

# Remove the glassmorphism card and shadow, restore original clean background
old_pattern = re.compile(r'<div class="relative z-10 text-center px-8 py-12 md:py-16 md:px-16 max-w-3xl mx-auto bg-white/70 dark:bg-gray-900/70 backdrop-blur-xl rounded-\[3rem\] shadow-\[0_20px_60px_rgba\(0,0,0,0\.05\)\] dark:shadow-\[0_20px_60px_rgba\(255,255,255,0\.02\)\] border border-white/50 dark:border-white/10 mx-6 sm:mx-auto">')
new_div = '<div class="relative z-10 text-center px-6 max-w-2xl mx-auto">'

content = old_pattern.sub(new_div, content)

# Adjust image positions so they don't overlap the text
img1 = re.compile(r'<div class="absolute top-20 md:top-32 left-4 md:left-12 lg:left-24 w-32 md:w-56 lg:w-64 h-48 md:h-72 lg:h-80 rounded-\[2rem\] overflow-hidden shadow-2xl animate-float-1 z-0 hidden sm:block">')
img1_new = '<div class="absolute top-32 left-4 md:left-8 lg:left-16 w-32 md:w-48 lg:w-64 h-48 md:h-72 lg:h-80 rounded-[2rem] overflow-hidden shadow-2xl animate-float-1 z-0 hidden sm:block">'

img2 = re.compile(r'<div class="absolute bottom-16 md:bottom-24 right-4 md:right-12 lg:right-24 w-36 md:w-64 lg:w-72 h-36 md:h-64 lg:h-72 rounded-full overflow-hidden shadow-2xl animate-float-2 z-0 hidden sm:block">')
img2_new = '<div class="absolute bottom-24 right-4 md:right-8 lg:right-16 w-36 md:w-48 lg:w-72 h-36 md:h-48 lg:h-72 rounded-full overflow-hidden shadow-2xl animate-float-2 z-0 hidden sm:block">'

content = img1.sub(img1_new, content)
content = img2.sub(img2_new, content)

with open('contact.html', 'w') as f:
    f.write(content)

print("Done")
