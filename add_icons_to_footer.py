import os
import glob
import re

directory = r"C:\Users\athee\Downloads\Portfolio"

# Added FontAwesome icons and optional pipe separation as requested in the prompt
target_footer = """<footer>
        <a href="https://www.linkedin.com/in/rahmanatheeq/" target="_blank"><i class="fa-brands fa-linkedin-in" style="margin-right: 5px;"></i>LinkedIn</a> <span style="margin-right: 15px; color: #ccc;">|</span>
        <a href="mailto:atheeqrahman15@gmail.com"><i class="fa-regular fa-envelope" style="margin-right: 5px;"></i>Email</a> <span style="margin-right: 15px; color: #ccc;">|</span>
        <a href="https://www.instagram.com/atheeqrahman._/?hl=en" target="_blank"><i class="fa-brands fa-instagram" style="margin-right: 5px;"></i>Instagram</a>
    </footer>"""

count = 0
for filepath in glob.glob(os.path.join(directory, "*.html")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We match the entire footer tag to replace it wholesale
    pattern = re.compile(r'<footer>.*?</footer>', re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub(target_footer, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Added icons to footer in {os.path.basename(filepath)}")

print(f"Successfully updated footers with icons in {count} files.")
