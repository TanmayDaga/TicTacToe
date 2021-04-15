import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from logic import TicTacToeBoard


class VLine(QtWidgets.QFrame):
    def __init__(self, parent, x, y):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(x, y, 16, 351))
        self.setLineWidth(4)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setFrameShape(QtWidgets.QFrame.VLine)


class HLine(QtWidgets.QFrame):
    def __init__(self, parent, x, y):
        super().__init__(parent)
        self.setGeometry(x, y, 321, 16)
        self.setLineWidth(4)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setFrameShape(QtWidgets.QFrame.HLine)


class PushButton(QtWidgets.QPushButton):
    def __init__(self, parent, x, y, bx, by):
        super().__init__(parent)
        self.setGeometry(x, y, 101, 91)
        self.bx = bx
        self.by = by
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(89)

    def reset(self):
        self.setText("")

    def setX(self):
        self.setText("X")

    def setO(self):
        self.setText("O")

    def occupied(self):
        if self.text():
            return True
        return False


class TicTacToeGui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(384, 460)
        # setting player variable
        # for person to person
        self.p1 = None
        self.p2 = None
        # for computer to person
        self.comp = None
        self.player = None
        # setting counter
        self.counter = 0

        # creating central widget
        self.central_widget = QtWidgets.QWidget(self)

        # creating up stacked widget
        self.stack_widget = QtWidgets.QStackedWidget(self.central_widget)

        # creating button font
        self.button_font = QtGui.QFont()

        # creating home screen
        self.home_screen = QtWidgets.QWidget()
        # creating play with computer button on home screen
        self.play_with_computer = QtWidgets.QPushButton(self.home_screen)
        # creating play with person button on home screen
        self.play_with_person = QtWidgets.QPushButton(self.home_screen)

        # creating play screen
        self.play_screen = QtWidgets.QWidget()
        # creating buttons on playscreen
        self.button_list = []
        # creating lines on playScreen
        self.v_line1 = VLine(self.play_screen, 128, 80)
        self.v_line2 = VLine(self.play_screen, 256, 80)
        self.h_line3 = HLine(self.play_screen, 30, 190)
        self.h_line4 = HLine(self.play_screen, 30, 320)
        # creating exit button on play screen
        self.exit_button = QtWidgets.QPushButton(self.play_screen)

        self.setupUi()

    def setupUi(self):
        # setting central widget
        self.setCentralWidget(self.central_widget)

        # setting stacked widget geometry
        self.stack_widget.setGeometry(QtCore.QRect(0, 0, 384, 460))

        # setting button font
        self.button_font.setBold(True)
        self.button_font.setFamily('Comic Sans Ms')
        self.button_font.setWeight(75)
        self.button_font.setPointSize(22)

        # setting home screen
        self.stack_widget.addWidget(self.home_screen)
        # play with computer button
        self.play_with_computer.setGeometry(QtCore.QRect(100, 90, 171, 101))
        self.play_with_computer.setFont(self.button_font)
        self.play_with_computer.setText('Play with\n computer')
        self.play_with_computer.clicked.connect(partial(self.on_click_play_with_computer, ))
        # play with person button
        self.play_with_person.setGeometry(QtCore.QRect(100, 230, 171, 101))
        self.play_with_person.setFont(self.button_font)
        self.play_with_person.setText('Play with\n person')
        self.play_with_person.clicked.connect(self.on_click_play_with_person)

        # setting play_screen
        self.stack_widget.addWidget(self.play_screen)
        # setting buttons on play_screen
        for x in enumerate([30, 150, 270]):
            for y in enumerate([90, 215, 340]):
                self.but = PushButton(self.play_screen, x[1], y[1], x[0], y[0])
                self.button_list.append(self.but)
                self.but.clicked.connect(partial(self.on_click_button, self.but))

        # setting exit button on play_screen
        self.exit_button.setText('Exit')
        self.exit_button.setGeometry(QtCore.QRect(10, 10, 111, 41))
        self.exit_button.setFont(self.button_font)
        self.exit_button.clicked.connect(self.on_click_exit_button)

    def on_click_exit_button(self):
        self.stack_widget.setCurrentIndex(0)
        self.reset_screen()

    def on_click_play_with_computer(self):

        self.p1 = None
        self.p2 = None
        self.comp = 0
        self.player = 0
        self.reset_screen()
        self.stack_widget.setCurrentIndex(1)

    def on_click_play_with_person(self):
        self.comp = None
        self.player = None
        self.p1 = '0'
        self.p2 = '0'
        self.reset_screen()
        self.stack_widget.setCurrentIndex(1)

    def on_click_button(self, *args):

        button = args[0]

        if self.counter > 9:
            exit()
        if not button.occupied():
            # if game is person to person
            if self.p1:
                if int(self.p1) > int(self.p2):
                    self.p2 = str(int(self.p2) + 1)
                    button.setX()
                    self.counter += 1
                    self.board.change_sign(button.bx, button.by, '2')
                    if self.check_win():
                        return
                    if self.counter == 9:
                        self.draw()
                else:
                    self.p1 = str(int(self.p1) + 1)
                    button.setO()
                    self.counter += 1
                    self.board.change_sign(button.bx, button.by, '1')
                    if self.check_win():
                        return
                    if self.counter == 9:
                        self.draw()

            # Game is computer to person
            else:
                button.setO()
                self.counter += 1
                self.board.change_sign(button.bx, button.by, '1')

                if self.check_win():
                    return
                elif self.counter <= 8:

                    self.computer_play()


                if self.check_win():
                    return
                # if game draw
                if self.counter == 9:
                    self.draw()

    def draw(self):
        box = QtWidgets.QMessageBox()
        box.setIcon(QtWidgets.QMessageBox.Information)
        box.setWindowTitle('Draw')
        box.setInformativeText("Game is draw")
        box.exec_()
        self.stack_widget.setCurrentIndex(0)

    def computer_play(self):
        row, column = self.board.random_play()

        for items in self.button_list:
            if items.bx == row:
                if items.by == column:
                    items.setX()

                    self.counter += 1
                    break

    def reset_screen(self):
        # first time it would give error
        try:
            del self.board
        except AttributeError as e:
            pass
        self.counter = 0
        self.board = TicTacToeBoard()
        for items in self.button_list:
            items.reset()

    def check_win(self):
        for i in ['1', '2']:
            if self.board.row_win(i):
                box = QtWidgets.QMessageBox()
                box.setIcon(QtWidgets.QMessageBox.Information)
                box.setWindowTitle('Won')
                box.setInformativeText('O won' if i == '1' else 'X won')
                box.exec_()
                self.stack_widget.setCurrentIndex(0)
                return True
            if self.board.column_win(i):
                box = QtWidgets.QMessageBox()
                box.setIcon(QtWidgets.QMessageBox.Information)
                box.setWindowTitle('Won')
                box.setInformativeText('O won' if i == '1' else 'X won')
                box.exec_()
                self.stack_widget.setCurrentIndex(0)
                return True
            if self.board.diagonal_win(i):
                box = QtWidgets.QMessageBox()
                box.setIcon(QtWidgets.QMessageBox.Information)
                box.setWindowTitle('Won')
                box.setInformativeText('O won' if i == '1' else 'X won')
                box.exec_()
                self.stack_widget.setCurrentIndex(0)
                return True
        return False


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = TicTacToeGui()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
