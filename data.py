import os
import shutil
import eel


@eel.expose
def get_data_folder() -> str:
    return os.path.dirname(__file__)+"\\data"


@eel.expose
def copyfile(src, subclass: str, path: str = get_data_folder()):
    """
    Copy the file to the data directory and its subclass
    """

    shutil.copy(src, path + subclass)


@eel.expose
def get_path_infos(path):
    try:
        files = os.listdir(path)
        real_files = [f for f in files if os.path.isfile(
            os.path.join(path, f))]
        real_dirs = [f for f in files if os.path.isdir(os.path.join(path, f))]

    except PermissionError:
        eel.alert_error("Can't read this files")
        return {"dirs": [], "files": []}

    except Exception as e:
        # do some things
        return {"dirs": [], "files": []}

    return {"dirs": real_dirs, "files": real_files}
