import sys
import PyQt5.QtWidgets as qt

from graph_editor.main_menu import MainWindow


def main():
    app = qt.QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
