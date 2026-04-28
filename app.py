import os 
import sys
import ui.main_window as mw
import PySide6.QtWidgets as QtWidgets

def main():
    print("Starting GUI...")
    app = QtWidgets.QApplication([])
    widget = mw.MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()