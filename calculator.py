from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

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
        self.button_undo = QPushButton()
        self.button_undo.clicked.connect(self.undo_input)
        self.button_undo.setIcon(QIcon(icon1))
        self.button_undo.setIconSize(QSize(60, 60))

        self.button_1 = QPushButton('1')
        self.button_1.clicked.connect(lambda: self.input_value(1))

        self.button_2 = QPushButton('2')
        self.button_2.clicked.connect(lambda: self.input_value(2))

        self.button_3 = QPushButton('3')
        self.button_3.clicked.connect(lambda: self.input_value(3))

        self.button_4 = QPushButton('4')
        self.button_4.clicked.connect(lambda: self.input_value(4))

        self.button_5 = QPushButton('5')
        self.button_5.clicked.connect(lambda: self.input_value(5))

        self.button_6 = QPushButton('6')
        self.button_6.clicked.connect(lambda: self.input_value(6))

        self.button_7 = QPushButton('7')
        self.button_7.clicked.connect(lambda: self.input_value(7))

        self.button_8 = QPushButton('8')
        self.button_8.clicked.connect(lambda: self.input_value(8))

        self.button_9 = QPushButton('9')
        self.button_9.clicked.connect(lambda: self.input_value(9))

        self.button_0 = QPushButton('0')
        self.button_0.clicked.connect(lambda: self.input_value(0))

        self.button_plus = QPushButton('+')
        self.button_plus.clicked.connect(lambda: self.input_operator('+'))

        self.button_minus = QPushButton('-')
        self.button_minus.clicked.connect(lambda: self.input_operator('-'))

        self.button_multi = QPushButton('x')
        self.button_multi.clicked.connect(lambda: self.input_operator('*'))

        self.button_div = QPushButton('/')
        self.button_div.clicked.connect(lambda: self.input_operator('/'))

        self.button_decimal = QPushButton('.')
        self.button_decimal.clicked.connect(lambda: self.input_decimal('.'))

        self.button_clear = QPushButton('C')
        self.button_clear.clicked.connect(self.clear_buffer)

        self.button_equals = QPushButton('=')
        self.button_equals.setMinimumHeight(50)
        self.button_equals.clicked.connect(self.evaluate)

        """
        The below lines serve to position all the widgets created above within the layout. The first two params are the
        row/column positions, the latter two (wherever used) indicate the span of a widget.
        """
        layout.addWidget(self.display, 1, 0, 1, 3)
        layout.addWidget(self.button_undo, 1, 3)
        layout.addWidget(self.button_1, 2, 0)
        layout.addWidget(self.button_2, 2, 1)
        layout.addWidget(self.button_3, 2, 2)
        layout.addWidget(self.button_4, 3, 0)
        layout.addWidget(self.button_5, 3, 1)
        layout.addWidget(self.button_6, 3, 2)
        layout.addWidget(self.button_7, 4, 0)
        layout.addWidget(self.button_8, 4, 1)
        layout.addWidget(self.button_9, 4, 2)
        layout.addWidget(self.button_0, 5, 1)
        layout.addWidget(self.button_plus, 2, 3)
        layout.addWidget(self.button_minus, 3, 3)
        layout.addWidget(self.button_multi, 4, 3)
        layout.addWidget(self.button_div, 5, 3)
        layout.addWidget(self.button_decimal, 5, 0)
        layout.addWidget(self.button_clear, 5, 2)
        layout.addWidget(self.button_equals, 6, 0, 1, 4)

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
            self.buffer += str(value)
            self.display.setText(self.buffer)
        else:
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
            return
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
        if decimal not in self.buffer:
            self.input_operator(decimal)
        else:
            return

    def evaluate(self):

        """
        Uses the eval() built in function to calculate the contents of the buffer string if it is in fact possible
        based on the buffer string syntax.
        """
        try:
            result = str(eval(self.buffer))
            self.buffer = result
            self.display.setText(result)
            self.ready = False
        except SyntaxError:
            pass

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
            return


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Calculator")
    window = Calculator()
    window.show()
    app.exec_()
