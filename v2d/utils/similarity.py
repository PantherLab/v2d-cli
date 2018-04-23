import pickle
from .files import exists_file_home
from .images import download_confusables, join


def load_file(threshold=75):
    path = str(join('confusables-{}.pickle'.format(threshold)))
    filepath = 'confusables-{}.pickle'.format(threshold)
    if not exists_file_home(path):
        path = download_confusables(filename=filepath)

    with open(path, 'rb') as f:
        return pickle.load(f)
