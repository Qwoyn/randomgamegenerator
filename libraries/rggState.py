class GlobalState(object):
	"""A state class build to avoid all these global statements."""

	session = None#Session()

	alert = True

	pogSelection = set()
	pogSelectionCandidate = set()
	pogHover = None
	
	rightclickmode = True
	gridMode = False

	mouseButton = None
	mousePosition = (0, 0)

	pogPlacement = False
	pogPath = "path"

	previousLinePlacement = None #(0, 0) expected
	nextLinePlacement = None

	thickness = 1
	linecolour = [1.0, 1.0, 1.0]
	drawmode = "Freehand"

	GM = None

	storedMessages = []

	moveMode = "free"
	moveablePogs = []

	cameraPog = None
	pogmove = [0, 0]

	dreams = {}

	@staticmethod
	def incrementDreams(target, amount):
		if target not in GlobalState.dreams:
			GlobalState.dreams[target] = 0
		GlobalState.dreams[target] += amount

	@staticmethod
	def getDreams(target):
		if target not in GlobalState.dreams:
			return 0
		return GlobalState.dreams[target]

	@staticmethod
	def initialize(mainApp):
		GlobalState.App = mainApp
