from PySide6.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys

app = QApplication(sys.argv) #argv allows for cmd args

# Create our window
window = QWidget() # TODO: Create the main widget and swap to it
window.show()

# Start the event loop.
app.exec()
