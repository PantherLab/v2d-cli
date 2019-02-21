import requests
from tqdm import tqdm
import math
import zipfile
from .files import create_home_directory, dir_exists, home_directory
from .files import exists_file_home, join, exists_dir_home


def download_confusables(version='1.0.0', filename='confusables-75.pickle'):
    if not dir_exists(home_directory()):
        create_home_directory()
    if not exists_file_home(filename):
        url = ('https://github.com/next-security-lab/deep-confusables-similarity/'
               'releases/download/{}/{}').format(version, filename)
        response = requests.get(url, stream=True)
        size = int(response.headers.get('content-length', 0))
        block_size = 1024
        wrote = 0

        with open(str(join(filename)), 'wb') as f:
            for data in tqdm(response.iter_content(block_size),
                             total=math.ceil(size//block_size),
                             unit='KB', unit_scale=True):
                wrote = wrote + len(data)
                f.write(data)

            if size != 0 and wrote != size:
                print('It was an error!')

    return str(join(filename))


def unzip(filename, output):
    if(exists_file_home(filename) and not exists_dir_home(output)):
        zip = zipfile.ZipFile(filename, 'r')
        zip.extractall(output)
        zip.close()
