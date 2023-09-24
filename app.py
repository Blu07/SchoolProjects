from flask import Flask, render_template, url_for
import os
import subprocess
import threading
import secrets
import sys
import re
import argparse

secret_key = secrets.token_hex(16)

main_Folder = 'Projects'

app = Flask(__name__, template_folder=main_Folder)
app.secret_key = secret_key

def loadProjects():
    
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
                
                # Add the title and link to the project_pages list
                project_pages.append((file_name_str, link))

    # Sort the project_pages list alphabetically by title
    project_pages.sort(key=lambda x: x[0])
    
    # Generate the link
    html_str = '<nav>'
    for name, url in project_pages:
        href = f"{ url_for('serve_project', project_path=url) }"
        link = f'''<a href="{href}">{name}</a>'''
        html_str += link

    html_str += '</nav>'


    return html_str



@app.route('/')
def index():
    side_menu_content = loadProjects()

    return render_template('index.html', side_menu_content=side_menu_content, title="Main Page")




@app.route(f'/{main_Folder}/<path:project_path>')
def serve_project(project_path):
    # Split the project_path into a list of directories and the final HTML file
    path_parts = project_path.split("/")
    num_layers = len(path_parts)
    print(num_layers)
    side_menu_content = loadProjects()

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
    return render_template(
        f"{project_name}/{subfolders}/{file_name}",
        side_menu_content=side_menu_content,
        title=path_parts[-2]
        )





if __name__ == '__main__':
    
    # Define a function to run the SASS watcher
    def run_full_process():
        full_sass_process = subprocess.Popen(['python', 'static/python/full_sass.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        full_sass_process.communicate()
      

    # Define a function to run the SASS watcher
    def run_sass_watcher():
            sass_watcher_process = subprocess.Popen(['python', 'static/python/sass_watcher.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            sass_watcher_process.communicate()
    


    parser = argparse.ArgumentParser(
        prog='SASS Watcher',
        description='Watches for changes made to scss files, then updates that css file'
    )
    
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-i', '--init', action='store_true', help='Initialize venv, install python and node modules')
    group.add_argument('-f', '--full', action='store_true')
    group.add_argument('-n', '--normal', action='store_true')
    
    args = parser.parse_args()


    initialize = args.init
    do_full_sass = initialize or args.full


    if initialize:
        os.system('''
                  pip install -r requirements.txt \
                  npm install \
                  ''')
        

    if do_full_sass:
        print("Preprocessing all .scss files...")
        
        # Create a thread to run the full process
        full_sass_thread = threading.Thread(target=run_full_process)
        full_sass_thread.start()
        full_sass_thread.join()


    # Create a thread to run the SASS watcher
    sass_watcher_thread = threading.Thread(target=run_sass_watcher)
    sass_watcher_thread.daemon = True  # Exit the thread when the main program exits
    sass_watcher_thread.start()
    
    # Run the app on completion
    app.run(debug=True)




    # mode = init:
    #    pip install flask
    #    pip install watchdog
    #    npm install sass
    #    python static/python/full_sass.py

    # mode = full_sass:
