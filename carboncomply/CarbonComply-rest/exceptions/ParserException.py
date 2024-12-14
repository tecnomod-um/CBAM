from pathlib import Path


class ParserException(Exception):
    def __init__(self, file: Path, msg: str):
        self.file = file
        self.msg = msg