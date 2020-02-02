# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	Styles.py
# @Time		    	:	2020/2/1 11:16
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.1
from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPixmap
from ORM.Common.Enums import MessageDialogType


def main_background_style() -> str:
    return 'background-color: qlineargradient(spread:pad, x1:0.304, y1:0.0738182, x2:0.637, y2:0.988636, ' \
           'stop:0 rgba(0, 0, 129, 255), stop:0.421569 rgba(0, 85, 207, 255), stop:0.612745 rgba(0, 86, 214, 255), ' \
           'stop:1 rgba(0, 0, 143, 255)); border-radius: 16px;'


def dialog_background_style(message_dialog_type: MessageDialogType = MessageDialogType.ABOUT) -> str:
    if message_dialog_type == MessageDialogType.ABOUT:
        pass
    elif message_dialog_type == MessageDialogType.ASK:
        pass
    elif message_dialog_type == MessageDialogType.INFORMATION:
        pass
    elif message_dialog_type == MessageDialogType.WARNING:
        pass
    elif message_dialog_type == MessageDialogType.ERROR:
        pass
    elif message_dialog_type == MessageDialogType.SUCCESS:
        pass
    else:
        pass
    return 'background-color: qlineargradient(spread:pad, x1:0.441, y1:0.171091, x2:0.441, y2:1, ' \
           'stop:0 rgba(38, 0, 129, 255), stop:0.632353 rgba(0, 0, 0, 255), stop:1 rgba(0, 135, 255, 255)); ' \
           'border-radius: 16px;'


def transparent_label_style() -> str:
    return 'background-color: rgba(255, 255, 255, 0);'


def head_label_style() -> str:
    return '''
            QLabel#LBL_Title_Head {
                background-color: rgba(255, 255, 255, 0);
                color: rgba(255, 255, 255, 0.98);
            }
            QLabel#LBL_Title_Head:hover {
                background-color: rgba(255, 255, 255, 0);
                color: rgba(0, 255, 0, 0.98);
            }
        '''


def title_label_style() -> str:
    return 'background-color: rgba(255, 255, 255, 0);color: rgb(255, 255, 0);'


def normal_label_style() -> str:
    return 'background-color: rgba(255, 255, 255, 0); color: rgb(85, 255, 255);'


def submit_button_style() -> str:
    return '''
            QPushButton#PBTN_Submit {
                background-color: rgba(255, 255, 255, 0);
                color: rgba(0, 255, 0, 0.98);
                border-style: outset;
                border-width: 2px;
                border-radius: 8px;
                border-color: beige;
                padding-left: 24px;
                padding-right: 24px;
                padding-top: 6px;
                padding-bottom: 6px;
            }
            QPushButton#PBTN_Submit:hover {
                background-color: rgba(255, 255, 0, 0.98);
                color: rgba(0, 0, 102, 0.98);
                border-style: inset;
            }
        '''


def reset_button_style() -> str:
    return '''
            QPushButton#PBTN_Reset {
                background-color: rgba(255, 255, 255, 0);
                color: rgba(10, 193, 255, 0.98);
                border-style: outset;
                border-width: 2px;
                border-radius: 8px;
                border-color: beige;
                padding-left: 24px;
                padding-right: 24px;
                padding-top: 6px;
                padding-bottom: 6px;
            }
            QPushButton#PBTN_Reset:hover {
                background-color: rgba(255, 255, 0, 0.98);
                color: rgba(0, 0, 102, 0.98);
                border-style: inset;
            }
        '''


def normal_line_edit_style() -> str:
    return 'background-color: rgba(255, 255, 255, 0); border-style: outset; border-width: 1px; border-radius: 8px; ' \
           'border-color: rgb(255, 255, 255); color: rgb(255, 255, 0);'


def password_line_edit_style() -> str:
    return 'background-color: rgba(255, 255, 255, 0); border-style: outset; border-width: 1px; border-radius: 8px; ' \
           'border-color: rgb(255, 255, 255); color: rgb(255, 0, 0);'


def msg_title_style() -> str:
    return 'background-color: rgba(255, 255, 255, 0); color: rgba(255, 255, 0, 0.98);'


def msg_content_style() -> str:
    return 'background-color: rgba(255, 255, 255, 0); color: rgba(255, 255, 255, 0.98);'


def msg_head_style() -> str:
    return '''
            QLabel#LBL_01_Head_Title {
                background-color: rgba(255, 255, 255, 0);
                color: rgba(255, 255, 255, 0.98);
            }
            QLabel#LBL_01_Head_Title:hover {
                background-color: rgba(255, 255, 255, 0);
                color: rgba(0, 255, 0, 0.98);
            }
        '''


def msg_submit_style() -> str:
    return '''
            QPushButton#PBTN_Submit {
                background-color: rgba(255, 255, 255, 0);
                color: rgba(0, 255, 0, 0.98);
            }
            QPushButton#PBTN_Submit:hover {
                color: rgba(0, 102, 0, 0.98);
            }
        '''


def msg_reset_style() -> str:
    return '''
            QPushButton#PBTN_Reset {
                background-color: rgba(255, 255, 255, 0);
                color: rgba(0, 0, 255, 0.98);
            }
            QPushButton#PBTN_Reset:hover {
                color: rgba(0, 0, 102, 0.98);
            }
        '''


def msg_cancel_style() -> str:
    return '''
            QPushButton#PBTN_Cancel {
                background-color: rgba(255, 255, 255, 0);
                color: rgba(255, 0, 0, 0.98);
            }
            QPushButton#PBTN_Cancel:hover {
                color: rgba(102, 0, 0, 0.98);
            }
        '''


def message_dialog_image_style(image_name: str = 'information.png') -> QPixmap:
    return QPixmap().fromImage(QImage('./Resources/{}'.format(image_name)))


def get_image(image_name: str = None, width: int = 40, height: int = 40) -> QPixmap:
    return message_dialog_image_style(image_name).scaled(QtCore.QSize(width, height), QtCore.Qt.KeepAspectRatio)


def msg_image(msg_type: MessageDialogType = MessageDialogType.ABOUT) -> QPixmap:
    if msg_type == MessageDialogType.ABOUT:
        return get_image('about.png', 96, 96)
    elif msg_type == MessageDialogType.ASK:
        return get_image('ask.png', 96, 96)
    elif msg_type == MessageDialogType.INFORMATION:
        return get_image('information.png', 96, 96)
    elif msg_type == MessageDialogType.WARNING:
        return get_image('warning.png', 96, 96)
    elif msg_type == MessageDialogType.ERROR:
        return get_image('error.png', 96, 96)
    elif msg_type == MessageDialogType.SUCCESS:
        return get_image('success.png', 96, 96)
    else:
        return get_image('fails.png', 96, 96)
