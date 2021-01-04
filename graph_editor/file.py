import re


class TextFile:
    def __init__(self, file_path: str):
        self._file_path = file_path.strip('\n')
        self._short_name = self._get_short_name()
        self._try_read()

    def _try_read(self):
        try:
            with open(self._file_path, 'r') as file:
                file.read()
        except UnicodeError:
            raise TypeError

    def _get_short_name(self) -> str:
        match = re.findall(r'[/\\]?([\w\d]+?[.]?[\w\d]+?)$', self._file_path)
        return match[0]

    @property
    def path(self):
        return self._file_path

    @property
    def short_name(self):
        return self._short_name
