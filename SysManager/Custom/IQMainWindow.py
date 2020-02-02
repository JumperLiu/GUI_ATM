# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	IQMainWindow.py
# @Time		    	:	2020/2/1 22:42
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QMouseEvent
from PyQt5.QtWidgets import QMainWindow


class IQMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(IQMainWindow, self).__init__(parent)
        self.m_flag = False
        self.m_position = None

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, event: QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_position)
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.m_flag = False
        self.setCursor(Qt.ArrowCursor)
