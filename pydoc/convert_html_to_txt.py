import os

# List all HTML files in the current directory
html_files = [file for file in os.listdir() if file.endswith(".html")]

# Create or open the pydoc.txt file
with open("pydoc.txt", "w") as txt_file:
    # Loop through each HTML file
    for html_file in html_files:
        with open(html_file, "r") as html_content:
            # Read the content of the HTML file
            content = html_content.read()
            # Write the content to pydoc.txt
            txt_file.write(content)
