# -*- coding: utf-8 -*-

"""
    @project：PyQt5Book
    @Author：董超
    @file：callLayout_Demo_LayoutManage.py
    @date：2023/5/28
    @software：PyCharm
    @github: https://github.com/dongchao612/PyQt5Book
"""
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

from Chapter03.Layout_Demo_LayoutManage.Layout_Demo_LayoutManage import Ui_LayoutDemo


class LayoutDemo(QMainWindow, Ui_LayoutDemo):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(LayoutDemo, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        print('收益_min:', self.doubleSpinBox_returns_min.text())
        print('收益_max:', self.doubleSpinBox_returns_max.text())
        print('最大回撤_min:', self.doubleSpinBox_maxdrawdown_min.text())
        print('最大回撤_max:', self.doubleSpinBox_maxdrawdown_max.text())
        print('sharp比_min:', self.doubleSpinBox_sharp_min.text())
        print('sharp比_max:', self.doubleSpinBox_sharp_max.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = LayoutDemo()
    ui.show()
    sys.exit(app.exec_())
