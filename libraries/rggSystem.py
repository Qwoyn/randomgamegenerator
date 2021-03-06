'''
initialization - for the Random Game Generator project
By Doctus (kirikayuumura.noir@gmail.com)

Qt and C++ services.

    This file is part of RandomGameGenerator.

    RandomGameGenerator is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    RandomGameGenerator is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with RandomGameGenerator.  If not, see <http://www.gnu.org/licenses/>.
'''
from sys import maxsize
from os import walk, stat, path, remove
from random import choice as rchoice
from random import random
from math import hypot, cos, sin, pi

from libraries.rggQt import QAction, QCoreApplication, QMessageBox, QMenu, QPoint, QInputDialog, QFileDialog
from libraries.rggConstants import UNICODE_STRING

class wAction(QAction):

	def __init__(self, text, parent, id):
		QAction.__init__(self, text, parent)
		self.id = id

class fake(object):
	"""Fake translation tools."""

	@staticmethod
	def translate(context, key, *args):
		"""Fake translate to mark strings before they are used."""
		if args:
			raise RuntimeError("Fake translation of {context} failed. "
				"Comment arguments will not be preserved.".format(context=context))
		assert(not args)
		return key

# Real translation
def translate(*args):
	return UNICODE_STRING(QCoreApplication.translate(*args))

mainWindow = None

def signal(*args, **kwargs):
	"""Creates a signal."""

	# Figure out parameters
	parameters = args
	for parm in parameters:
		if not isinstance(parm, type):
			raise TypeError("Parameters to the signal constructor must be types.")
	doc = kwargs.get('doc')

	# A unique key
	key = object()

	def get(self):
		if not hasattr(self, '_signals'):
			self._signals = {}
		if key not in self._signals:
			self._signals[key] = signalStorage(parameters)
		return self._signals[key]

	return property(get, doc=doc)

class signalStorage(object):
	"""A signal mechanism similar to Qt's signals.

	Would have used Qt's if they supported python better.

	"""

	def __init__(self, parameters):
		"""Initializes the signal.

		args -- the parameters used to trigger the signal

		"""
		self.callbacks = set()
		self.parameters = parameters

	def emit(self, *args):
		"""Emit this signal to all connected slots."""
		if len(args) != len(self.parameters):
			raise TypeError("Too few parameters to signal.")
		for parm, arg in zip(self.parameters, args):
			if not isinstance(arg, parm):
				raise TypeError("Invalid parameter to signal: expected {0} to be {1}.".format(repr(arg), parm))
		for callback in self.callbacks:
			try:
				callback(*args)
			except Exception as e:
				import traceback
				print("ERROR encountered in signal handler {handler}:".format(handler=repr(callback)))
				traceback.print_exc()

	def connect(self, callable):
		"""Connect this signal to a slot. (Python callable.)"""
		self.callbacks.add(callable)

	def disconnect(self, callable=None):
		"""Disconnect this signal from a specified slot,
		or all slots if no parameter is specified.

		"""
		if callable is None:
			self.callbacks = set()
		else:
			self.callbacks.remove(callable)

def injectMain():
	"""Injects and returns the main C++ interface object."""
	global mainWindow

	assert(not mainWindow)

	try:
		from libraries.rggMain import MainWindow
	except ImportError as e:
		from rggMain import MainWindow
	mainWindow = MainWindow()
	return mainWindow

def showErrorMessage(message, title=translate('system', "Error", 'default error prompt title')):
	"""Pops up an error message to the user."""
	QMessageBox.critical(mainWindow, title, message)

def showPopupMenuAt(position, choices):
	popup = QMenu(mainWindow)
	idCounter = 0

	for choice in choices:
		popup.addAction(wAction(choice, mainWindow, idCounter))
		idCounter += 1

	realx = position[0] + (mainWindow.x() + mainWindow.glwidget.x())
	realy = position[1] + (mainWindow.y() + mainWindow.glwidget.y())
	selectedAction = popup.exec_(QPoint(realx, realy))

	if not selectedAction:
		return -1

	return selectedAction.id

def showPopupMenuAtAbs(position, choices):
	popup = QMenu(mainWindow)
	idCounter = 0

	for choice in choices:
		popup.addAction(wAction(choice, mainWindow, idCounter))
		idCounter += 1

	realx = position[0]
	realy = position[1]
	selectedAction = popup.exec_(QPoint(realx, realy))

	if not selectedAction:
		return -1

	return selectedAction.id

