import PyQt5.QtWidgets as qt

from graph_editor.editor_window import EditorWindow
from graph_editor.file import TextFile
from graph_editor.last_file_button import LastFileButton


class MainFunc:
    def __init__(self, main_window):
        self.main_window = main_window
        self.current_old_buttons = list()

    def open_button_func(self):
        file_name = qt.QFileDialog.getOpenFileName(self.main_window,
                                                   'Открыть файл')

        text_file = TextFile(file_name[0])
        self.main_window.open_docs.update({
            file_name[0]: EditorWindow(text_file,
                                       self.main_window)
        })
        self.main_window.history.update_history(text_file)
        self.init_last_uses()

    def create_button_func(self):
        dir_name = qt.QFileDialog.getExistingDirectory(self.main_window,
                                                       'Выберете папку')
        file_name = qt.QInputDialog.getText(self.main_window, 'Имя файла',
                                            'Введите имя файла:')
        file_path = dir_name[0] + file_name[0]

        text_file = TextFile(file_path)
        self.main_window.open_docs.update({
            file_path: EditorWindow(text_file,
                                    self.main_window, True)
        })
        self.main_window.history.update_history(text_file)
        self.init_last_uses()

    def close_button_func(self):
        for file in self.main_window.open_docs:
            self.main_window.open_docs[file].ed_close(False)
        self.main_window.close()

    def init_last_uses(self):
        buttons = list()
        for line in self.main_window.history.history:
            buttons.append(LastFileButton(line, self.main_window))

        self._remove_old_buttons()

        for button in buttons:
            self.main_window.last_use_layout.addWidget(button)
        self.current_old_buttons = buttons

    def _remove_old_buttons(self):
        for button in self.current_old_buttons:
            button.close()
