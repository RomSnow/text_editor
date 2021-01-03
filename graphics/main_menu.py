from PyQt5 import QtCore, QtGui, QtWidgets

from graphics.main_window_func import MainFunc


class MainWindow(object):
    def __init__(self):
        self.main_window = QtWidgets.QMainWindow()
        self.main_window.open_docs = dict()
        self.main_func = MainFunc(self.main_window)
        self.setupUi(self.main_window)
        self.main_window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(812, 515)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # open_button
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setGeometry(QtCore.QRect(30, 90, 281, 91))
        self.open_button.setObjectName("open_button")
        self.open_button.clicked.connect(self.main_func.open_button_func)
        # create_button
        self.create_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_button.setGeometry(QtCore.QRect(30, 200, 281, 91))
        self.create_button.setObjectName("create_button")
        self.create_button.clicked.connect(self.main_func.create_button_func)
        # label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 10, 341, 91))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(369, 89, 401, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        # last_use_layout
        self.last_use_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.last_use_layout.setContentsMargins(0, 0, 0, 0)
        self.last_use_layout.setObjectName("last_use_layout")
        # close_button
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(30, 380, 281, 91))
        self.close_button.setObjectName("close_button")
        self.close_button.clicked.connect(self.main_func.close_button_func)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Текстовый редактор"))
        self.open_button.setText(_translate("MainWindow", "Открыть"))
        self.create_button.setText(_translate("MainWindow", "Создать"))
        self.label.setText(_translate("MainWindow", "Последние открытые документы:"))
        self.close_button.setText(_translate("MainWindow", "Закрыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    sys.exit(app.exec_())
