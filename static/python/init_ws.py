import threading
import subprocess
import os
import argparse


# Define the paths of the css and scss folders
scss_Folder = 'static/scss'
css_Folder = 'static/css'


if __name__=='__main__':


    def do_initialize():
        os.system('pip install -r requirements.txt')
        os.system('npm install')


    def do_full_sass():
        print(f"Preprocessing all .scss files in {scss_Folder}.")
        os.system(f"sass --embed-source-map --update {scss_Folder}:{css_Folder}")
        print(f"Finished preprocessing all .scss files in {scss_Folder}.")



    parser = argparse.ArgumentParser(
        prog='Initialize Workspace',
        description='Generates neccecary files and modules for workspace.'
    )
    

    group = parser.add_mutually_exclusive_group()

    group.add_argument('-i', '--init', action='store_true', help='Initialize venv, install python and node modules.')
    group.add_argument('-f', '--full', action='store_true', help=f'Update all changed .scss files in {scss_Folder}.')
    

    args = parser.parse_args()


    if args.init:
       do_initialize()
       
    do_full_sass()



