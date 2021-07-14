import os


class LangLoader:

    def __init__(self, path_to_lang: str):
        self._path = path_to_lang
        self._dirs = os.listdir(self._path)
        self._data = {}
        for dir in ['__pycache__', '__init__.py']:
             self._dirs.remove(dir)

        for dir in self._dirs:

            path_to_module = self._path.replace('/', '.')[2:] + f'.{dir}'

            self._data[dir] = __import__(path_to_module, globals(), locals(), [dir], 0)

    def __getitem__(self, item) -> __import__:
        return self._data[item]
