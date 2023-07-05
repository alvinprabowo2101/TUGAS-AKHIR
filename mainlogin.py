import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from login import Ui_LOGINN
from register import Ui_REGISTERR
from menu import Ui_MENU
from menu2 import Ui_SEMUA
from menu3 import Ui_MainWindow
import webbrowser


class MenuUtama(QMainWindow, Ui_MENU):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.LOGOUT.clicked.connect(self.logout)
        self.LIHATSEMUA.clicked.connect(self.open_menu_film)
        self.FILM1.clicked.connect(self.open_menu_video)

    def open_menu_film(self):
        self.menu_film = MenuFilm()
        self.menu_film.show()
        self.hide()

    def logout(self):
        self.login_form = LoginForm()
        self.login_form.show()
        self.hide()

    def open_menu_video(self):
        self.menu_video = MenuVideo()
        self.menu_video.show()
        self.hide()


class MenuFilm(QMainWindow, Ui_SEMUA):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.LOGOUT.clicked.connect(self.logout)
        self.LOGO_2.clicked.connect(self.open_menu_film)
        self.FILM1.clicked.connect(self.open_menu_video)

    def open_menu_film(self):
        self.menu_film = MenuUtama()
        self.menu_film.show()
        self.hide()

    def logout(self):
        self.login_form = LoginForm()
        self.login_form.show()
        self.hide()

    def open_menu_video(self):
        self.menu_video = MenuVideo()
        self.menu_video.show()
        self.hide()


class RegisterForm(QMainWindow, Ui_REGISTERR):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.LOGIN.clicked.connect(self.open_login)

    def open_login(self):
        self.login_form.show()
        self.hide()


class MenuVideo(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.LOGO_3.clicked.connect(self.open_menu_film)
        self.LOGOUT_2.clicked.connect(self.logout)

    def open_menu_film(self):
        self.menu_film = MenuUtama()
        self.menu_film.show()
        self.hide()

    def logout(self):
        self.login_form = LoginForm()
        self.login_form.show()
        self.hide()


class LoginForm(QMainWindow, Ui_LOGINN):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.LOGIN.clicked.connect(self.login)
        self.IG.clicked.connect(self.open_instagram1)
        self.IGG.clicked.connect(self.open_instagram2)
        self.IGGG.clicked.connect(self.open_instagram3)
        self.REGISTER.clicked.connect(self.open_register)
        self.CL.clicked.connect(self.close)

    def open_instagram1(self):
        self.menu_form = MenuUtama()
        self.menu_form.login_form = self
        webbrowser.open("https://www.instagram.com/iamjaisywoii/")

    def open_instagram2(self):
        self.menu_form = MenuUtama()
        self.menu_form.login_form = self
        webbrowser.open("https://www.instagram.com/ro_bintang22/")

    def open_instagram3(self):
        self.menu_form = MenuUtama()
        self.menu_form.login_form = self
        webbrowser.open("https://www.instagram.com/alvinpbw/")

    def login(self):
        username = self.USERNAME.text()
        password = self.PASSWORD.text()
        if username == "admin" and password == "admin":
            if hasattr(self, 'menu_form'):
                self.menu_form.show()
            else:
                self.open_menu()
            self.hide()
        else:
            self.show_error_message("Username atau password salah.")

    def open_menu(self):
        self.menu_form = MenuUtama()
        self.menu_form.login_form = self
        self.menu_form.show()
        self.hide()

    def open_register(self):
        self.register_form = RegisterForm()
        self.register_form.login_form = self
        self.register_form.show()
        self.hide()

    def show_error_message(self, message):
        error_dialog = QtWidgets.QMessageBox()
        error_dialog.setIcon(QtWidgets.QMessageBox.Warning)
        error_dialog.setText(message)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_form = LoginForm()
    login_form.show()
    sys.exit(app.exec_())
