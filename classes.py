from PyQt6 import QtWidgets, QtGui
from PyQt6 import QtCore

class player_stats_ui():
    def __init__(self, win_rate, tank_win_rate, damage, frame_winrates, frame_tank, frame_tank_stats, window):
        font = QtGui.QFont()
        font.setPointSize(10)

        self.win_rate_field = QtWidgets.QTextEdit(window)
        self.add_wr(win_rate, frame_winrates, font)

        self.tank_field = QtWidgets.QTextEdit(window)
        self.add_tank(frame_tank, font)

        self.tank_stats_field = QtWidgets.QTextEdit(window)
        self.add_tank_stats(tank_win_rate,damage,frame_tank_stats,font)


    def add_wr(self, win_rate, frame_winrates, font):
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.ColorRole.Text, QtGui.QColor.fromRgb(0xff, 0xff, 0xff, alpha=255))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.win_rate_field.sizePolicy().hasHeightForWidth())
        self.win_rate_field.setSizePolicy(sizePolicy)
        self.win_rate_field.setMaximumSize(QtCore.QSize(40, 24))
        self.win_rate_field.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.win_rate_field.setStyleSheet("background-color: transparent")
        self.win_rate_field.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.win_rate_field.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.win_rate_field.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.win_rate_field.setPalette(pal)
        self.win_rate_field.setFont(font)
        self.win_rate_field.setHtml(win_rate)
        frame_winrates.insertWidget(frame_winrates.count(), self.win_rate_field)

    def add_tank(self, frame_tank, font):
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.ColorRole.Text, QtGui.QColor.fromRgb(0xff, 0xff, 0xff, alpha=255))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tank_field.sizePolicy().hasHeightForWidth())
        self.tank_field.setSizePolicy(sizePolicy)
        self.tank_field.setMaximumSize(QtCore.QSize(40, 24))
        self.tank_field.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tank_field.setStyleSheet("background-color: transparent")
        self.tank_field.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tank_field.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tank_field.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.tank_field.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.tank_field.setPalette(pal)
        self.tank_field.setFont(font)
        self.tank_field.setHtml("tank:")
        frame_tank.insertWidget(frame_tank.count(), self.tank_field)

    def add_tank_stats(self, tank_win_rate, damage, frame_tank_stats, font):
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.ColorRole.Text, QtGui.QColor.fromRgb(0xff, 0xff, 0xff, alpha=255))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tank_stats_field.sizePolicy().hasHeightForWidth())
        self.tank_stats_field.setSizePolicy(sizePolicy)
        self.tank_stats_field.setMaximumSize(QtCore.QSize(75, 24))
        self.tank_stats_field.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tank_stats_field.setStyleSheet("background-color: transparent")
        self.tank_stats_field.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tank_stats_field.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tank_stats_field.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.tank_stats_field.setPalette(pal)
        self.tank_stats_field.setFont(font)
        self.tank_stats_field.setHtml(tank_win_rate+" | "+damage)
        frame_tank_stats.insertWidget(frame_tank_stats.count(), self.tank_stats_field)

class player_stats():
    def __init__(self, id, win_rate, tank_win_rate, tank_damage):
        self.id = id
        self.win_rate = win_rate
        self.tank_win_rate = tank_win_rate
        self.tank_damage = tank_damage




