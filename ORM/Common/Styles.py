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


def main_background_style() -> str:
    return 'background-color: qlineargradient(spread:pad, x1:0.304, y1:0.0738182, x2:0.637, y2:0.988636, ' \
           'stop:0 rgba(0, 0, 129, 255), stop:0.421569 rgba(0, 85, 207, 255), stop:0.612745 rgba(0, 86, 214, 255), ' \
           'stop:1 rgba(0, 0, 143, 255));'


def title_label_style() -> str:
    return 'background-color: rgba(255, 255, 255, 0);color: rgb(255, 255, 0);'


def normal_label_style() -> str:
    return 'background-color: rgba(255, 255, 255, 0); color: rgb(85, 255, 255);'


def submit_button_style() -> str:
    return '''
            QPushButton#PBTN_Submit {
                background-color: rgba(255, 255, 255, 0);
                color: rgb(0, 255, 0, 0.98);
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
                color: rgb(0, 0, 102, 0.98);
                border-style: inset;
            }
        '''


def reset_button_style() -> str:
    return '''
            QPushButton#PBTN_Reset {
                background-color: rgba(255, 255, 255, 0);
                color: rgb(10, 193, 255, 0.98);
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
                color: rgb(0, 0, 102, 0.98);
                border-style: inset;
            }
        '''


def normal_line_edit_style() -> str:
    return 'background-color: rgba(255, 255, 255, 0); border-style: outset; border-width: 1px; border-radius: 8px; ' \
           'border-color: rgb(255, 255, 255); color: rgb(255, 255, 0);'


def password_line_edit_style() -> str:
    return 'background-color: rgba(255, 255, 255, 0); border-style: outset; border-width: 1px; border-radius: 8px; ' \
           'border-color: rgb(255, 255, 255); color: rgb(255, 0, 0);'
