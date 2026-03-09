import os
import glob
import re

directory = r"C:\Users\athee\Downloads\Portfolio"

target_footer = """<footer>
        <a href="https://www.linkedin.com/in/rahmanatheeq/" target="_blank">LinkedIn</a>
        <a href="mailto:atheeqrahman15@gmail.com">Email</a>
        <a href="https://www.instagram.com/atheeqrahman._/?hl=en" target="_blank">Instagram</a>
    </footer>"""

count = 0
for filepath in glob.glob(os.path.join(directory, "*.html")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the existing footer gracefully
    pattern = re.compile(r'<footer>\s*<a href="#">LinkedIn</a>\s*<a href="#">Email</a>\s*<a href="#">Instagram</a>\s*</footer>', re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub(target_footer, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated footer in {os.path.basename(filepath)}")
    else:
        # Fallback if the space differs slightly or it was already updated
        fallback_pattern = re.compile(r'<footer>.*?</footer>', re.DOTALL)
        if fallback_pattern.search(content):
            new_content = fallback_pattern.sub(target_footer, content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Updated footer via fallback in {os.path.basename(filepath)}")

print(f"Successfully updated footers in {count} files.")
