from app import css_Folder, scss_Folder
import os


if __name__ == "__main__":
    os.system(f'sass --watch --embed-source-map {scss_Folder}:{css_Folder}')