import sys
from PyQt4 import QtCore, QtGui

import cGame


app = QtGui.QApplication(sys.argv)

window = QtGui.QMainWindow()
window.setMinimumSize(640, 480)

mGame = cGame.cGame(window)

window.show()

app.exec_()