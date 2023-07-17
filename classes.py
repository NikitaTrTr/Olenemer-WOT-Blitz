from PyQt6 import QtWidgets, QtGui
from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit


class PlayerStats:
    def __init__(self, player_nickname: str, win_rate: float, tank_win_rate: float, tank_damage: int):
        self.player_nickname = player_nickname
        self.win_rate = win_rate
        self.tank_win_rate = tank_win_rate
        self.tank_damage = tank_damage


class PlayerStatsUi:
    def __init__(self, window: QWidget, team_panel: QVBoxLayout):
        player_line = QHBoxLayout(window)
        player_line.setSpacing(0)

        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.ColorRole.Text, QtGui.QColor.fromRgb(0xff, 0xff, 0xff, alpha=255))

        nickname_field = self.configure_field(QTextEdit())
        player_wr_field = self.configure_field(QTextEdit())
        tank_label = self.configure_field(QTextEdit())
        tank_wr_damage = self.configure_field(QTextEdit())
        nickname_field.setPalette(pal)
        tank_label.setPalette(pal)
        tank_wr_damage.setPalette(pal)
        player_wr_field.setPalette(pal)

        nickname_field.setMaximumSize(QtCore.QSize(100, 24))
        player_wr_field.setMaximumSize(QtCore.QSize(47, 24))
        tank_label.setMaximumSize(QtCore.QSize(38, 24))
        tank_wr_damage.setMaximumSize(QtCore.QSize(100, 24))

        self.nickname_field = nickname_field
        self.player_wr_field = player_wr_field
        self.tank_label = tank_label
        self.tank_wr_damage = tank_wr_damage

        player_line.addWidget(nickname_field)
        player_line.addWidget(player_wr_field)
        player_line.addWidget(tank_label)
        player_line.addWidget(tank_wr_damage)

        team_panel.addLayout(player_line)

    @staticmethod
    def configure_field(field: QTextEdit):
        field.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum,
                                                  QtWidgets.QSizePolicy.Policy.Maximum))
        field.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        field.setStyleSheet("background-color: transparent")
        field.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        field.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        field.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        return field

    def set_stats(self, player_stats: PlayerStats):
        nick = player_stats.player_nickname
        wr = str(player_stats.win_rate)[0:4] + '%'
        tank_wr = str(player_stats.tank_win_rate)[0:4]
        damage = str(player_stats.tank_damage)
        self.nickname_field.setHtml(self.format_field(nick))
        self.player_wr_field.setHtml(self.format_field(wr))
        self.tank_wr_damage.setHtml(self.format_field(f'{tank_wr}% l {damage}'))
        self.tank_label.setHtml(self.format_field('tank: '))

    @staticmethod
    def format_field(data: str):
        return f'<span style="font-family: Arial narrow; font-size: 16px;">{data}</span>'
