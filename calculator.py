from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import re

"""
Simple desktop calculator with basic calculator functions built in. 
"""


class Calculator(QDialog):

    def __init__(self):
        QDialog.__init__(self)

        self.ready = True
        """
        The ready attribute indicates helps separate between different calculations. It is modified when the evaluation
        button is clicked and re-set to True when any other button is clicked
        """

        self.buffer = ''
        """
        The buffer attribute is all the data (numbers, decimal sign, operators) that the user has included in their 
        current calculation so far.
        """

        self.setStyleSheet('background-color: #A9A9A9;'
                           'font-family: Century Gothic;'
                           'font-size: 35pt;'
                           )

        layout = QGridLayout()
        """
        This is one of four generic layouts for a PyQt app, most suited for a calculator imo.
        """

        self.setGeometry(500, 200, 300, 300)
        """
        The first two params determine the windows' position on the screen, the latter two determine it's default size.
        
        The widget below serves as a display for user input and evaluation.
        """
        self.display = QLineEdit()
        self.display.setMinimumHeight(60)
        self.display.setMaximumHeight(70)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setText('0')
        self.display.setStyleSheet('background-color: #E6E6FA; '
                                   'border-color: grey; '
                                   'border-width: 5px; '
                                   'border-style: outset;')

        """
        Below are the widgets under the buttons seen in the main window.
        """
        icon1 = QPixmap('undo.png')
        button_undo = QPushButton()
        button_undo.clicked.connect(self.undo_input)
        button_undo.setIcon(QIcon(icon1))
        button_undo.setIconSize(QSize(60, 60))

        button_1 = QPushButton('1')
        button_1.clicked.connect(lambda: self.input_value(1))

        button_2 = QPushButton('2')
        button_2.clicked.connect(lambda: self.input_value(2))

        button_3 = QPushButton('3')
        button_3.clicked.connect(lambda: self.input_value(3))

        button_4 = QPushButton('4')
        button_4.clicked.connect(lambda: self.input_value(4))

        button_5 = QPushButton('5')
        button_5.clicked.connect(lambda: self.input_value(5))

        button_6 = QPushButton('6')
        button_6.clicked.connect(lambda: self.input_value(6))

        button_7 = QPushButton('7')
        button_7.clicked.connect(lambda: self.input_value(7))

        button_8 = QPushButton('8')
        button_8.clicked.connect(lambda: self.input_value(8))

        button_9 = QPushButton('9')
        button_9.clicked.connect(lambda: self.input_value(9))

        button_0 = QPushButton('0')
        button_0.clicked.connect(lambda: self.input_value(0))

        button_plus = QPushButton('+')
        button_plus.clicked.connect(lambda: self.input_operator('+'))

        button_minus = QPushButton('-')
        button_minus.clicked.connect(lambda: self.input_operator('-'))

        button_multi = QPushButton('x')
        button_multi.clicked.connect(lambda: self.input_operator('*'))

        button_div = QPushButton('/')
        button_div.clicked.connect(lambda: self.input_operator('/'))

        button_decimal = QPushButton('.')
        button_decimal.clicked.connect(lambda: self.input_decimal('.'))

        button_clear = QPushButton('C')
        button_clear.clicked.connect(self.clear_buffer)

        button_equals = QPushButton('=')
        button_equals.setMinimumHeight(50)
        button_equals.clicked.connect(self.evaluate)

        """
        The below lines serve to position all the widgets created above within the layout. The first two params are the
        row/column positions, the latter two (wherever used) indicate the span of a widget.
        """
        layout.addWidget(self.display, 1, 0, 1, 3)
        layout.addWidget(button_undo, 1, 3)
        layout.addWidget(button_1, 2, 0)
        layout.addWidget(button_2, 2, 1)
        layout.addWidget(button_3, 2, 2)
        layout.addWidget(button_4, 3, 0)
        layout.addWidget(button_5, 3, 1)
        layout.addWidget(button_6, 3, 2)
        layout.addWidget(button_7, 4, 0)
        layout.addWidget(button_8, 4, 1)
        layout.addWidget(button_9, 4, 2)
        layout.addWidget(button_0, 5, 1)
        layout.addWidget(button_plus, 2, 3)
        layout.addWidget(button_minus, 3, 3)
        layout.addWidget(button_multi, 4, 3)
        layout.addWidget(button_div, 5, 3)
        layout.addWidget(button_decimal, 5, 0)
        layout.addWidget(button_clear, 5, 2)
        layout.addWidget(button_equals, 6, 0, 1, 4)

        self.setLayout(layout)
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))

    def input_value(self, value):

        """
        Takes the value input by the user and adds it into the buffer string.
        If the ready attrib is True, which means that the calculator is ready to start a new input series, the value
        is added onto the buffer string.
        Else, for example just after the evaluate button was pushed, the method will replace the buffer with newest user
        input, re-set the ready attrib and the program will interpret this as a new calculation being started by the
        user.
        """
        if self.ready is True:
            try:
                if re.split('[-+/*]', self.buffer)[-1] == '0':
                    return
            except IndexError:
                pass

            self.buffer += str(value)
            self.display.setText(self.buffer)
        else:
            try:
                if re.split('[-+/*]', self.buffer)[-1] == '0':
                    return
            except IndexError:
                pass

            self.buffer = str(value)
            self.display.setText(self.buffer)
            self.ready = True

    def input_operator(self, operator):

        """
        Takes the operator and adds it onto the buffer string if the buffer string ends with a digit. Else,
        it replaces the operator/decimal separator currently at the end of the buffer string.
        If the buffer is empty, the operator is not added.
        """
        if self.buffer == '':
            if operator == '-':
                self.buffer += operator
                self.display.setText(self.buffer)
        if self.buffer[-1].isdigit():
            self.buffer += operator
            self.display.setText(self.buffer)
            self.ready = True
        else:
            self.buffer = self.buffer[:-1] + operator
            self.display.setText(self.buffer)
            self.ready = True

    def input_decimal(self, decimal):

        """
        Places a decimal operator at the end of the buffer string on the condition that the decimal
        separator is not already present in the buffer string.
        """
        try:
            if decimal not in re.split('[-+/*]', self.buffer)[-1] and re.split('[-+/*]', self.buffer)[-1]:
                self.input_operator(decimal)
        except IndexError:
            QMessageBox.warning(self, 'Error',
                                '<font size=1> Input some numbers first. </font>')

    def evaluate(self):

        """
        Uses the eval() built in function to calculate the contents of the buffer string if it is in fact possible
        based on the buffer string syntax.
        """
        try:
            result = str(round(eval(self.buffer), 8))
            self.buffer = result
            self.display.setText(result)
            self.ready = False
        except SyntaxError:
            QMessageBox.warning(self, 'Error',
                                '<font size=1> Can\'t evaluate, input some numbers and try again. </font>')
        except ZeroDivisionError:
            QMessageBox.warning(self, 'Error',
                                '<font size=1> Can\'t divide by zero. </font>')

    def clear_buffer(self):

        """
        Clears the buffer string.
        """
        self.buffer = ''
        self.display.setText('0')

    def undo_input(self):

        """
        Removes the symbols input by the user into the buffer string on the condition that the ready attrib is True
        which indicates that the user is currently in the course of a calculation. Does not remove symbols from buffer
        string if a calculation's been completed (after the evaluation button is clicked).
        """
        if self.ready is True:
            if len(self.buffer) <= 1:
                self.buffer = ''
                self.display.setText('0')
            else:
                self.buffer = self.buffer[:-1]
                self.display.setText(self.buffer)
        else:
            pass


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Calculator")
    window = Calculator()
    window.show()
    app.exec_()
