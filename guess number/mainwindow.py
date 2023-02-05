"""Module for main window."""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from ui_mainwindow import Ui_MainWindow
from game_window import GameWindow


class MainWindow(QMainWindow):
    """Class of main window."""

    def __init__(self):
        """Init."""
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Number Guessing Game")

        self.info_level = {'light': [20, 10], 'middle': [500, 15], 'hard': [1000, 30]}
        self.set_enabled(False)

        self.chosen_level = self.info_level['light']
        self.ui.lightLevel.setChecked(True)
        self.set_value(self.chosen_level)

        self.ui.beginButtom.clicked.connect(self.run_game)
        self.ui.actionExit.triggered.connect(self.closeEvent)

        self.ui.lightLevel.stateChanged.connect(self.uncheck)
        self.ui.middleLevel.stateChanged.connect(self.uncheck)
        self.ui.hardLevel.stateChanged.connect(self.uncheck)
        self.ui.userLevel.stateChanged.connect(self.uncheck)

    def close_window(self):
        """Method for closing window."""
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            self.close()
        else:
            pass

    def closeEvent(self, event):
        """CloseEvent."""
        self.close_window()

    def run_game(self):
        """Start game."""
        if self.ui.userLevel.isChecked():
            self.chosen_level = self.get_info()

        self.window_game = GameWindow(self.chosen_level)
        self.window_game.backSignal.connect(self.show)
        self.hide()
        self.window_game.show()

    def get_info(self):
        """Get numbers from QLineEdit for users level."""
        max_number = int(self.ui.maxNumber.text())
        max_attempts = int(self.ui.maxAttempts.text())
        return [max_number, max_attempts]

    def set_enabled(self, flag):
        """Set enabled for QLineEdit."""
        self.ui.maxNumber.setEnabled(flag)
        self.ui.maxAttempts.setEnabled(flag)

    def set_value(self, data):
        """Fill QLineEdit with numbers."""
        self.set_enabled(False)
        self.ui.maxNumber.setText(str(data[0]))
        self.ui.maxAttempts.setText(str(data[1]))

    def uncheck(self, state):
        """Set check for QCheckBoxes."""
        if state == Qt.Checked:
            if self.sender() == self.ui.lightLevel:
                self.chosen_level = self.info_level['light']
                self.set_value(self.chosen_level)
                self.ui.middleLevel.setChecked(False)
                self.ui.hardLevel.setChecked(False)
                self.ui.userLevel.setChecked(False)

            elif self.sender() == self.ui.middleLevel:
                self.chosen_level = self.info_level['middle']
                self.set_value(self.chosen_level)
                self.ui.lightLevel.setChecked(False)
                self.ui.hardLevel.setChecked(False)
                self.ui.userLevel.setChecked(False)

            elif self.sender() == self.ui.hardLevel:
                self.chosen_level = self.info_level['hard']
                self.set_value(self.chosen_level)
                self.ui.lightLevel.setChecked(False)
                self.ui.middleLevel.setChecked(False)
                self.ui.userLevel.setChecked(False)

            elif self.sender() == self.ui.userLevel:
                self.set_enabled(True)
                self.ui.lightLevel.setChecked(False)
                self.ui.middleLevel.setChecked(False)
                self.ui.hardLevel.setChecked(False)


