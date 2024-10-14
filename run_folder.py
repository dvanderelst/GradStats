import os

def generate_readme_md(course_root):
    # Initialize the content for the readme file
    readme_content = "# Course Tutorials\n\n"
    readme_content += "This page contains links to all tutorials and R scripts organized by section.\n\n"
    
    # Walk through the course folder
    for section_folder in sorted(os.listdir(course_root)):
        section_path = os.path.join(course_root, section_folder)
        # Only process directories that represent course sections with the format '02 DataWrangling'
        if os.path.isdir(section_path) and " " in section_folder and section_folder[0].isdigit():
            # Extract section name by splitting on the first space
            section_name = section_folder.split(" ", 1)[1].replace("_", " ").title()  # Format the section name
            readme_content += f"## {section_name}\n"
            
            # Find markdown and R files in each section
            for file in sorted(os.listdir(section_path)):
                if file.endswith(".md") or file.endswith(".R"):  # Include both .md and .R files
                    file_path = os.path.join(section_folder, file)
                    tutorial_name = file.replace(".md", "").replace(".R", "").replace("_", " ").title()  # Format the file name
                    # Create link to the file
                    readme_content += f"- [{tutorial_name}]({file_path})\n"
            
            readme_content += "\n"  # Add space after each section

    # Write the readme file to the course root folder
    readme_file_path = os.path.join(course_root, "README.md")
    with open(readme_file_path, "w") as f:
        f.write(readme_content)

    print(f"README.md generated successfully at {readme_file_path}!")

# Example usage:
if __name__ == "__main__":
    course_root = "."  # Use current directory as the course root
    generate_readme_md(course_root)
