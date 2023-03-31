from PyQt6 import QtWidgets
from PyQt6 import QtCore
from gui import Ui_MainWindow
from classes import player_stats_ui
from statistic_checker import statistic_checker
import keyboard
from pymouse import PyMouse

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.hook = keyboard.on_press(self.grab_scanning_event)
        self.souz_team = self.generate_souz()
        self.vragi_team = self.generate_vragi()
        self.checker = statistic_checker()

        self.pushButton.setCheckable(True)
        self.pushButton.clicked.connect(self.activate_scanning)

        self.souz_stats.setStyleSheet("#souz_stats {background-color: rgba(74, 82, 113, 150); border: 1px solid darknavy;}")
        self.vragi_stats.setStyleSheet("#vragi_stats {background-color: rgba(74, 82, 113, 150); border: 1px solid darknavy;}")
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint|QtCore.Qt.WindowType.WindowStaysOnTopHint)

    def grab_scanning_event(self, event):
        if event.event_type == 'down':
            if event.scan_code == 87:
                self.pushButton.click()
            if event.scan_code == 67:
                m = PyMouse()
                m.click(980, 120, 1)
    def activate_scanning(self):
        self.fill_stats()

    def fill_stats(self):
        players = self.checker.return_olenei()
        souz_team_stats, vragi_team_stats = players[0], players[1]
        for i in range(7):
            self.fill_player_stats(self.souz_team, souz_team_stats[i], i)
        for i in range(7):
            self.fill_player_stats(self.vragi_team, vragi_team_stats[i], i)

    def fill_player_stats(self, team, player_stats, index):
        team[index].win_rate_field.setHtml(str(player_stats.win_rate))

    def generate_souz(self):
        souz_team = []
        for i in range(7):
            player = player_stats_ui("", "", "", self.souz_winrates, self.souz_tank, self.souz_tank_stats, self.layoutWidget)
            souz_team.append(player)
        return souz_team

    def generate_vragi(self):
        vragi_team = []
        for i in range(7):
            player = player_stats_ui("", "", "", self.vragi_winrates, self.vragi_tank, self.vragi_tank_stats, self.layoutWidget)
            vragi_team.append(player)
        return vragi_team

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.showFullScreen()
    #window.show()
    app.exec()