def promptString(prompt, title=translate('system', "Input", 'default string prompt title'), inittext=None):
	if inittext is not None:
		text, ok = QInputDialog.getText(mainWindow, title, prompt, text=inittext)
	else:
		text, ok = QInputDialog.getText(mainWindow, title, prompt)
	if not ok:
		return None
	return UNICODE_STRING(text)

def promptInteger(prompt, title=translate('system', "Input", 'default integer prompt title'),
		min=-maxsize, max=maxsize, default=0, step=1):
	value, ok = QInputDialog.getInt(mainWindow, title, prompt, default, min, max, step)
	if not ok:
		return None
	return int(value)

def promptCoordinates(prompt1, prompt2, title=translate('system', "Input", 'default coordinate prompt title'),
		min=-maxsize, max=maxsize, step=1):
	value1 = promptInteger(prompt1, title, min, max, step)
	if value1 is None:
		return None
	value2 = promptInteger(prompt2, title, min, max, step)
	if value2 is None:
		return None
	return (value1, value2)

def promptLoadFile(title, filter, dir=''):
	filename = QFileDialog.getOpenFileName(mainWindow,
		title,
		dir,
		filter)
	if not filename:
		return None
	return UNICODE_STRING(filename[0])

def promptSaveFile(title, filter, dir=''):
	filename = QFileDialog.getSaveFileName(mainWindow,
		title,
		dir,
		filter)
	if not filename:
		return None
	return UNICODE_STRING(filename[0])

def promptButtonSelection(prompt, text=[], defaultButton = 0):
	convertedText = ()
	if text is not tuple: #lists/dictionaries make this function a sad panda :(
		convertedText = (text)
	else:
		convertedText = text

	if(len(convertedText) == 0):
		return -1

	buttons = []

	questionDialog = QMessageBox(mainWindow);
	questionDialog.setText(prompt);

	j = len(convertedText) - 1
	while(j >= 0):
		newButton = questionDialog.addButton(convertedText[j], QMessageBox.AcceptRole);
		buttons.insert(0, newButton);
		if(j == defaultButton):
			questionDialog.setDefaultButton(newButton)
		j -= 1

	questionDialog.exec_()

	i = 0
	for button in buttons:
		if(questionDialog.clickedButton() == button):
			return i
		i += 1

	return -1

def promptYesNo(prompt):
	questionDialog = QMessageBox(mainWindow)
	questionDialog.setText(prompt)
	questionDialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
	return questionDialog.exec_()

def findFiles(dir, extensions):
	"""Get the list of files with one of the given extensions."""
	files = []
	for dirpath, dirnames, filenames in walk(dir):
		if ".svn" in dirpath:
			continue
		#filenames.sort()
		for filename in filenames:
			if path.splitext(filename)[1] in extensions:
				name = path.join(dirpath, filename)[len(dir) + 1:]
				#print "found file:", name, makePortableFilename(name)
				if stat(path.join(dirpath, filename))[6] == 0: continue
				files.append(makePortableFilename(name))
	#files.sort()
	return files

def checkFileExtension(filename, extension):
	if extension not in filename:
		return filename + extension
	return filename

def cameraPosition():
	return mainWindow.glwidget.camera

def cameraSize():
	return (mainWindow.glwidget.w, mainWindow.glwidget.h)

def setCameraPosition(position):
	mainWindow.glwidget.camera = list(position)

def findRandomAppend():
	"""Gives a random character to append to string to make it """
	# Can't spell swear words without vowels
	# Left out l and v because they look enough like i and u
	letters = '256789bcdfghjkmnpqrstwxz'
	return rchoice(letters)


def makeLocalFilename(filename):
	"""Converts a portable path to a complete path."""
	# TODO: Implement filename conversion
	return filename

def makePortableFilename(filename):
	"""Attempts to convert a local path to a portable, relative, unique path."""
	# TODO: Implement filename conversion
	return filename.replace('\\', '/')

def drawSelectionCircle(x, y, splasifarcity, radius):
	mainWindow.glwidget.addSelectionCircle(splasifarcity, x, y, radius)

def clearSelectionCircles():
	mainWindow.glwidget.clearSelectionCircles()

def drawRectangle(x, y, w, h, r, g, b):
	mainWindow.glwidget.addRectangle(x, y, w, h, r, g, b)

def clearRectangles():
	mainWindow.glwidget.clearRectangles()

def drawLine(x, y, w, h, thickness, r, g, b):
	mainWindow.glwidget.addLine(thickness, x, y, w, h, r, g, b)

