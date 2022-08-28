# import sys
# from PyQt5.QtWidgets import (
#     QApplication,
#     QWidget,
#     QLabel,
#     QPushButton,
#     QLineEdit,
#     QComboBox,
#     QRadioButton,
#     QHBoxLayout, # Горизонтальный layout
#     QVBoxLayout, # Вертикальное размещение
#     QGridLayout, # сеточное размещение
#     QFormLayout,
#     QDialog,
#     QDialogButtonBox,
#     QMainWindow,
#     QToolBar,
#     QStatusBar
# )

#
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle('Hello World')
# window.setGeometry(50, 50, 300, 300)
#
# message = QLabel('<h1>Hello world label</h1>', parent=window)
# message.move(50, 50)
#
# button = QPushButton('click', parent=window)  # создаем кнопку
# button.move(50, 100)
#
# edit = QLineEdit('Text', parent=window)  # создаем место для ввода данных
# edit.move(50, 150)
#
# combo = QComboBox(parent=window)
# combo.addItems(['python', 'Java', 'Go', 'Java Script'])
# combo.move(200, 100)
#
# radio = QRadioButton('Python', parent=window)
# radio.move(200, 150)
#
# window.show()
#
# sys.exit(app.exec_())

# # 1. Horizontal Layout
#
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle('Horizontal')
# #window.setGeometry(50, 50, 300, 300)
#
# layout = QHBoxLayout()
#
# layout.addWidget(QPushButton('left', parent=window))  # создаем кнопку
# layout.addWidget(QPushButton('middle', parent=window))
# layout.addWidget(QPushButton('right', parent=window))
# layout.addWidget(QLabel('Bye - Bye!!!', parent=window))
#
# window.setLayout(layout)
# window.show()
#
# sys.exit(app.exec_())


# # 2. Vertical Layout   Вертикальное автоматическое размещение и положение
#
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle('Horizontal')
# #window.setGeometry(50, 50, 300, 300)
#
# layout = QVBoxLayout()
#
# layout.addWidget(QPushButton('left', parent=window))  # создаем кнопку
# layout.addWidget(QPushButton('middle', parent=window))
# layout.addWidget(QPushButton('right', parent=window))
# layout.addWidget(QLabel('Bye - Bye!!!', parent=window))
#
# window.setLayout(layout)
# window.show()
#
# sys.exit(app.exec_())

# # 3. Grid layout
#
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle('Grid')
#
# #создаем кнопки с указанием номера стороки и столбца
#
# layout = QGridLayout()
# layout.addWidget(QPushButton('button'), 0, 0) #1- цифра: ряд 2 - цифра: колонка
# layout.addWidget(QPushButton('button'), 0, 1)
# layout.addWidget(QPushButton('button'), 0, 2)
# layout.addWidget(QPushButton('button'), 1, 0)
# layout.addWidget(QPushButton('button'), 1, 1)
# layout.addWidget(QPushButton('button'), 1, 2)
# layout.addWidget(QPushButton('button'), 2, 0)
# layout.addWidget(QPushButton('button'), 2, 1, 1, 2) # широкая кнопка (от какой
#                                                     # до какой кнопки
#
# window.setLayout(layout)
#
# window.show()
#
# sys.exit(app.exec_())


# # Form layout  Создание формы для заполнения
#
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle('Form')
#
# layout = QFormLayout()
# layout.addRow('Name', QLineEdit())
# layout.addRow('Age', QLineEdit())
# layout.addRow('Education', QLineEdit())
# layout.addRow('Job', QLineEdit())
# layout.addRow('Hobbies', QLineEdit())
# layout.addWidget(QPushButton('Submit'))
#
#
# window.setLayout(layout)
#
# window.show()
#
# sys.exit(app.exec_())

# # Диалоговое окно
#
# class Dialog(QDialog):
#
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle('Dialog Window')
#         box_layout = QVBoxLayout()
#         form_layout = QFormLayout()
#         form_layout.addRow('Name', QLineEdit())
#         form_layout.addRow('Age', QLineEdit())
#         form_layout.addRow('Education', QLineEdit())
#         form_layout.addRow('Job', QLineEdit())
#
#         box_layout.addLayout(form_layout)
#
#         buttons = QDialogButtonBox()
#
#         buttons.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
#         box_layout.addWidget(buttons)
#         self.setLayout(box_layout)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     dialog = Dialog()
#     dialog.show()
#     sys.exit(app.exec_())


