import re

with open('home2.html', 'r') as f:
    content = f.read()

# Fix hero section height
content = content.replace('<section class="relative h-[85vh] min-h-[600px] w-full flex flex-col md:flex-row bg-[#F9F9F8] dark:bg-gray-900 overflow-hidden">', 
                          '<section class="relative h-[85vh] min-h-[500px] md:h-[70vh] lg:h-[85vh] lg:min-h-[600px] w-full flex flex-col md:flex-row bg-[#F9F9F8] dark:bg-gray-900 overflow-hidden">')

# Fix left typography container (w-1/2 -> w-[45%])
content = content.replace('<div class="w-full md:w-1/2 h-full flex flex-col justify-center px-8 md:pl-24 relative z-20">',
                          '<div class="w-full md:w-[45%] lg:w-1/2 h-full flex flex-col justify-center px-8 md:pl-12 lg:pl-24 relative z-20">')

# Fix typography sizes (md:text-[8rem] -> md:text-[6rem])
content = content.replace('<h1 class="text-[5rem] md:text-[8rem] lg:text-[10rem] font-serif font-bold text-brand-900 dark:text-white leading-[0.8] tracking-tighter mix-blend-difference dark:mix-blend-normal">',
                          '<h1 class="text-[5rem] md:text-[5.5rem] lg:text-[10rem] font-serif font-bold text-brand-900 dark:text-white leading-[0.85] tracking-tighter mix-blend-difference dark:mix-blend-normal mt-12 md:mt-0">')

# Fix description margin (mt-8 -> mt-16)
content = content.replace('<p class="mt-8 text-xl font-medium text-gray-500 dark:text-gray-400 max-w-sm md:ml-12 border-l-4 border-accent pl-6">',
                          '<p class="mt-8 md:mt-12 lg:mt-16 text-lg md:text-xl font-medium text-gray-500 dark:text-gray-400 max-w-sm md:ml-8 lg:ml-12 border-l-4 border-accent pl-6">')

# Fix right image container (w-1/2 -> w-[55%])
content = content.replace('<div class="absolute inset-0 md:relative md:w-1/2 h-full z-0 md:z-10 bg-gray-200">',
                          '<div class="absolute inset-0 md:relative md:w-[55%] lg:w-1/2 h-full z-0 md:z-10 bg-gray-200">')

# Fix featured expedition card placement
content = content.replace('<div class="hidden md:block absolute bottom-12 right-12 bg-white/90 dark:bg-gray-900/90 backdrop-blur-md p-6 max-w-xs border-l-2 border-accent">',
                          '<div class="hidden md:block absolute bottom-1/4 right-8 lg:bottom-16 lg:right-16 bg-white/90 dark:bg-gray-900/90 backdrop-blur-md p-5 lg:p-6 max-w-[250px] lg:max-w-xs border-l-2 border-accent shadow-2xl">')

with open('home2.html', 'w') as f:
    f.write(content)

print("Done")
