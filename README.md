# Static-Site-Generator

A robust, Python-based static site generator that transforms Markdown content into a structured HTML website. This project demonstrates backend engineering fundamentals, specifically focusing on file system manipulation, recursive processing, and the transformation of unstructured data into web-ready formats.

🚀 Overview
In a modern ICT environment, static site generators offer a high-security, low-latency alternative to traditional CMS platforms. By removing the database and server-side processing at runtime, this architecture significantly reduces the attack surface, making it an ideal choice for high-integrity government or corporate documentation sites.

🛠 Technical Features
Recursive Directory Processing: Automatically crawls a source directory to mirror its structure in the public output, demonstrating mastery of Python's os and shutil libraries.

Markdown-to-HTML Parser: Custom-built logic to handle block-level elements (headings, quotes, lists, code blocks) and inline markdown (bold, italic, links, images).

Template Integration: Utilizes a centralized HTML template to ensure design consistency across all generated pages.

Automated Build Pipeline: Includes a clean-and-build script that ensures the public directory is refreshed and synchronized with the latest source content every time the generator runs.

🏗 Key Programming Concepts Demonstrated
Recursion: Used for traversing complex folder structures.

Object-Oriented Programming (OOP): Implementing nodes and leaf-nodes to represent HTML structures.

Regex & String Manipulation: Efficiently parsing markdown syntax into valid HTML tags.

Error Handling: Robust management of file permissions and directory paths.

🛡 Strategic & Security Considerations
Zero-Trust Content Delivery: Because the output is purely static HTML/CSS, the risks of SQL Injection and Cross-Site Scripting (XSS) are virtually eliminated at the server level.

Infrastructure Simplicity: The generated site can be hosted on any secure object storage (AWS S3, Azure Blob, etc.), reducing maintenance overhead and technical debt.

Auditability: Every change to the site is tracked through Git version control before the site is built, providing a perfect audit trail for compliance and governance.

🚦 How to Run
Clone the repository:

Bash
git clone https://github.com/jmacneill66/Static-Site-Generator.git
Run the generator:

Bash
python3 main.sh
View the output:
The generated site will be available in the /public directory.


