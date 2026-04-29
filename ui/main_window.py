import PySide6.QtWidgets as QtWidgets
import PySide6.QtCore as QtCore
import os
from core import runner as runner
from PySide6.QtWidgets import QFileDialog

class MyWidget(QtWidgets.QWidget):

    writableDirectory = False
    validURL = False

    def __init__(self):
        super().__init__()

        #Label de directorio actual
        self.directoryLabel = QtWidgets.QLabel("Current Directory: ")

        #Campo de texto para URL
        self.urlField = QtWidgets.QLineEdit()
        self.urlField.textChanged.connect(self.checkURL)
        
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
        if runner.checkWritableDirectory(runner.destinationDirectory):
            self.writableDirectory = True
        else:
            self.writableDirectory = False
        self.directoryLabel.setText(runner.destinationDirectory)
        self.enableSearchButton()

    def checkURL(self):
        runner.url = self.urlField.text()
        if runner.checkValidURL(runner.url):
            self.validURL = True
        else:
            self.validURL = False
        self.enableSearchButton()

    def enableSearchButton(self):
        if self.writableDirectory and self.validURL:
            self.urlSearchButton.setEnabled(True)
        else:
            self.urlSearchButton.setEnabled(False)
        