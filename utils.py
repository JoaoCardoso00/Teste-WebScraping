from requests import get
import os
import shutil

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'anexos')

def baixar_anexo(url: str, file_name: str, subdir: str) -> None:
    """Function to download a file from a given url and save it in a sub-directory"""
    print(f"Downloading {url}...")
    with open(os.path.join(current_directory, subdir, file_name), 'wb') as f:
        f.write(get(url).content)

