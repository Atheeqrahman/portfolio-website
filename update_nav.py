import os
import glob

html_files = glob.glob(r"C:\Users\athee\Downloads\Portfolio\*.html")

for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "certifications.html" in content:
        continue # already added
    
    # 1. Add to mobile-nav-links
    # Handle the fact that we might have whitespace differences
    new_mobile = '<li><a href="honors.html">Honors</a></li>\n            <li><a href="certifications.html">Certifications</a></li>'
    content = content.replace('<li><a href="honors.html">Honors</a></li>', new_mobile)
    
    # 2. Add to desktop-nav
    new_desktop_1 = '<a href="honors.html">HONORS</a>\n            <a href="certifications.html">CERTIFICATIONS</a>'
    new_desktop_2 = '<a href="honors.html" class="active">HONORS</a>\n            <a href="certifications.html">CERTIFICATIONS</a>'
    
    content = content.replace('<a href="honors.html">HONORS</a>', new_desktop_1)
    content = content.replace('<a href="honors.html" class="active">HONORS</a>', new_desktop_2)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} files.")
