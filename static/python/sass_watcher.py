from full_sass import do_full_sass
import os
import argparse

def start_sass_watcher(scss_Folder, css_Folder):
    os.system(f'sass --watch --embed-source-map {scss_Folder}:{css_Folder}')


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(prog='Receive scss/css Filepaths')

    parser.add_argument('scss_path', help='String of the scss filepath in the workspace.')
    parser.add_argument('css_path', help='String of the scss filepath in the workspace.')

    args = parser.parse_args()


    do_full_sass(args.scss_path, args.css_path)
    start_sass_watcher(args.scss_path, args.css_path)