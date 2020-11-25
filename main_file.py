import sqlite3
import sys
import admin_file

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from Проект_QT import MainAdminWindow, PupilDialog, UserDialog, BookDialog


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('start_window.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run_login)
        self.lineEdit.textChanged.connect(self.update_button)
        self.lineEdit_2.textChanged.connect(self.update_button)
        # Обратите внимание: имя элемента такое же как в QTDesigner

        self.db = None
        self.con = None

    def run_login(self):
        self.statusBar().clearMessage()
        db = self.comboBox.currentText()
        login, password = self.lineEdit.text(), self.lineEdit_2.text()
        self.con = sqlite3.connect(db)

        if login or password:
            cur = self.con.cursor()
            exist = cur.execute(f'select type from users '
                                f'where login = "{login}" and password = "{password}"').fetchall()
            print(exist)
            if exist:
                print('Успешно')
                user_type = exist[0][0]
                if user_type == 0:
                    pass  # продолжить как ученик
                elif user_type == 1:
                    #  admin_app = QApplication(sys.argv)
                    self.admin_ex = MainAdminWindow('library.db')
                    self.admin_ex.show()
                    #  sys.exit(admin_app.exec_())

                    pass  # продолжить как админ
            else:
                self.statusBar().showMessage('login или password указаны не верно')
        else:
            pass  # продолжить как гость

    def update_button(self):
        if self.lineEdit.text() or self.lineEdit_2.text():
            self.pushButton.setText('Продолжить')
        else:
            self.pushButton.setText('Продолжить как гость')

    def admin(self, db):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())