from PySide6.QtWidgets import QApplication, QMainWindow
from UIs.compiled.main_window import  Ui_MainWindow
from pages.Main_Window import MainWindow
# Only needed for access to command line arguments
import sys

app = QApplication(sys.argv) #argv allows for cmd args

# Create our window
window = MainWindow()
window.show()

# Start the event loop.
app.exec()
