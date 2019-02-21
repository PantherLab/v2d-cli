from pathlib import Path

DIR_NAME = '.unicode'


def file_exists(path):
    file = Path(path)
    return file.is_file()


def dir_exists(path):
    file = Path(path)
    return file.is_dir()


def create_home_directory():
    home = Path.home()
    full_path = home.joinpath(DIR_NAME)
    full_path.mkdir(exist_ok=True, parents=True)


def join(file):
    return home_directory().joinpath(file)


def exists_file_home(file):
    return file_exists(home_directory().joinpath(file))


def exists_dir_home(dir):
    return dir_exists(home_directory().joinpath(dir))


def home_directory():
    return Path.home().joinpath(DIR_NAME)
