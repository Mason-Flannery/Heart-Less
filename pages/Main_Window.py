from UIs.compiled.main_window  import Ui_MainWindow
from PySide6.QtWidgets import QWidget, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # TODO: Connect actions? Implement the file reader
        
