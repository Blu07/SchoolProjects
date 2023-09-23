import os
import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the paths of the css ans scss folders
scss_folder = 'static/scss'
css_folder = 'static/css'

# Define the command to compile SASS
class SASSHandler(FileSystemEventHandler):
    def on_modified(self, event):
        src_path = event.src_path
        new_file_path = f"{css_folder}/{src_path[len(scss_folder) + 1:-4]+'css'}"

        sass_command = f"sass --embed-source-map {src_path} {new_file_path}"
        print(f"Changes detected in {src_path}")
        os.system(sass_command)
        print("SASS compilation complete")



def compile_sass():
    for root, _, files in os.walk(scss_folder):
        for file in files:
            if file.endswith(".scss"):
                scss_path = os.path.join(root, file)
                css_path = os.path.join(css_folder, os.path.splitext(file)[0] + '.css')
                sass_command = f"sass --embed-source-map {scss_path} {css_path}"
                os.system(sass_command)




def main():
    
    # Check for the --full-sass command-line argument
    if len(sys.argv) > 1 and sys.argv[1] == '--full-sass':
        print(f"Preprocessing all .sass files in {scss_folder}.")
        compile_sass()
        print("Sass preprocessing complete.")
    
    
    # Create an observer that monitors the directory
    observer = Observer()
    event_handler = SASSHandler()
    observer.schedule(event_handler, path=scss_folder, recursive=False)
    
    print(f"Watching {scss_folder} for changes...")
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()



if __name__ == "__main__":
    main()
    
   