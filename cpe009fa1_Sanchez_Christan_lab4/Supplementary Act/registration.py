# registration.py
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import re


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Account Registration")
        self.setGeometry(100, 100, 400, 300)

        # Set the window icon
        self.setWindowIcon(QIcon('pythonico.ico'))

        self.initUI()

    def initUI(self):
        title = QLabel("Account Registration")
        title.setAlignment(Qt.AlignCenter)

        self.first_name_label, self.first_name_input = self.create_input_field("First Name:")
        self.last_name_label, self.last_name_input = self.create_input_field("Last Name:")
        self.username_label, self.username_input = self.create_input_field("Username:")

        self.password_label, self.password_input = self.create_input_field("Password:")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.email_label, self.email_input = self.create_input_field("Email Address:")
        self.contact_number_label, self.contact_number_input = self.create_input_field("Contact Number:")

        self.submit_button = QPushButton("Submit")
        self.clear_button = QPushButton("Clear")

        self.submit_button.clicked.connect(self.submit_form)
        self.clear_button.clicked.connect(self.clear_form)

        form_layout = QVBoxLayout()
        form_layout.addWidget(title)
        form_layout.addWidget(self.first_name_label)
        form_layout.addWidget(self.first_name_input)
        form_layout.addWidget(self.last_name_label)
        form_layout.addWidget(self.last_name_input)
        form_layout.addWidget(self.username_label)
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(self.password_label)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(self.email_label)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(self.contact_number_label)
        form_layout.addWidget(self.contact_number_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.clear_button)

        form_layout.addLayout(button_layout)
        self.setLayout(form_layout)

    def create_input_field(self, label_text):
        label = QLabel(label_text)
        input_field = QLineEdit()
        input_field.setToolTip(f"Enter your {label_text.lower()}")
        return label, input_field

    def validate_email(self, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    def submit_form(self):
        if not self.validate_email(self.email_input.text()):
            QMessageBox.warning(self, "Error", "Please enter a valid email address.")
            return
        QMessageBox.information(self, "Success", "Registration successful!")

    def clear_form(self):
        self.first_name_input.clear()
        self.last_name_input.clear()
        self.username_input.clear()
        self.password_input.clear()
        self.email_input.clear()
        self.contact_number_input.clear()