# # Main Window Главное окно
#
# class MyWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle('My Window')
#         self.setCentralWidget(QLabel('Central title'))
#         self._create_menu()
#         self._create_tool_bar()
#         self._create_status_bar()
#
#     def _create_menu(self):
#         self.menu = self.menuBar().addMenu('Menu')
#         self.menu.addMenu('Edit')
#         self.menu.addAction('Exit', self.close)
#         self.menu.addAction('Hello', self.adjustSize)
#
#     def _create_tool_bar(self):
#         tools = QToolBar()
#         self.addToolBar(tools)
#         tools.addAction('Exit', self.close)
#
#     def _create_status_bar(self):
#         status = QStatusBar()
#         status.showMessage('Some message')
#         self.setStatusBar(status)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.setGeometry(50, 50, 300, 300)
#     window.show()
#     sys.exit(app.exec_())


# # Signals  Сигналы
#
# def greeting():
#     if message.text():
#         message.setText('')
#     else:
#         message.setText('Hello')
#
# app = QApplication(sys.argv)
# window = QWidget()
# window.setWindowTitle('Signals')
#
# layout = QVBoxLayout()
# button = QPushButton('GREET')
#
# button.clicked.connect(greeting)  # отлови клик
#
# layout.addWidget(button)
# message = QLabel('')
# layout.addWidget(message)
# window.setLayout(layout)
#
# window.show()
# sys.exit(app.exec_())


############################################################################

# Calculator

import sys
from functools import partial

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QLineEdit,
    QGridLayout,
    QPushButton

)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

ERROR = 'Error'

class Calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.setFixedSize(500, 500)
        self.general_layout = QVBoxLayout()

        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)
        self._central_widget.setLayout(self.general_layout)
        self._create_display() # создание дисплея
        self._create_button()


    def _create_display(self):  # Создание дисплея
        self.display = QLineEdit()
        self.display.setFixedHeight(150)
        self.display.setAlignment(Qt.AlignLeft)
        self.display.setReadOnly(True) #ввод только с кнопок
        self.display.setFont(QFont('Times', 32))
        self.general_layout.addWidget(self.display)


    def _create_button(self):
        self.button = {}
        button_layout = QGridLayout()
        button = {
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            '/': (0, 3),
            'C': (0, 4),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '*': (1, 3),
            '(': (1, 4),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '-': (2, 3),
            ')': (2, 4),
            '0': (3, 0),
            '00': (3, 1),
            '.': (3, 2),
            '+': (3, 3),
            '=': (3, 4)
        }
        for button_text, position in button.items():
            self.button[button_text] = QPushButton(button_text)
            self.button[button_text].setFixedSize(80, 80)
            self.button[button_text].setFont(QFont('Times', 12))
            button_layout.addWidget(self.button[button_text], position[0],
                                     position[1])

            self.general_layout.addLayout(button_layout)

    def set_display_text(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def display_text(self):
        return self.display.text()

    def clear_display(self):
        self.set_display_text('')


class CalculatorController:
    def __init__(self, window, function):
        self._window = window
        self._evaluate = function

        self._connect_signals()

    def _build_expression(self, symbol):
        if self._window.display_text() == ERROR:
            self._window.clear_display()

        expression = self._window.display_text() + symbol
        self._window.set_display_text(expression)

    def _connect_signals(self):
        for button_text, but in self._window.button.items():
            if button_text not in {'=', 'C'}:
                but.clicked.connect(
                    partial(self._build_expression, button_text)
                )
        self._window.button['='].clicked.connect(self._calculate_result) #
        self._window.display.returnPressed.connect(self._calculate_result) #
        self._window.button['C'].clicked.connect(self._window.clear_display)

    def _calculate_result(self):
        result = self._evaluate(expression=self._window.display_text())
        self._window.set_display_text(result)


def evaluate_expression(expression):
    try:
        result = str(eval(expression))
    except Exception:
        result = ERROR

    return result


def main():
    calculator = QApplication(sys.argv)
    window = Calculator()
    window.show()
    CalculatorController(window=window, function=evaluate_expression)

    sys.exit(calculator.exec_())


if __name__ == '__main__':
    main()