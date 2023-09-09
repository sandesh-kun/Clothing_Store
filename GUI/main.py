import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from login_gui import LoginWindow
from registration_gui import RegistrationWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Clothing Store")
        self.setGeometry(100, 100, 800, 600)

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Navigation Bar
        nav_layout = QHBoxLayout()
        home_button = QPushButton("Home")
        login_button = QPushButton("Login")
        registration_button = QPushButton("Registration")
        cart_button = QPushButton("Add to Cart")

        nav_layout.addWidget(home_button)
        nav_layout.addWidget(login_button)
        nav_layout.addWidget(registration_button)
        nav_layout.addStretch(1)
        nav_layout.addWidget(cart_button)

        main_layout.addLayout(nav_layout)

        # Display Images and Prices Horizontally
        image_hlayout = QHBoxLayout()
        row_layout = QVBoxLayout()  # Layout for each row
        row_item_count = 0

        for image_path, price in [("shirt.jpg", "1000"), ("shirt.jpg", "1500"), ("shirt.jpg", "2000"), ("shirt.jpg", "2500"), ("shirt.jpg", "3000")]:
            if row_item_count >= 3:
                image_hlayout.addLayout(row_layout)
                row_layout = QVBoxLayout()
                row_item_count = 0

            image_layout = QVBoxLayout()

            pixmap = QPixmap(image_path)
            image_label = QLabel()
            image_label.setPixmap(pixmap)
            image_label.setAlignment(Qt.AlignCenter)
            image_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            image_layout.addWidget(image_label)

            price_label = QLabel(f"Price: Rs. {price}")
            price_label.setAlignment(Qt.AlignCenter)
            image_layout.addWidget(price_label)

            try_on_button = QPushButton("Try On")
            try_on_button.setStyleSheet("text-align: center;")
            image_layout.addWidget(try_on_button)

            buy_button = QPushButton("Buy")
            buy_button.setStyleSheet("text-align: center;")
            image_layout.addWidget(buy_button)

            row_layout.addLayout(image_layout)
            row_item_count += 1

        if row_item_count > 0:
            image_hlayout.addLayout(row_layout)

        main_layout.addLayout(image_hlayout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Connect buttons to functions
        home_button.clicked.connect(self.show_home)
        login_button.clicked.connect(self.show_login)
        registration_button.clicked.connect(self.show_registration)
        cart_button.clicked.connect(self.show_cart)

    def show_home(self):
        pass

    def show_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()

    def show_registration(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.show()

    def show_cart(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
