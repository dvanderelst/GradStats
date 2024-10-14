import os
import re

def generate_readme_md(course_root, github_repo_url, branch, included_numbers):
    # Initialize the content for the readme file
    readme_content = "# Course Tutorials\n\n"
    readme_content += "This page contains links to all class notes and R scripts organized by section.\n\n"
    
    # Regular expression to match numbers at the start of a file name followed by space or hyphen
    num_prefix_pattern = re.compile(r'^\d+[\s-]')

    # Walk through the course folder
    for section_folder in sorted(os.listdir(course_root)):
        section_path = os.path.join(course_root, section_folder)
        
        # Check if the folder starts with a number in the included_numbers list
        folder_number = section_folder.split(" ", 1)[0]
        if os.path.isdir(section_path) and folder_number.isdigit() and int(folder_number) in included_numbers:
            # Extract section name by splitting on the first space
            section_name = section_folder.split(" ", 1)[1].replace("_", " ").title()  # Format the section name in title case
            readme_content += f"## {section_name}\n"
            
            # Separate numbered and non-numbered markdown files, and R files
            numbered_md_files = []
            non_numbered_md_files = []
            r_files = []
            
            # Find markdown and R files in each section
            for file in sorted(os.listdir(section_path)):
                if file.endswith(".md"):
                    # Check if the file starts with a number
                    match = num_prefix_pattern.match(file)
                    if match:
                        numbered_md_files.append(file)  # Store file name
                    else:
                        non_numbered_md_files.append(file)
                elif file.endswith(".R"):
                    r_files.append(file)

            # Sort numbered markdown files by their prefix number
            numbered_md_files.sort()

            # Add numbered markdown files to the section
            if numbered_md_files:
                readme_content += "**Class Notes (Markdown files):**\n"
                for file in numbered_md_files:
                    file_path = os.path.join(section_folder, file)
                    # Remove number prefixes and replace hyphens with spaces
                    tutorial_name = re.sub(r'^\d+[\s-]', '', file).replace(".md", "").replace("-", " ").title()
                    readme_content += f"- [{tutorial_name}]({file_path})\n"
            
            # Add non-numbered markdown files
            if non_numbered_md_files:
                if not numbered_md_files:  # Add a header if no numbered files
                    readme_content += "**Class Notes (Markdown files):**\n"
                for file in non_numbered_md_files:
                    file_path = os.path.join(section_folder, file)
                    # Replace hyphens with spaces
                    tutorial_name = file.replace(".md", "").replace("-", " ").title()
                    readme_content += f"- [{tutorial_name}]({file_path})\n"

            # Add R files to the section
            if r_files:
                readme_content += "\n**R Scripts:**\n"
                for file in r_files:
                    # Link to GitHub view of the file using the specified branch
                    github_file_url = f"{github_repo_url}/blob/{branch}/{section_folder}/{file}"
                    script_name = file.replace("-", " ")  # Keep the `.R` extension, replace hyphens with spaces
                    readme_content += f"- [`{script_name}`]({github_file_url})\n"
            
            readme_content += "\n"  # Add space after each section

    # Write the readme file to the course root folder
    readme_file_path = os.path.join(course_root, "README.md")
    with open(readme_file_path, "w") as f:
        f.write(readme_content)

    print(f"README.md generated successfully at {readme_file_path}!")

# Example usage:
if __name__ == "__main__":
    course_root = "."  # Use current directory as the course root
    github_repo_url = "https://github.com/dvanderelst/GradStats"
    branch = "Fall2024"  # Specify the current branch
    included_numbers = [1, 2, 3, 4, 5, 6]  # Example: Only include folders starting with 2, 3, or 5
    generate_readme_md(course_root, github_repo_url, branch, included_numbers)