def deleteLine(x, y, w, h, thickness = -1):
	mainWindow.glwidget.deleteLine(thickness, x, y, w, h)

def drawPreviewLine(x, y, w, h, thickness, r, g, b):
	mainWindow.glwidget.addPreviewLine(thickness, x, y, w, h, r, g, b)

def clearLines():
	mainWindow.glwidget.clearLines()

def clearPreviewLines():
	mainWindow.glwidget.clearPreviewLines()

def getLinesOfThickness(thickness):
	lines = dict()
	try:
		lines = mainWindow.glwidget.lines[thickness]
	except:
		pass
	return lines

def drawSegmentedLine(x, y, w, h, thickness, r, g, b, preview=False):
	'''Draws a straight line, but split into small lines (length < 10), which are returned as a set.'''
	if abs(x-w)+abs(y-h) < 10:
		if preview:
			drawPreviewLine(x, y, w, h, thickness, r, g, b)
		else:
			drawLine(x, y, w, h, thickness, r, g, b)
		newline = set()
		newline.add((x, y, w, h, thickness, r, g, b))
		return newline
	else:
		first = drawSegmentedLine(x, y, (x+w)/2.0, (y+h)/2.0, thickness, r, g, b, preview)
		second = drawSegmentedLine((x+w)/2.0, (y+h)/2.0, w, h, thickness, r, g, b, preview)
		return first | second

def drawRectangleMadeOfLines(x, y, w, h, colour, thickness, preview=False):
	'''Draws lines in a rectangular shape.'''
	return drawSegmentedLine(x, y, w, y, thickness, colour[0], colour[1], colour[2], preview) | drawSegmentedLine(w, y, w, h, thickness, colour[0], colour[1], colour[2], preview) | drawSegmentedLine(w, h, x, h, thickness, colour[0], colour[1], colour[2], preview) | drawSegmentedLine(x, h, x, y, thickness, colour[0], colour[1], colour[2], preview)

def drawCircle(centre, edge, colour, thickness, preview=False):
	'''Draws lines to form an approximate circle.'''
	lines = set()
	radius = hypot(edge[0]-centre[0], edge[1]-centre[1])
	vert = [centre[0]+radius, centre[1], 0, 0]
	for r in range(3, 363, 3):
		vert[2] = centre[0]+cos(r*0.01745329)*radius
		vert[3] = centre[1]+sin(r*0.01745329)*radius
		lines.update(drawSegmentedLine(vert[0], vert[1], vert[2], vert[3], thickness, colour[0], colour[1], colour[2], preview))
		vert[0] = vert[2]
		vert[1] = vert[3]
	return lines

def drawRegularPolygon(sides, centre, size, colour, thickness, rainbow = False, preview = False):
	#TODO: Add rotation parameter.
	vertices = []
	lines = set()
	for i in range(sides):
		vertices.append((centre[0]+size*cos(2*pi*i/sides), centre[1]+size*sin(2*pi*i/sides)))
	for p in range(sides):
		for q in range(sides):
			if sides%2 == 1 or p%(sides/2) != q%(sides/2):
				if not rainbow:
					lines.update(drawSegmentedLine(vertices[p][0], vertices[p][1], vertices[q][0], vertices[q][1], thickness, colour[0], colour[1], colour[2], preview))
				else:
					lines.update(drawSegmentedLine(vertices[p][0], vertices[p][1], vertices[q][0], vertices[q][1], thickness, random(), random(), random(), preview))
	return lines

def addText(text, pos):
	return mainWindow.glwidget.addText(text, pos)

def removeText(ID):
	mainWindow.glwidget.removeText(ID)

def setZoom(zoom):
	#_main.setZoom(zoom)
	print("unimplemented2")
	return False

def getZoom():
	return mainWindow.glwidget.zoom

def getMapPosition(screenCoordinates):
	mapPosition = list(map(lambda p,c,d: p/d - c/d, screenCoordinates, cameraPosition(), (getZoom(), getZoom())))
	return mapPosition

def purgeEmptyFiles(rootpath):
	'''Recursively deletes all empty files in rootpath and its subdirectories. Never deletes directories.'''
	rootpath = UNICODE_STRING(rootpath)
	for (dirpath, dirnames, filenames) in walk(rootpath):
		for filename in filenames:
			fullpath = path.join(dirpath, filename)
			try:
				if stat(fullpath).st_size == 0:
					remove(fullpath)
			except WindowsError:
				print("Warning: pog locale error.")
