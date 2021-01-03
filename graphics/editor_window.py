import PyQt5.QtWidgets as qt


class EditorWindow(qt.QWidget):
    def __init__(self, file: str,
                 main_window,
                 create_mod=False):
        super().__init__()
        self.create_mod = create_mod
        self.file = file
        self.main_window = main_window
        self._init_ui()
        self.show()
        self.is_changed = False
        self.is_start = True

    def _init_ui(self):
        self.resize(600, 800)
        self.setWindowTitle(self.file)

        main_layout = qt.QVBoxLayout()

        self.edit_area = qt.QTextEdit()
        if not self.create_mod:
            self.edit_area.setText(self._get_current_text())
        self.edit_area.textChanged.connect(self._change_text)
        main_layout.addWidget(self.edit_area)

        button_layout = qt.QHBoxLayout()
        save_button = qt.QPushButton('Сохранить')
        save_button.clicked.connect(self._save_text)

        back_button = qt.QPushButton('Отменить изменения')
        back_button.clicked.connect(self._back_text)

        close_button = qt.QPushButton('Закрыть')
        close_button.clicked.connect(self.ed_close)

        button_layout.addWidget(save_button)
        button_layout.addWidget(back_button)
        button_layout.addWidget(close_button)

        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def _get_current_text(self) -> str:
        with open(self.file, 'r') as file:
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
            with open(self.file, 'w') as file:
                file.write(self.edit_area.text())

        self.is_changed = False
        self.create_mod = False

    def ed_close(self, is_myself=True):
        if is_myself:
            self.main_window.open_docs.pop(self.file)
        self.close()

    def closeEvent(self, a0):
        if self.is_changed:
            self._save_text()


if __name__ == '__main__':
    app = qt.QApplication([])
    window = EditorWindow(__file__, None)
    app.exec_()
