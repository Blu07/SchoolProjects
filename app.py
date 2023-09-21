from flask import Flask, render_template, send_from_directory
import os
import subprocess
import threading
import secrets
import re
import json

secret_key = secrets.token_hex(16)

main_Folder = 'Projects'

app = Flask(__name__, template_folder=main_Folder)
app.secret_key = secret_key

def getProjects():
    
    project_pages = []

    # Get a list of immediate child directories in the main_Folder folder
    project_subdirectories = [os.path.join(main_Folder, d) for d in os.listdir(main_Folder) if
                              os.path.isdir(os.path.join(main_Folder, d))]

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
                relative_path = os.path.relpath(os.path.join(subdirectory, file), main_Folder)
                link = relative_path.replace(os.sep, '/')
                print(link)
                
                # Add the title and link to the project_pages list
                project_pages.append((file_name_str, link))

    # Sort the project_pages list alphabetically by title
    project_pages.sort(key=lambda x: x[0])

    json_data = [{"name": name, "url": f'{main_Folder}/{url}'} for name, url in project_pages]
    json_file_path = 'static/json/projects.json'
    
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)




@app.route('/')
def index():
    return render_template(f"/index.html")



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
    return render_template(f"/{project_name}/{subfolders}/{file_name}")


if __name__ == '__main__':
     # Define a function to run the SASS watcher
    def run_sass_watcher():
        sass_watcher_process = subprocess.Popen(['python', 'static\python\sass_watcher.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        sass_watcher_process.communicate()

    # Create a thread to run the SASS watcher
    sass_watcher_thread = threading.Thread(target=run_sass_watcher)
    sass_watcher_thread.daemon = True  # Exit the thread when the main program exits
    sass_watcher_thread.start()
    app.run()