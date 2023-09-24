from app import css_Folder, scss_Folder
from full_sass import do_full_sass
import os


if __name__ == "__main__":
    
    def start_sass_watcher():
        os.system(f'sass --watch --embed-source-map {scss_Folder}:{css_Folder}')


    do_full_sass()
    start_sass_watcher()