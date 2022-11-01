from requests import get
import os
import shutil

CURRENT_DIRECTORY = os.getcwd()

def baixar_anexo(url: str, file_name: str, subdir: str) -> None:
    """Function to download a file from a given url and save it in a sub-directory"""
    print(f"Downloading {url}...")
    with open(os.path.join(CURRENT_DIRECTORY, subdir, file_name), 'wb') as f:
        f.write(get(url).content)

