import os

def generate_index_md(course_root):
    # Initialize the content for the index file
    index_content = "# Course Tutorials\n\n"
    index_content += "This page contains links to all tutorials and R scripts organized by section.\n\n"
    
    # Walk through the course folder
    for section_folder in sorted(os.listdir(course_root)):
        section_path = os.path.join(course_root, section_folder)
        # Only process directories that represent course sections with the format '02 DataWrangling'
        if os.path.isdir(section_path) and " " in section_folder and section_folder[0].isdigit():
            # Extract section name by splitting on the first space
            section_name = section_folder.split(" ", 1)[1].replace("_", " ").title()  # Format the section name
            index_content += f"## {section_name}\n"
            
            # Find markdown and R files in each section
            for file in sorted(os.listdir(section_path)):
                if file.endswith(".md") or file.endswith(".R"):  # Include both .md and .R files
                    file_path = os.path.join(section_folder, file)
                    tutorial_name = file.replace(".md", "").replace(".R", "").replace("_", " ").title()  # Format the file name
                    # Create link to the file
                    index_content += f"- [{tutorial_name}]({file_path})\n"
            
            index_content += "\n"  # Add space after each section

    # Write the index file to the course root folder
    index_file_path = os.path.join(course_root, "index.md")
    with open(index_file_path, "w") as f:
        f.write(index_content)

    print(f"index.md generated successfully at {index_file_path}!")

# Example usage:
if __name__ == "__main__":
    course_root = "."  # Use current directory as the course root
    generate_index_md(course_root)
