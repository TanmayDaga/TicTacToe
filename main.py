import sys

from PyQt5 import QtCore, QtGui, QtWidgets


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


class Button(QtWidgets.QPushButton):
    def __init__(self, parent, x, y):
        super().__init__(parent)
        self.setGeometry(x, y, 101, 91)
        self.setText("")

    def deletePic(self):
        self.setIcon(QtGui.QIcon(QtGui.QPixmap()))

    def setX(self):
        img = QtGui.QPixmap('images/x.jpeg')
        img.scaled(101, 91)
        self.setIcon(QtGui.QIcon(img))

    def setO(self):
        img = QtGui.QPixmap('images/o.png')
        img.scaled(101, 91)
        self.setIcon(QtGui.QIcon(img))


class GUI(object):
    def __init__(self, mainwindow: QtWidgets.QMainWindow):
        # setting main window
        self.mainwindow = mainwindow
        self.mainwindow.setFixedSize(384, 460)

        # setting central widget and stackwidget
        self.centralWidget = QtWidgets.QWidget(self.mainwindow)
        self.stackWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackWidget.setGeometry(QtCore.QRect(0, 0, 384, 460))

        # setting standard font
        self.standardFont = QtGui.QFont()
        self.standardFont.setBold(True)
        self.standardFont.setFamily('Comic Sans Ms')
        self.standardFont.setWeight(75)
        self.standardFont.setPointSize(22)

        # setting home page
        self.homeScreen = QtWidgets.QWidget()
        self.playWithComputer = QtWidgets.QPushButton(self.homeScreen)
        self.playWithComputer.setGeometry(QtCore.QRect(100, 90, 171, 101))
        self.playWithComputer.setFont(self.standardFont)
        self.playWithComputer.setText('Play with\n computer')
        self.playWithComputer.clicked.connect(self.onClickPlayWithComputer)
        self.playWithPerson = QtWidgets.QPushButton(self.homeScreen)
        self.playWithPerson.setGeometry(100, 230, 171, 101)
        self.playWithPerson.setFont(self.standardFont)
        self.playWithPerson.setText('Play with\n person')
        self.stackWidget.addWidget(self.homeScreen)

        # setting play screen
        self.playScreen = QtWidgets.QWidget()
        # setting lines
        self.lineVertical1 = VLine(self.playScreen, 128, 80)
        self.lineVertical2 = VLine(self.playScreen, 256, 80)
        self.lineHorizontal1 = HLine(self.playScreen, 30, 190)
        self.lineHorizontal2 = HLine(self.playScreen, 30, 320)
        # setting buttons
        self.button1 = Button(self.playScreen, 30, 90)
        self.button2 = Button(self.playScreen, 150, 90)
        self.button3 = Button(self.playScreen, 270, 90)
        self.button4 = Button(self.playScreen, 30, 210)
        self.button5 = Button(self.playScreen, 150, 210)
        self.button6 = Button(self.playScreen, 270, 210)
        self.button7 = Button(self.playScreen, 30, 340)
        self.button8 = Button(self.playScreen, 150, 340)
        self.button9 = Button(self.playScreen, 270, 340)
        # setting exit button
        self.exitButtonPlayScreen = QtWidgets.QPushButton('Exit', self.playScreen)
        self.exitButtonPlayScreen.setGeometry(QtCore.QRect(10, 10, 111, 41))
        self.exitButtonPlayScreen.setFont(self.standardFont)
        self.stackWidget.addWidget(self.playScreen)

        self.mainwindow.setCentralWidget(self.centralWidget)
        self.stackWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.mainwindow)

        # TODO

    def onClickPlayWithComputer(self):
        self.refreshScreen()
        self.stackWidget.setCurrentIndex(1)

        # TODO

    def onClickPlayWithPerson(self):
        self.refreshScreen()
        self.stackWidget.setCurrentIndex()

    def onClickExitButton(self):
        pass

    def refreshScreen(self):
        self.button1.deletePic()
        self.button2.deletePic()
        self.button3.deletePic()
        self.button4.deletePic()
        self.button5.deletePic()
        self.button6.deletePic()
        self.button7.deletePic()
        self.button8.deletePic()
        self.button9.deletePic()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    v = QtWidgets.QMainWindow()
    ex = GUI(v)
    v.show()
    sys.exit(app.exec_())
