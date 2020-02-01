# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	CustomQLabel.py
# @Time		    	:	2020/2/2 0:00
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QLabel


class CustomQLabel(QLabel):
    MP_Signal = pyqtSignal()
    MR_Signal = pyqtSignal()
    ME_Signal = pyqtSignal()
    ML_Signal = pyqtSignal()

    def __init__(self, parent=None):
        super(CustomQLabel, self).__init__(parent)
        self.setMouseTracking(True)
        self.pressed = False
        self.hovered = False

    def mousePressEvent(self, _: QMouseEvent):
        if not self.pressed:
            self.MP_Signal.emit()
            self.pressed = True

    def mouseReleaseEvent(self, _: QMouseEvent):
        if self.pressed:
            self.MR_Signal.emit()
            self.pressed = False

    def enterEvent(self, *args, **kwargs):
        if not self.hovered:
            self.ME_Signal.emit()
            self.hovered = True

    def leaveEvent(self, *args, **kwargs):
        if self.hovered:
            self.ML_Signal.emit()
            self.hovered = False

