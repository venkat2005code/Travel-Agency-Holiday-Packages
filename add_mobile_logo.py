import re

files = ['dashboard.html', 'admin.html']

old_hamburger = """<!-- Sidebar Toggle (Mobile) -->
<button id="sidebar-toggle" class="lg:hidden mr-4 text-gray-500 hover:text-gray-900 dark:hover:text-white transition-colors">
    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
</button>"""

new_mobile_group = """<!-- Mobile Left Group (Hamburger + Logo) -->
<div class="flex items-center gap-3 lg:hidden shrink-0">
    <button id="sidebar-toggle" class="text-gray-500 hover:text-brand-900 dark:hover:text-white transition-colors">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
    </button>
    <a class="flex items-center gap-1 font-serif font-bold text-xl text-brand-900 dark:text-white" href="index.html">
        <svg class="w-6 h-6 text-accent shrink-0" fill="currentColor" viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z"></path></svg>
        <span>Trek<span class="text-accent">.</span></span>
    </a>
</div>"""

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    # The hamburger block might have been modified in spacing, let's use a regex to safely replace it
    # But it's exactly the same in my earlier grep
    if old_hamburger in content:
        content = content.replace(old_hamburger, new_mobile_group)
    else:
        # Fallback if there are minor whitespace differences
        content = re.sub(
            r'<!-- Sidebar Toggle \(Mobile\) -->\s*<button id="sidebar-toggle" class="lg:hidden mr-4[^>]+>.*?</button>',
            new_mobile_group,
            content,
            flags=re.DOTALL
        )
        
    with open(file, 'w') as f:
        f.write(content)

print("Done")
