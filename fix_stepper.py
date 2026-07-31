import re

with open('packages.html', 'r') as f:
    content = f.read()

# Fix Step 1 border
target = '<div class="w-10 h-10 rounded-full bg-brand-900 dark:bg-white text-white dark:text-brand-900 font-bold flex items-center justify-center shadow-lg"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewbox="0 0 24 24"><path d="M5 13l4 4L19 7" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path></svg></div>'
replacement = '<div class="w-10 h-10 rounded-full bg-brand-900 dark:bg-white text-white dark:text-brand-900 font-bold flex items-center justify-center shadow-lg border-4 border-white dark:border-gray-800"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewbox="0 0 24 24"><path d="M5 13l4 4L19 7" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path></svg></div>'

content = content.replace(target, replacement)

with open('packages.html', 'w') as f:
    f.write(content)

print("Done")
