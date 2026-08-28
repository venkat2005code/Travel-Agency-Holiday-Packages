import re

old_block = r'''<button class="relative text-gray-500 hover:text-blue-600 transition-colors">
<svg class="w-5 h-5 sm:w-6 sm:h-6" fill="none" stroke="currentColor" viewbox="0 0 24 24"><path d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path></svg>
<span class="absolute top-0 right-0 w-2.5 h-2.5 bg-red-500 rounded-full border-2 border-white dark:border-gray-800"></span>
</button>'''

new_block = '''<div class="relative group">
<button class="relative text-gray-500 hover:text-blue-600 transition-colors py-1">
<svg class="w-5 h-5 sm:w-6 sm:h-6" fill="none" stroke="currentColor" viewbox="0 0 24 24"><path d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path></svg>
<span class="absolute top-1 right-0 w-2.5 h-2.5 bg-red-500 rounded-full border-2 border-white dark:border-gray-800"></span>
</button>
<div class="absolute top-full right-0 mt-2 w-72 bg-white dark:bg-gray-800 rounded-xl shadow-xl opacity-0 group-hover:opacity-100 pointer-events-none group-hover:pointer-events-auto transition-all before:absolute before:-top-4 before:right-0 before:w-full before:h-4 border border-gray-100 dark:border-gray-700 z-50 overflow-hidden">
<div class="px-4 py-3 border-b border-gray-100 dark:border-gray-700 font-bold text-brand-900 dark:text-white bg-gray-50 dark:bg-gray-800/50">Notifications</div>
<a class="block px-4 py-3 hover:bg-gray-50 dark:hover:bg-gray-700 text-sm border-b border-gray-100 dark:border-gray-700 transition-colors" href="#"><span class="font-bold text-brand-900 dark:text-white">Flight Update</span><br/><span class="text-gray-500">Your Paris flight schedule has changed.</span></a>
<a class="block px-4 py-3 hover:bg-gray-50 dark:hover:bg-gray-700 text-sm transition-colors border-b border-gray-100 dark:border-gray-700" href="#"><span class="font-bold text-brand-900 dark:text-white">Payment Received</span><br/><span class="text-gray-500">Thank you for your final installment.</span></a>
<a class="block px-4 py-2 text-center text-xs font-bold text-blue-600 hover:text-blue-800 bg-gray-50 dark:bg-gray-700/50 transition-colors" href="#">View all notifications</a>
</div>
</div>'''

for f in ['dashboard.html', 'admin.html']:
    with open(f, 'r') as file:
        content = file.read()
    
    content = content.replace(old_block, new_block)
    
    with open(f, 'w') as file:
        file.write(content)
    print(f"Updated {f}")
