import keyboard
from PyQt6 import QtWidgets

class KeyGrabber(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.hook = keyboard.on_press(self.keyboardEventReceived)
    def keyboardEventReceived(self, event):
        if event.event_type == 'down':
            if event.scan_code == 68:
                if self.isVisible():
                    self.hide()
                else:
                    self.setVisible(True)