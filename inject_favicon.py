import os
import glob

directory = r"C:\Users\athee\Downloads\Portfolio"
favicon_tag = '    <link rel="icon" href="img/ar_logo.png">\n</head>'

count = 0
for filepath in glob.glob(os.path.join(directory, "*.html")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<link rel="icon"' not in content:
        new_content = content.replace('</head>', favicon_tag)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Added favicon to {os.path.basename(filepath)}")

print(f"Successfully injected favicon into {count} files.")
