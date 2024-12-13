import os
from pathlib import Path
import uuid
import tempfile
import os
from utils.Singleton import Singleton


class FileService(metaclass=Singleton):

    def save(self, folder, file, filename):
        os.makedirs(folder, exist_ok=True)
        file_path: Path = Path(folder / filename)
        file.save(file_path)

    def create_temp_dir(self) -> Path:
        temp_folder = Path(tempfile.gettempdir(), str(uuid.uuid4()))
        os.makedirs(temp_folder, exist_ok=True)
        return temp_folder

    def create_workdir(self, data_dir) -> Path:
        workdir = Path(data_dir, str(uuid.uuid4()))
        os.makedirs(workdir, exist_ok=True)
        return workdir

    def create_folder(self, workdir, folder_name) -> Path:
        folder = Path(workdir, folder_name)
        os.makedirs(folder, exist_ok=True)
        return folder

    def read_file(self, path: Path) -> str:
        content = ''
        with open(path, "r") as file:
            content = file.read()
        return content
