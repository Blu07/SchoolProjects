from static.python.full_sass import do_full_sass
import os

scss_Folder = 'static/scss'
css_Folder = 'static/css'

if __name__=='__main__':
    
    def do_initialize():
        os.system('pip install -r requirements.txt')
        os.system('npm install')


    def do_full_sass():
       os.system(f"'py', 'static/python/full_sass.py', {scss_Folder}, {css_Folder}")
        


    do_initialize()
    do_full_sass()



