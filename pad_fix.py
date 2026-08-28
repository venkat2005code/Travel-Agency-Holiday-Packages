import re

with open('packages.html', 'r') as f:
    content = f.read()

# Replace padding for max-w containers
content = re.sub(r'(max-w-\w+\s+mx-auto\s+)px-6', r'\1px-8 lg:px-12', content)

with open('packages.html', 'w') as f:
    f.write(content)
print("Updated padding in packages.html")
