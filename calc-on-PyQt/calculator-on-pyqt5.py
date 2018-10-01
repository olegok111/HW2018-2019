# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QDesktopWidget, QLabel
from PyQt5.QtGui import QFont

operation_was_made = False
op = ''
num = ''
num1 = ''
num2 = ''

def op_modify_plus():
    global op, num1, num, operation_was_made
    operation_was_made = False
    op = '+'
    if num != '':
        num1 = num
        num = ''
        test_window.set_screen_text(op)

def op_modify_minus():
    global op, num1, num, operation_was_made
    operation_was_made = False
    op = '-'
    if num != '':
        num1 = num
        num = ''
        test_window.set_screen_text(op)

def op_modify_multi():
    global op, num1, num, operation_was_made
    operation_was_made = False
    op = '*'
    if num != '':
        num1 = num
        num = ''
        test_window.set_screen_text(op)

def op_modify_div():
    global op, num1, num, operation_was_made
    operation_was_made = False
    op = '/'
    if num != '':
        num1 = num
        num = ''
        test_window.set_screen_text(op)

def num_add_1():
    global num
    num += '1'
    test_window.set_screen_text(num)

def num_add_2():
    global num
    num += '2'
    test_window.set_screen_text(num)

def num_add_3():
    global num
    num += '3'
    test_window.set_screen_text(num)

def num_add_4():
    global num
    num += '4'
    test_window.set_screen_text(num)

def num_add_5():
    global num
    num += '5'
    test_window.set_screen_text(num)

def num_add_6():
    global num
    num += '6'
    test_window.set_screen_text(num)

def num_add_7():
    global num
    num += '7'
    test_window.set_screen_text(num)

def num_add_8():
    global num
    num += '8'
    test_window.set_screen_text(num)

def num_add_9():
    global num
    num += '9'
    test_window.set_screen_text(num)

def num_add_0():
    global num
    if num != '0':
        num += '0'
        test_window.set_screen_text(num)

def calculate():
    global num1, num2, num, operation_was_made
    if not operation_was_made:
        res = ''
        num2 = num
        num = ''
        if num1 != '' and num2 != '':
            if op == '+':
                res = round(float(num1) + float(num2), 5)
            elif op == '-':
                res = round(float(num1) - float(num2), 5)
            elif op == '*':
                res = round(float(num1) * float(num2), 5)
            elif op == '/':
                if num2 != '0':
                    res = round(float(num1) / float(num2), 5)
                else:
                    res = 'Error: Division by zero.'
        elif num1 == '' and op != '':
            res = 'Error: First operand is not set.'
        elif num2 == '' and op != '':
            res = 'Error: Second operand is not set.'
        elif op == '':
            res = 'Error: Operation is not set.'
        else:
            res = 'Error: Unknown error.'  # I believe it's impossible to get it.
        res = str(res)
        test_window.set_screen_text(res)
        num1 = res
        num2 = ''
        operation_was_made = True

def clear():
    global num1, num2, num, op
    num1 = ''
    num2 = ''
    num = ''
    op = ''
    test_window.set_screen_text('')

def add_point():
    global num
    if num.find('.') == -1:
        num += '.'
        test_window.set_screen_text(num)

class Calc(QWidget):

    def __init__(self):
        super().__init__()
        self.calc_screen = QLabel('', self)
        self.initUI()


    def initUI(self):
        btn_1 = QPushButton('1', self)
        btn_2 = QPushButton('2', self)
        btn_3 = QPushButton('3', self)
        btn_4 = QPushButton('4', self)
        btn_5 = QPushButton('5', self)
        btn_6 = QPushButton('6', self)
        btn_7 = QPushButton('7', self)
        btn_8 = QPushButton('8', self)
        btn_9 = QPushButton('9', self)
        btn_0 = QPushButton('0', self)
        btn_equal = QPushButton('=', self)
        btn_plus = QPushButton('+', self)
        btn_minus = QPushButton('-', self)
        btn_multi = QPushButton('*', self)
        btn_div = QPushButton('/', self)
        btn_clear = QPushButton('C', self)
        btn_point = QPushButton('.', self)

        btn_plus.clicked.connect(op_modify_plus)
        btn_minus.clicked.connect(op_modify_minus)
        btn_multi.clicked.connect(op_modify_multi)
        btn_div.clicked.connect(op_modify_div)
        btn_equal.clicked.connect(calculate)
        btn_1.clicked.connect(num_add_1)
        btn_2.clicked.connect(num_add_2)
        btn_3.clicked.connect(num_add_3)
        btn_4.clicked.connect(num_add_4)
        btn_5.clicked.connect(num_add_5)
        btn_6.clicked.connect(num_add_6)
        btn_7.clicked.connect(num_add_7)
        btn_8.clicked.connect(num_add_8)
        btn_9.clicked.connect(num_add_9)
        btn_0.clicked.connect(num_add_0)
        btn_clear.clicked.connect(clear)
        btn_point.clicked.connect(add_point)

        btn_1.setGeometry(40, 440, 40, 40)
        btn_2.setGeometry(120, 440, 40, 40)
        btn_3.setGeometry(200, 440, 40, 40)
        btn_4.setGeometry(40, 520, 40, 40)
        btn_5.setGeometry(120, 520, 40, 40)
        btn_6.setGeometry(200, 520, 40, 40)
        btn_7.setGeometry(40, 600, 40, 40)
        btn_8.setGeometry(120, 600, 40, 40)
        btn_9.setGeometry(200, 600, 40, 40)
        btn_0.setGeometry(120, 680, 40, 40)
        btn_plus.setGeometry(400, 440, 40, 40)
        btn_minus.setGeometry(400, 520, 40, 40)
        btn_multi.setGeometry(400, 600, 40, 40)
        btn_div.setGeometry(400, 680, 40, 40)
        btn_equal.setGeometry(480, 440, 80, 280)
        btn_clear.setGeometry(200, 680, 40, 40)
        btn_point.setGeometry(40, 680, 40, 40)

        self.calc_screen.setGeometry(40, 40, 520, 50)
        self.calc_screen.setFont(QFont('Arial', 16))
        self.resize(600, 760)
        self.center()
        self.setWindowTitle('Calculator on PyQt5 ver 1.0')
        self.show()

    def center(self):
        widget_rectangle = self.frameGeometry()
        center_of_screen = QDesktopWidget().availableGeometry().center()
        widget_rectangle.moveCenter(center_of_screen)
        self.move(widget_rectangle.topLeft())

    def set_screen_text(self, text):
        self.calc_screen.setText(text)

app = QApplication(sys.argv)
test_window = Calc()
sys.exit(app.exec_())