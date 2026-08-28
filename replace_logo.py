import os
import re
import glob

# The old path variations
old_path_regex = re.compile(
    r'<path[^>]*d="M3\.055\s+11H5a2\s+2\s+0\s+012\s+2v1a2\s+2\s+0\s+002\s+2\s+2\s+2\s+0\s+012\s+2v2\.945M8\s+3\.935V5\.5A2\.5\s+2\.5\s+0\s+0010\.5\s+8h\.5a2\s+2\s+0\s+012\s+2\s+2\s+2\s+0\s+104\s+0\s+2\s+2\s+0\s+012-2h1\.064M15\s+20\.488V18a2\s+2\s+0\s+012-2h3\.064M21\s+12a9\s+9\s+0\s+11-18\s+0\s+9\s+9\s+0\s+0118\s+0z"[^>]*>'
    r'|'
    r'<path[^>]*d="M3\.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2\.945M8 3\.935V5\.5A2\.5 2\.5 0 0010\.5 8h\.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1\.064M15 20\.488V18a2 2 0 012-2h3\.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"[^>]*>'
)

# New path
new_path = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18z M3.5 9h17 M3.5 15h17 M12 3v18 M12 3c-4.4 4-4.4 14 0 18 M12 3c4.4 4 4.4 14 0 18"></path>'

files = glob.glob('*.html')
for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # We also need to handle the one with stroke-width="1.5" if necessary, but regex should catch it 
    # wait, the regex above matches <path ... d="..."> where d is the exact string.
    
    # Let's just do a simpler string replace since the d attribute is constant
    d_string = 'M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z'
    
    if d_string in content:
        # replace the whole path tag. It's safer to just replace the d="" content
        content = content.replace(d_string, 'M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18z M3.5 9h17 M3.5 15h17 M12 3v18 M12 3c-4.4 4-4.4 14 0 18 M12 3c4.4 4 4.4 14 0 18')
        
        with open(f, 'w') as file:
            file.write(content)
        print(f"Updated {f}")

