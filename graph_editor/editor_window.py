import os

import PyQt5.QtWidgets as qt

from graph_editor.file import TextFile


class EditorWindow(qt.QWidget):
    def __init__(self, file: TextFile,
                 main_window,
                 create_mod=False):
        super().__init__()
        self.create_mod = create_mod
        self.file_path = file.path
        self.short_file_name = file.short_name
        self.main_window = main_window
        self._init_ui()
        self.show()
        self.is_changed = False
        self.is_start = True

    def _init_ui(self):
        self.resize(600, 800)
        self.setWindowTitle(self.short_file_name)

        main_layout = qt.QVBoxLayout()

        self.edit_area = qt.QTextEdit()
        if not self.create_mod:
            self.edit_area.setText(self._get_current_text())
        self.edit_area.textChanged.connect(self._change_text)
        main_layout.addWidget(self.edit_area)

        button_layout = qt.QHBoxLayout()
        save_button = qt.QPushButton('Сохранить')
        save_button.clicked.connect(self._save_text)

        save_as_button = qt.QPushButton('Сохранить как')
        save_as_button.clicked.connect(self._save_as)

        back_button = qt.QPushButton('Отменить изменения')
        back_button.clicked.connect(self._back_text)

        close_button = qt.QPushButton('Закрыть')
        close_button.clicked.connect(self.ed_close)

        button_layout.addWidget(save_button)
        button_layout.addWidget(save_as_button)
        button_layout.addWidget(back_button)
        button_layout.addWidget(close_button)

        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def _get_current_text(self) -> str:
        with open(self.file_path, 'r') as file:
            text = file.read()

        return text

    def _back_text(self):
        if not self.is_changed:
            qt.QMessageBox.question(self, 'Отменить изменения',
                                    'Нет изменений', qt.QMessageBox.Ok)
            return

        if self.create_mod:
            qt.QMessageBox.question(self, 'Отменить изменения',
                                    'Файл пустой', qt.QMessageBox.Ok)
            return

        question = qt.QMessageBox.question(self, 'Отменить изменения',
                                           'Хотите отменить все изменения?',
                                           qt.QMessageBox.Yes,
                                           qt.QMessageBox.No)

        if question == qt.QMessageBox.Yes:
            self.edit_area.setText(self._get_current_text())

    def _change_text(self):
        if not self.is_start:
            self.is_changed = True
        else:
            self.is_start = False

    def _save_as(self):
        dir_name = qt.QFileDialog.getExistingDirectory(self.main_window,
                                                       'Выберете папку')
        if not dir_name:
            return
        file_name = qt.QInputDialog.getText(self.main_window, 'Имя файла',
                                            'Введите имя файла:')
        if not file_name or not file_name[0]:
            return

        if file_name[0] in os.listdir(dir_name):
            qt.QMessageBox.question(self,
                                    'Ошибка', 'Такой файл уже существует',
                                    qt.QMessageBox.Ok)

        file_path = f'{dir_name}/{file_name[0]}'
        with open(file_path, 'w') as file:
            file.write(self.edit_area.toPlainText())

        new_file = TextFile(file_path)
        self.file_path = new_file.path
        self.short_file_name = new_file.short_name
        self.main_window.history.update_history(new_file)
        self.main_window.main_func.init_last_uses()
        self.setWindowTitle(self.short_file_name)

    def _save_text(self):
        if not self.is_changed:
            qt.QMessageBox.question(self, 'Сохранить изменения',
                                    'Нет изменений', qt.QMessageBox.Ok)
            return

        question = qt.QMessageBox.question(self, 'Сохранить изменения',
                                           'Хотите сохранить все изменения?',
                                           qt.QMessageBox.Yes,
                                           qt.QMessageBox.No)

        if question == qt.QMessageBox.Yes:
            try:
                with open(self.file_path, 'w') as file:
                    file.write(self.edit_area.toPlainText())
            except FileNotFoundError:
                question = qt.QMessageBox.question(self, 'Ошибка записи',
                                                   'Нет доступа к файлу',
                                                   qt.QMessageBox.Ok)
                self.ed_close()

        self.is_changed = False
        self.create_mod = False

    def ed_close(self, is_myself=True):
        if is_myself:
            self.main_window.open_docs.pop(self.file_path)
        self.close()

    def closeEvent(self, a0):
        self.main_window.history.save_history()
        if self.is_changed:
            self._save_text()


if __name__ == '__main__':
    app = qt.QApplication([])
    window = EditorWindow(__file__, None)
    app.exec_()
