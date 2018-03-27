import pickle
from .files import exists_file_home
from .images import download_confusables, join


def load_file(path=str(join('confusables.pickle'))):
    if not exists_file_home(path):
        path = download_confusables()

    with open(path, 'rb') as f:
        return pickle.load(f)
