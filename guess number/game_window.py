"""Module with game."""

from typing import List

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import random


class GameWindow(QWidget):
    """Class of window of game."""
    backSignal = QtCore.pyqtSignal()

    def __init__(self, list_info: List):
        """Init."""
        super().__init__()
        self.setWindowTitle("Number Guessing Game")
        self.setWindowIcon(QtGui.QIcon('numbers.png'))
        self.UiComponents()
        self.number = 0
        self.max_number = list_info[0]
        self.max_attempts = list_info[1]
        self.attempts = self.max_attempts

    def UiComponents(self):
        """Init window."""
        head = QLabel("Number Guessing Game", self)
        head.setGeometry(20, 10, 300, 60)

        font = QFont('Times', 14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)

        head.setFont(font)
        head.setAlignment(Qt.AlignCenter)
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.darkCyan)
        head.setGraphicsEffect(color)

        self.info = QLabel("Welcome", self)
        self.info.setGeometry(40, 85, 260, 60)
        self.info.setWordWrap(True)
        self.info.setFont(QFont('Times', 13))
        self.info.setAlignment(Qt.AlignCenter)
        self.info.setStyleSheet("QLabel"
                                "{"
                                "border : 2px solid black;"
                                "background : lightgrey;"
                                "}")

        self.spin = QSpinBox(self)
        self.spin.setRange(1, 20)
        self.spin.setGeometry(120, 170, 100, 60)
        self.spin.setAlignment(Qt.AlignCenter)
        self.spin.setFont(QFont('Times', 15))

        self.check = QPushButton("Check", self)
        self.check.setGeometry(130, 235, 80, 30)
        self.check.clicked.connect(self.check_action)

        start = QPushButton("Start", self)
        start.setGeometry(65, 280, 100, 40)

        reset_game = QPushButton("Reset", self)
        reset_game.setGeometry(175, 280, 100, 40)
        color_red = QGraphicsColorizeEffect()
        color_red.setColor(Qt.red)
        reset_game.setGraphicsEffect(color_red)

        color_green = QGraphicsColorizeEffect()
        color_green.setColor(Qt.darkBlue)
        start.setGraphicsEffect(color_green)

        start.clicked.connect(self.start_action)
        reset_game.clicked.connect(self.reset_action)

    def start_action(self):
        """Start bottom."""
        self.check.setEnabled(True)
        self.attempts = self.max_attempts
        self.info.setStyleSheet("QLabel"
                                "{"
                                "border : 2px solid black;"
                                "background : lightgrey;"
                                "}")

        self.number = random.randint(1, self.max_number)
        self.info.setText("Try to guess number between 1 to {0}".format(self.max_number))

    def check_action(self):
        """Check bottom."""
        user_number = self.spin.value()

        if user_number == self.number and self.attempts > 1:
            self.info.setText("Correct Guess")
            self.info.setStyleSheet("QLabel"
                                    "{"
                                    "border : 2px solid black;"
                                    "background : lightgreen;"
                                    "}")

        elif user_number < self.number and self.attempts > 1:
            self.attempts = self.attempts - 1
            self.info.setText("Your number is smaller.\nRemaining attempts {0}".format(self.attempts))

        elif user_number > self.number and self.attempts > 1:
            self.attempts = self.attempts - 1
            self.info.setText("Your number is bigger.\nRemaining attempts {0}".format(self.attempts))

        else:
            self.info.setText("Attempts ended")
            self.check.setEnabled(False)

    def reset_action(self):
        """Reset bottom."""
        self.check.setEnabled(True)
        self.attempts = self.max_attempts
        self.info.setStyleSheet("QLabel"
                                "{"
                                "border : 2px solid black;"
                                "background : lightgrey;"
                                "}")
        self.info.setText("Welcome")

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        """CloseEvent."""
        self.backSignal.emit()
        self.close()
