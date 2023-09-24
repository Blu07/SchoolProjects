import os

from sass_watcher import scss_folder, css_folder



def compile_all_sass():
    for root, _, files in os.walk(scss_folder):
        for file in files:
            if file.endswith(".scss"):
                scss_path = os.path.join(root, file)
                css_path = os.path.join(css_folder, os.path.splitext(file)[0] + '.css')
                sass_command = f"sass --embed-source-map {scss_path} {css_path}"
                os.system(sass_command)


if __name__=='__main__':
    compile_all_sass()