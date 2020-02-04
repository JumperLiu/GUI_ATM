# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	IQLabel.py
# @Time		    	:	2020/2/2 0:00
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QApplication, QLabel
from ORM.Common.Styles import get_image
from SysManager.Custom.IQMainWindow import IQMainWindow


class IQLabel(QLabel):
    MP_Signal = pyqtSignal()
    MR_Signal = pyqtSignal()
    ME_Signal = pyqtSignal()
    ML_Signal = pyqtSignal()

    def __init__(self, parent=None):
        super(IQLabel, self).__init__(parent)
        self.setMouseTracking(True)
        self.formatExt: str = 'png'
        self.normalImage: str or None = None
        self.hoverImage: str or None = None
        self.hoverToolTip: str or None = None
        self.parentWindow: IQMainWindow or None = None
        self.__app__: QApplication or None = None
        self.pressed = False
        self.hovered = False
        self.parentWindowMined = False

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

    def __setImage__(self, hover: bool = False):
        # if hover:
        #     if self.hoverImage.find('.{}'.format(self.formatExt)) != -1:
        #         image = self.hoverImage
        #     else:
        #         image = '{}.{}'.format(self.hoverImage, self.formatExt)
        # else:
        #     if self.normalImage.find('.{}'.format(self.formatExt)) != -1:
        #         image = self.normalImage
        #     else:
        #         image = '{}.{}'.format(self.normalImage, self.formatExt)
        image = (self.hoverImage if (self.hoverImage.find('.{}'.format(self.formatExt)) != -1)
                 else '{}.{}'.format(self.hoverImage, self.formatExt)) if hover else \
            (self.normalImage if (self.normalImage.find('.{}'.format(self.formatExt)) != -1)
             else '{}.{}'.format(self.normalImage, self.formatExt))
        self.setPixmap(get_image(image))
        self.repaint()

    def setNormalImage(self):
        self.__setImage__()

    def setHoverImage(self):
        self.__setImage__(True)
        self.setToolTip("<div style='font-family: 微软雅黑; font-size: 12pt; color: yellow;'><b>{}</b>"
                        "</div>".format(self.hoverToolTip))

    def setMinWindow(self):
        self.parentWindow.showMinimized()
        self.parentWindowMined = True

    def setCloseWindow(self):
        self.__app__ = QApplication.instance()
        self.__app__.quit()
