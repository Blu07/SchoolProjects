from flask import Flask, render_template, jsonify
import os
import subprocess
import secrets
import re

secret_key = secrets.token_hex(16)

main_Folder = "Projects"


app = Flask(__name__, template_folder=main_Folder)
app.secret_key = secret_key

def getProjects():
    project_folder = main_Folder  # Change this to the path of your main_Folder folder
    project_pages = []

    # Get a list of immediate child directories in the main_Folder folder
    project_subdirectories = [os.path.join(project_folder, d) for d in os.listdir(project_folder) if
                              os.path.isdir(os.path.join(project_folder, d))]

    # Iterate through the subdirectories and check for HTML files one layer down
    for subdirectory in project_subdirectories:
        subdirectory_files = os.listdir(subdirectory)
        for file in subdirectory_files:
            if file.endswith(".html"):
                # Get the file name without the file extension
                file_name = os.path.splitext(file)[0]

                # Use regular expressions to split the input string at capital letters
                words = re.findall('[a-z]+|[A-Z][a-z]*|[0-9]+', file_name)
    
                # Join the words with spaces and capitalize the first letter of each word
                file_name_str = ' '.join(word.capitalize() for word in words)
                
                # Create a link based on the file's relative path within the main_Folder folder
                relative_path = os.path.relpath(os.path.join(subdirectory, file), project_folder)
                link = relative_path.replace(os.sep, '/')

                # Add the title and link to the project_pages list
                project_pages.append((file_name_str, link))

    # Sort the project_pages list alphabetically by title
    project_pages.sort(key=lambda x: x[0])

    # Generate the HTML code
   
    return (project_pages)




@app.route('/')
def index():
    projects = getProjects()
    return render_template("index.html", projects=projects)



@app.route(f'/{main_Folder}/<path:project_path>')
def serve_project(project_path):
    # Split the project_path into a list of directories and the final HTML file
    path_parts = project_path.split('/')

    # Ensure that there is at least one directory and one HTML file
    if len(path_parts) < 2 or not path_parts[-1].endswith(".html"):
        # Handle the case where the URL doesn't match your expected structure
        return "Invalid URL"

    # Extract the project_name and file_name
    project_name = path_parts[0]
    file_name = path_parts[-1]

    # Join the remaining path parts to get the folder structure
    subfolders = "/".join(path_parts[1:-1])

    # Render the template with the appropriate folder structure
    return render_template(f"{project_name}/{subfolders}/{file_name}")




if __name__ == '__main__':
    # Run the SASS watcher script as a subprocess and capture its output
    sass_watcher_process = subprocess.Popen(['python', 'sass_watcher.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    app.run()

    sass_watcher_process.terminate()