from static.python.full_sass import do_full_sass
import os

if __name__=='__main__':
    
    def do_initialize():
        os.system('pip install -r requirements.txt')
        os.system('npm install')


    def do_full_sass():
       os.system('py', 'static/python/full_sass.py')
        


    do_initialize()
    do_full_sass()



