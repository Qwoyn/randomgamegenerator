from libraries.rggState import GlobalState
from libraries.rggDockWidget.diceRoller import diceRoller
from libraries.rggDockWidget.pogPalette import pogPalette
from libraries.rggDockWidget.chatWidget import chatWidget
from libraries.rggDockWidget.ICChatWidget import ICChatWidget
from libraries.rggDockWidget.userListWidget import userListWidget
from libraries.rggDockWidget.mapEditor import mapEditor
from libraries.rggDockWidget.transferMonitorWidget import transferMonitorWidget
from libraries.rggDockWidget.deckWidget import deckWidget

def initialize(mainWindow):
	GlobalState.dwidget = diceRoller(mainWindow)
	GlobalState.pwidget = pogPalette(mainWindow)
	GlobalState.cwidget = chatWidget(mainWindow)
	GlobalState.icwidget = ICChatWidget(mainWindow)
	GlobalState.uwidget = userListWidget(mainWindow)
	GlobalState.mwidget = mapEditor(mainWindow)
	GlobalState.fwidget = transferMonitorWidget(mainWindow)
	GlobalState.deckwidget = deckWidget(mainWindow)
