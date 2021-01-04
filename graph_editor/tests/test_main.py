import os
import unittest

from PyQt5.QtWidgets import QApplication

from graph_editor.main_menu import MainWindow
from graph_editor.main_window_func import MainFunc


class MainFuncTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = QApplication([])
        self.main_window = MainWindow()
        self.main_window.main_window.is_debug = True
        self.func = MainFunc(self.main_window.main_window)

    def test_open(self):
        self.func.open_button_func()
        self.assertTrue(self.main_window
                        .main_window.open_docs)

    def test_create(self):
        self.func.create_button_func()
        self.assertTrue(os.path.isfile(
            f'{os.path.dirname(__file__)}/../test.my'))
        os.remove(f'{os.path.dirname(__file__)}/../test.my')

    def test_init_history(self):
        self.func.init_last_uses()
        self.assertFalse(self.func.current_old_buttons)

    def test_close_all(self):
        self.func.close_button_func()
        self.assertFalse(self.main_window.main_window.open_docs)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MainFuncTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)