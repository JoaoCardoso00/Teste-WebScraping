import requests
import os
import shutil
from bs4 import BeautifulSoup
from utils import baixar_anexo

WEBSITE_URL = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
CURRENT_DIRECTORY = os.getcwd()
SUBDIR = "anexos"
PATH_ANEXOS = os.path.join(CURRENT_DIRECTORY, SUBDIR)

def main():
    page = requests.get(WEBSITE_URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    anexos = soup.find_all(lambda tag: tag.name == 'a' and tag.get('href').endswith('.pdf') and 'Anexo' in tag.get('href'))

    if not (os.path.exists(PATH_ANEXOS)):
        os.mkdir(PATH_ANEXOS)

    for index, anexo in enumerate(anexos, start=1):
        baixar_anexo(anexo.get('href'), f'anexo-{index}.pdf', SUBDIR)

    shutil.make_archive(SUBDIR, 'zip', SUBDIR)
    shutil.rmtree(SUBDIR)

if __name__ == '__main__':
    main()