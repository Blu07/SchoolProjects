from app import css_Folder, scss_Folder
import os


if __name__ == "__main__":
    def do_full_sass():
        print(f"Preprocessing all .scss files in {scss_Folder}.")
        os.system(f"sass --embed-source-map --update {scss_Folder}:{css_Folder}")
        print(f"Finished preprocessing all .scss files in {scss_Folder}.")


    do_full_sass()