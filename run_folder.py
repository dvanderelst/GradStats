import os

def generate_readme_md(course_root, github_repo_url, branch, included_numbers):
    # Initialize the content for the readme file
    readme_content = "# Course Tutorials\n\n"
    readme_content += "This page contains links to all class notes and R scripts organized by section.\n\n"
    
    # Walk through the course folder
    for section_folder in sorted(os.listdir(course_root)):
        section_path = os.path.join(course_root, section_folder)
        
        # Check if the folder starts with a number in the included_numbers list
        folder_number = section_folder.split(" ", 1)[0]
        if os.path.isdir(section_path) and folder_number.isdigit() and int(folder_number) in included_numbers:
            # Extract section name by splitting on the first space
            section_name = section_folder.split(" ", 1)[1].replace("_", " ").title()  # Format the section name in title case
            readme_content += f"## {section_name}\n"
            
            # Separate markdown and R files
            md_files = []
            r_files = []
            
            # Find markdown and R files in each section
            for file in sorted(os.listdir(section_path)):
                if file.endswith(".md"):
                    md_files.append(file)
                elif file.endswith(".R"):
                    r_files.append(file)

            # Add markdown files to the section
            if md_files:
                readme_content += "**Class Notes (Markdown files):**\n"
                for file in md_files:
                    file_path = os.path.join(section_folder, file)
                    tutorial_name = file.replace(".md", "").replace("_", " ").title()  # Format the file name
                    readme_content += f"- [{tutorial_name}]({file_path})\n"
            
            # Add R files to the section
            if r_files:
                readme_content += "\n**R Scripts:**\n"
                for file in r_files:
                    # Link to GitHub view of the file using the specified branch
                    github_file_url = f"{github_repo_url}/blob/{branch}/{section_folder}/{file}"
                    script_name = file.replace(".R", "").replace("_", " ").title()  # Format the script name
                    readme_content += f"- [{script_name}]({github_file_url})\n"
            
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
