from flask import Flask, render_template, url_for
from init import scss_Folder, css_Folder
import secrets
import os
import subprocess
import threading
import re

secret_key = secrets.token_hex(16)

main_Folder = 'Projects'


app = Flask(__name__, template_folder=main_Folder)
app.secret_key = secret_key


def load_projects():

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
                file_name_str = process_name(os.path.splitext(file)[0])

                # Create a link based on the file's relative path within the main_Folder folder
                relative_path = os.path.relpath(
                    os.path.join(subdirectory, file), main_Folder)

                link = relative_path.replace(os.sep, '/')

                # Add the title and link to the project_pages list
                project_pages.append((link, file_name_str))

    # Sort the project_pages list alphabetically by title
    project_pages.sort(key=lambda x: x[0])

    # Generate the link
    html_str = '<nav>'
    for url, name in project_pages:
        href = f"{ url_for('serve_project', project_path=url) }"
        link = f'''<a href="{href}">{name}</a>'''
        html_str += link

    html_str += '</nav>'

    return html_str, project_pages


def process_name(original_name: str) -> str:

    # Use regular expressions to split the input string at capital letters
    words = re.findall('[a-z]+|[A-Z][a-z]*|[0-9]+', original_name)

    # Join the words with spaces and capitalize the first letter of each word
    new_name = ' '.join(word.capitalize() for word in words)

    return new_name


@app.route('/')
def index():
    side_menu_content, _ = load_projects()

    return render_template('index.html', side_menu_content=side_menu_content, title="Main Page")


@app.route(f'/{main_Folder}/<path:project_path>')
def serve_project(project_path):
    # Split the project_path into a list of directories and the final HTML file
    path_parts = project_path.split("/")
    num_layers = len(path_parts)
    print(num_layers)
    side_menu_content, all_pages = load_projects()

    # Ensure that there is at least one directory and one HTML file
    if len(path_parts) < 2 or not path_parts[-1].endswith(".html"):
        # Handle the case where the URL doesn't match your expected structure
        return "Invalid URL"

    # Extract the project_name and file_name
    project_name = path_parts[0]
    file_name = path_parts[-1]

    # Find title - fallback to filename without .html
    title = process_name(file_name[:-5])

    # Find title - the name of the project if it is in
    for url, page_name in all_pages:
        if url == project_path:
            title = page_name
            break

    # Join the remaining path parts to get the folder structure
    subfolders = "/".join(path_parts[1:-1])

    path = f"{project_name}/{subfolders}/{file_name}"

    # Render the template with the appropriate folder structure
    return render_template(path, side_menu_content=side_menu_content, title=title)


@app.route(f'/../Feedback/<path:step_file>')
def feedback_steps(step_file):
    return render_template(step_file)


@app.route('/portfolio')
def portfolio():
    return render_template(f"/portfolio.html")


if __name__ == '__main__':

    debug = True

    def open_sass_watcher_thread():
        # Function to create the thread holding the SASS watcher
        def sass_watcher_thread():
            sass_watcher_process = subprocess.Popen(
                ['python', 'static/python/sass_watcher.py', scss_Folder, css_Folder], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            sass_watcher_process.communicate()

        # Create a thread to run the SASS watcher
        watcher_thread = threading.Thread(target=sass_watcher_thread)
        watcher_thread.daemon = True  # Exit the thread when the main program exits
        watcher_thread.start()

    open_sass_watcher_thread()

    # Run the app
    app.run(debug=debug)
