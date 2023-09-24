import os
import argparse

def do_full_sass(scss_Folder, css_Folder):
    print(f"Preprocessing all .scss files in {scss_Folder}.")
    os.system(f"sass --embed-source-map --update {scss_Folder}:{css_Folder}")
    print(f"Finished preprocessing all .scss files in {scss_Folder}.")


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(prog='Receive scss/css Filepaths')

    parser.add_argument('scss_path', required=True, help='String of the scss filepath in the workspace.')
    parser.add_argument('css_path', required=True, help='String of the scss filepath in the workspace.')

    args = parser.parse_args()

    do_full_sass(args.scss_path, args.css_path)