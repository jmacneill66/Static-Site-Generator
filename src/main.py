from operator import index
from tempfile import template
from md_to_html_node import *
import shutil
import os
import sys


def copy_directory(src: str, dest: str):
    """Recursively copies all contents from src to dest, ensuring a clean copy."""
    if os.path.exists(dest):
        shutil.rmtree(dest)  # Remove existing destination directory

    os.makedirs(dest)  # Create a fresh destination directory

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isdir(src_path):
            # Recursively copy subdirectories
            copy_directory(src_path, dest_path)
        else:
            shutil.copy2(src_path, dest_path)  # Copy files
            print(f"Copied: {dest_path}")


def extract_title(markdown):
    """Extracts the first H1 title from markdown."""
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No H1 title found in markdown")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    """Recursively generate pages for all markdown files in a directory."""
    for root, _, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, dir_path_content)
                dest_path = os.path.join(
                    dest_dir_path, os.path.splitext(relative_path)[0] + ".html")

                # Create the destination directory if it doesn't exist
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                # Generate the HTML page
                generate_page(from_path, template_path, dest_path, basepath)


"""
def generate_page(from_path, template_path, dest_path, basepath):
    \""" Generates an HTML page using markdown and a template.\"""

    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}")
    print(f"Using basepath: {basepath}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()
    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    html_content = apply_basepath(html_content, basepath)

    # Replace template placeholders
    # output_content = template_content.replace(
    #    "{{ Title }}", title).replace("{{ Content }}", html_content)
    # output_content = output_content.replace('{{ Basepath }}', basepath)

    # Make sure basepath doesn't end with a slash for our replacements
    clean_basepath = basepath
    if clean_basepath.endswith('/'):
        clean_basepath = clean_basepath[:-1]

     # Replace template placeholders
    output_content = template_content.replace(
        "{{ Title }}", title).replace("{{ Content }}", html_content)

    # Replace href="/" with href="/basepath/" (avoid double slashes)
    # output_content = output_content.replace(
    #    'href="/', f'href="{clean_basepath}/')
    # output_content = output_content.replace(
    #    'src="/', f'src="{clean_basepath}/')

    def apply_basepath(html_content, basepath):
    Apply basepath to all absolute links and src attributes, ensuring no doubling.
    # Remove trailing slash if present
    clean_basepath = basepath.rstrip('/')

    # Check if we already have the basepath in links to avoid doubling  
    if f'href="{clean_basepath}/' in html_content:
        print("WARNING: Basepath already present in links")
        return html_content

    # First replace href="/path" with href="{basepath}/path"
    result = html_content.replace('href="/', f'href="{clean_basepath}/')

    # Then replace src="/path" with src="{basepath}/path"
    result = result.replace('src="/', f'src="{clean_basepath}/')

    # Debug output
    link_start = result.find('<link')
    if link_start >= 0:
        link_end = result.find('>', link_start) + 1
        print(f"Sample link after replacement: {result[link_start:link_end]}")

    return result

    print(
        f"Sample link after replacement: {output_content[output_content.find('<link'):output_content.find('>', output_content.find('<link'))+1]}")

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output_content) """


def generate_page(from_path, template_path, dest_path, basepath):
    """Generates an HTML page using markdown and a template."""

    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}")
    print(f"Using basepath: {basepath}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    # Apply basepath corrections
    html_content = apply_basepath(html_content, basepath)

    # Ensure basepath does not end with a slash
    clean_basepath = basepath.rstrip('/')

    # Replace template placeholders
    output_content = template_content.replace(
        "{{ Title }}", title).replace("{{ Content }}", html_content)

    # Debugging: Show a sample link replacement
    link_start = output_content.find('<link')
    if link_start >= 0:
        link_end = output_content.find('>', link_start) + 1
        print(
            f"Sample link after replacement: {output_content[link_start:link_end]}")

    # Save the generated HTML
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output_content)


def apply_basepath(html_content, basepath):
    """Apply basepath to all absolute links and src attributes."""
    clean_basepath = basepath.rstrip('/')

    # Avoid applying basepath multiple times
    if f'href="{clean_basepath}/' in html_content:
        return html_content

    # Replace absolute href/src attributes with basepath prepended
    result = html_content.replace('href="/', f'href="{clean_basepath}/')
    result = result.replace('src="/', f'src="{clean_basepath}/')

    return result


def main():
    template_path = "template.html"
    src = "static"
    dest = "docs"

    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    # function deletes public folder contents before copying
    copy_directory(src, dest)

    # Generate all pages recursively from the content directory
    generate_pages_recursive("content", template_path, "docs", basepath)


if __name__ == "__main__":
    main()
