import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    original = content
    
    # 1. Nav gap
    content = re.sub(r'<nav class="hidden lg:flex items-center gap-6">', r'<nav class="hidden lg:flex items-center gap-4 xl:gap-6">', content)
    
    # 2. Right side container gap
    content = re.sub(r'<div class="flex items-center gap-4">\s*(?=<button[^>]+id="theme-toggle")', r'<div class="flex items-center gap-2 xl:gap-4">\n', content)
    
    # 3. Button group gap
    content = re.sub(r'<div class="hidden lg:flex gap-3">', r'<div class="hidden lg:flex gap-2 xl:gap-3">', content)
    
    # 4. Remove ml-2 from LTR button
    content = re.sub(r'transition-colors ml-2 flex-shrink-0">LTR</button>', r'transition-colors flex-shrink-0">LTR</button>', content)
    
    # 5. Add whitespace-nowrap to Log in and Sign up
    content = re.sub(r'transition-colors"\s+href="login\.html">Log in</a>', r'transition-colors whitespace-nowrap" href="login.html">Log in</a>', content)
    content = re.sub(r'transition-shadow"\s+href="register\.html">Sign up</a>', r'transition-shadow whitespace-nowrap" href="register.html">Sign up</a>', content)
    content = re.sub(r'transition-colors"\s+href="register\.html">Sign up</a>', r'transition-colors whitespace-nowrap" href="register.html">Sign up</a>', content)
    
    # 6. Add whitespace-nowrap to Nav items
    for word in ['Destinations', 'Packages', 'About', 'Contact', 'Bookings']:
        content = re.sub(r'transition-colors"\s+href="([^"]+)">' + word + r'</a>', r'transition-colors whitespace-nowrap" href="\1">' + word + r'</a>', content)
        
    # 7. Add whitespace-nowrap to Dashboards button
    content = re.sub(r'transition-colors flex items-center gap-1">\s*Dashboards', r'transition-colors flex items-center gap-1 whitespace-nowrap">\n                        Dashboards', content)

    if content != original:
        with open(file, 'w') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"No changes for {file}")
