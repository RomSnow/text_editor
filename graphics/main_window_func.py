import PyQt5.QtWidgets as qt

from graphics.editor_window import EditorWindow


class MainFunc:
    def __init__(self, main_window):
        self.main_window = main_window

    def open_button_func(self):
        file_name = qt.QFileDialog.getOpenFileName(self.main_window,
                                                   'Открыть файл')

        self.main_window.open_docs.update({
            file_name[0]: EditorWindow(file_name[0], self.main_window)
        })

    def create_button_func(self):
        dir_name = qt.QFileDialog.getExistingDirectory(self.main_window,
                                                       'Выберете папку')
        file_name = qt.QInputDialog.getText(self.main_window, 'Имя файла',
                                            'Введите имя файла:')
        file_path = dir_name[0] + file_name[0]

        self.main_window.open_docs.update({
            file_path: EditorWindow(file_path, self.main_window, True)
        })

    def close_button_func(self):
        for file in self.main_window.open_docs:
            self.main_window.open_docs[file].ed_close(False)
        self.main_window.close()

    def init_last_uses(self):
        pass
