import PySide6.QtWidgets as QtWidgets
import PySide6.QtCore as QtCore
import os
from core import runner as runner
from PySide6.QtWidgets import QFileDialog

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        #Label de directorio actual
        self.directoryLabel = QtWidgets.QLabel("Current Directory: ")

        #Campo de texto para URL
        self.urlField = QtWidgets.QLineEdit()
        
        #Botón de selección de directorio
        self.directorySearchButton = QtWidgets.QPushButton("Destination Directory")
        self.directorySearchButton.clicked.connect(self.selectDirectory)
        
        #Botón de búsqueda de URL
        self.urlSearchButton = QtWidgets.QPushButton("Search")
        self.urlSearchButton.clicked.connect(runner.run)
        self.urlSearchButton.setEnabled(False)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.directoryLabel)
        self.layout.addWidget(self.urlField)
        self.layout.addWidget(self.directorySearchButton)
        self.layout.addWidget(self.urlSearchButton)
        self.setLayout(self.layout)

    def selectDirectory(self):
        runner.destinationDirectory = QFileDialog.getExistingDirectory(
            parent=None,
            caption="Select Destination Directory",
            options=QFileDialog.ShowDirsOnly
        )
        if runner.checkWritableDirectory(runner.destinationDirectory) and runner.checkValidURL(self.urlField.text()):
            self.urlSearchButton.setEnabled(True)
            self.directoryLabel.setText(runner.destinationDirectory)
            runner.url = self.urlField.text()
        else:
            self.urlSearchButton.setEnabled(False)
        