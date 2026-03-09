import os
import glob
import re

desired_order_hrefs = [
    "index.html",
    "work.html",
    "projects.html",
    "certifications.html",
    "research.html",
    "honors.html"
]

def reorder_list(html_content, is_list_item=False):
    if is_list_item:
        pattern = r'(\s*)(<li.*?>.*?</li>)'
    else:
        pattern = r'(\s*)(<a.*?>.*?</a>)'
        
    items = re.findall(pattern, html_content, re.DOTALL)
    if not items:
        return html_content
    
    item_map = {}
    for ws, item_html in items:
        m = re.search(r'href="([^"]+)"', item_html)
        if m:
            item_map[m.group(1)] = (ws, item_html)
            
    result_pieces = []
    # capture the first whitespace to use as default
    default_ws = items[0][0] if items else "\n            "
    
    for href in desired_order_hrefs:
        if href in item_map:
            ws, item_html = item_map[href]
            result_pieces.append(default_ws + item_html)
            del item_map[href]
            
    # add remaining
    for href, (ws, item_html) in item_map.items():
        result_pieces.append(default_ws + item_html)
        
    return "".join(result_pieces) + "\n        "

def replace_nav(match):
    return '<ul class="mobile-nav-links">' + reorder_list(match.group(1), True) + '</ul>'

def replace_desktop(match):
    return '<nav class="desktop-nav">' + reorder_list(match.group(1), False) + '</nav>'

directory = r"C:\Users\athee\Downloads\Portfolio"
count = 0

for filepath in glob.glob(os.path.join(directory, "*.html")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = re.sub(r'<ul class="mobile-nav-links">(.*?)</ul>', replace_nav, content, flags=re.DOTALL)
    new_content = re.sub(r'<nav class="desktop-nav">(.*?)</nav>', replace_desktop, new_content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Reordered navigation in {os.path.basename(filepath)}")
        
print(f"Nav elements reordered successfully in {count} HTML files.")
