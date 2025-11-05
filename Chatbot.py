import sys
from PyQt5 import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*

class ChatbotApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.txtbox = QPlainTextEdit(self)
        self.txtbox.setStyleSheet("font-size:13px;color:black;padding:10px;background-color:white;border:1px solid black;")
        self.txtbox.setGeometry(10,10,480,450)
        self.txtbox.setPlainText("Chatbot: Hello!")
        self.txtbox.setEnabled(False)

        self.user_input = QLineEdit(self)
        self.user_input.setStyleSheet("font-size:15px;padding:5px;border:1px solid black;")
        self.user_input.setGeometry(10,470,480,30)
        self.user_input.setPlaceholderText("Enter your prompt...")

        self.generate_btn = QPushButton(self)
        self.generate_btn.setStyleSheet("color:white;padding:5px;background:dodgerblue;border-radius: 2px;")
        self.generate_btn.clicked.connect(self.cb_response)
        self.generate_btn.setText("Generate")
        self.generate_btn.setGeometry(10,510,150,30)

        self.clear_btn = QPushButton(self)
        self.clear_btn.setStyleSheet("color:black;padding:5px;background:orange;border-radius: 2px;")
        self.clear_btn.clicked.connect(self.clear_chat)
        self.clear_btn.setText("Clear")
        self.clear_btn.setGeometry(175,510,150,30)

        self.exit_btn = QPushButton(self)
        self.exit_btn.setStyleSheet("padding:5px;border-radius: 2px;background-color:green;")
        self.exit_btn.clicked.connect(App.exit)
        self.exit_btn.setText("Exit")
        self.exit_btn.setGeometry(340,510,150,30)

    def cb_response(self):
        user_input = self.user_input.text().lower().strip()

        if not user_input:
            return

        self.txtbox.appendPlainText(f"You: {user_input}")

        if user_input in ["hello","hi","hey","h"]:
            reply = "Hi there!"
        elif user_input in ["how are you", "how are you?"]:
            reply = "I'm fine, thanks for asking!"
        elif user_input in ["bye","goodbye","see you"]:
            reply = "Goodbye! Have a great day!"
        else:
            reply = "Sorry, I didn't understand that."

        self.txtbox.appendPlainText(f"Chatbot: {reply}")
        self.user_input.clear()
    def clear_chat(self):
        self.txtbox.setPlainText("Chatbot: Hello!")
if __name__ == "__main__":
    App = QApplication(sys.argv)
    win = ChatbotApp()
    win.setWindowTitle("Simple rule-based Chatbot")
    win.setMinimumSize(500,550)
    win.setMaximumSize(500,550)
    win.show()
    sys.exit(App.exec())