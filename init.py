from static.python.full_sass import do_full_sass
import os
import subprocess

scss_Folder = 'static/scss'
css_Folder = 'static/css'

if __name__=='__main__':
    
    def do_initialize():
        os.system('pip install -r requirements.txt')
        os.system('npm install')
        try:
            subprocess.check_call('sass', shell=True)
            do_full_sass()
        except subprocess.CalledProcessError:
            print("Error: 'sass' is not recognized as a command.")
            # os.system()
            print("Need sass variable in PATH!")

    def do_full_sass():
       os.system(f'py static/python/full_sass.py {scss_Folder} {css_Folder}')
        
    _ = "New-Item -Path $profile -Type File -Force"
    _ = "notepad $PROFILE"

    do_initialize()
   



