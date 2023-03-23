from os.path import splitext

class Image():
    def __init__(self, root: str, file: str):
        self.root = root
        self.name = splitext(file)[0]
        self.extension = splitext(file)[1].replace('.', '').lower()
