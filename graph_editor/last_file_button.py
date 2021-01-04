import PyQt5.QtWidgets as qt

from graph_editor.editor_window import EditorWindow
from graph_editor.file import TextFile


class LastFileButton(qt.QPushButton):
    def __init__(self, file: TextFile,
                 main_window):
        super().__init__()
        self.file = file
        self.main_window = main_window
        self.setText(file.short_name)
        self.clicked.connect(self.open_file)
        self.show()

    def open_file(self):
        self.main_window.open_docs.update({
            self.file.path: EditorWindow(self.file,
                                         self.main_window)
        })
        self.main_window.history.update_history(self.file)
        self.main_window.main_func.init_last_uses()
