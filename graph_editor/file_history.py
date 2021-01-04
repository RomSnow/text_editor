from graph_editor.file import TextFile


class UsingHistory:
    def __init__(self, history_file: str, hist_lim: int):
        self._history = list()
        self.history_file = history_file
        self._init_history(history_file)
        self._lim = hist_lim

    def _init_history(self, file: str):
        with open(file, 'r') as file:
            for line in file:
                self._history.append(TextFile(line))

    def update_history(self, new_file: TextFile):
        if new_file in self._history:
            self._history.remove(new_file)

        if len(self._history) == self._lim:
            self._history.pop(0)

        self._history.append(new_file)

    def save_history(self):
        with open(self.history_file, 'w') as file:
            for line in self._history:
                file.write(f'{line.path}')

    @property
    def history(self) -> list:
        return self._history
