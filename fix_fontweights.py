import re
import glob

# Rules:
# h1, h2, h3, h4 -> replace font-bold/font-extrabold/font-black with font-semibold (600)
# p, subheadings (labels, captions) -> keep at font-normal(400) or font-medium(500) max

def fix_heading_weights(tag_match):
    """For heading tags, replace font-bold/font-extrabold/font-black with font-semibold"""
    content = tag_match.group(0)
    content = re.sub(r'\bfont-extrabold\b|\bfont-black\b|\bfont-bold\b', 'font-semibold', content)
    return content

def fix_para_weights(tag_match):
    """For p tags, replace font-bold/font-semibold/font-medium > 500 with font-medium"""
    content = tag_match.group(0)
    content = re.sub(r'\bfont-extrabold\b|\bfont-black\b|\bfont-bold\b|\bfont-semibold\b', 'font-medium', content)
    return content

html_files = [f for f in glob.glob('*.html')]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Fix heading tags (h1 through h4): inline tags only (not multi-line spanning beyond the opening tag)
    # We match the opening tag including its class attribute
    content = re.sub(
        r'<h[1-4](?=\s)[^>]*>',
        fix_heading_weights,
        content
    )

    # Fix paragraph tags  
    content = re.sub(
        r'<p(?=\s)[^>]*>',
        fix_para_weights,
        content
    )

    if content != original:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filename}")
    else:
        print(f"No changes: {filename}")

