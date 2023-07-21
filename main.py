from PIL import ImageGrab
from PyQt6 import QtWidgets
from PyQt6 import QtCore
from datetime import datetime

from PyQt6.QtWidgets import QPushButton

from gui import Ui_MainWindow
from classes import PlayerStatsUi
from StatisticsChecker import StatisticsChecker
import keyboard


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.config = "configs/1920.1080.125.txt"

        self.setupUi(self)
        self.al_team = self.generate_allies()
        self.en_team = self.generate_enemies()

        self.al_frame.setStyleSheet(
            "#al_frame {background-color: rgba(74, 82, 113, 150); border: 1px solid darknavy; border-radius: 10px;}")
        self.en_frame.setStyleSheet(
            "#en_frame {background-color: rgba(74, 82, 113, 150); border: 1px solid darknavy; border-radius: 10px;}")
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.hook = keyboard.on_press(self.on_key_press)

        self.button = QPushButton(self)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.acivate_olenemer)
        self.button.hide()

    def on_key_press(self, event):
        if event.event_type == 'down':
            if event.scan_code == 87:
                self.button.click()
            if event.scan_code == 68:
                if self.isHidden():
                    self.show()
                else:
                    self.hide()

    def acivate_olenemer(self):
        image = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
        filename = datetime.now().strftime("image_%Y-%m-%d_%H-%M-%S.png")
        image.save(f'screenshots/{filename}')
        statistics = StatisticsChecker.get_players_statistics(self.config, f'screenshots/{filename}')
        for i in range(7):
            self.al_team[i].set_stats(statistics['allies'][i])
            self.en_team[i].set_stats(statistics['enemies'][i])

    def generate_allies(self):
        allies_team = []
        self.al_frame.setLayout(self.al_panel)
        for i in range(7):
            player_ui = PlayerStatsUi(self.layoutWidget, self.al_panel)
            allies_team.append(player_ui)
        return allies_team

    def generate_enemies(self):
        enemies_team = []
        self.en_frame.setLayout(self.en_panel)
        for i in range(7):
            player_ui = PlayerStatsUi(self.layoutWidget, self.en_panel)
            enemies_team.append(player_ui)
        return enemies_team


def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.showFullScreen()
    app.exec()


if __name__ == '__main__':
    main()
