# -- * -- coding : utf-8 -- * --
# @Author	    	:	Jumper.Liu
# @Project	    	:	GUI_ATM_Project
# @File		    	:	App.py
# @Time		    	:	2020/1/16 13:26
# @Contact	    	:	Cynosure0313@live.cn
# @License	    	:	(C) Copyright 2019-2020
# @Software(IDE)	:	PyCharm
# @Site		    	:	https://www.jetbrains.com/pycharm/
# @Version	    	:	Python 3.8.0
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from SysManager import MainWindow
    from SysManager.CustomQMainWindow import CustomQMainWindow
    app = QApplication(sys.argv)
    mw = CustomQMainWindow()
    ui = MainWindow.Ui_MainWindow()
    ui.setupUi(mw)
    mw.show()
    sys.exit(app.exec_())
