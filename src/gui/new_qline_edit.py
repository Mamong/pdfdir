# -*- coding:utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class NewQLineEdit(QtWidgets.QLineEdit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)  # 删除没有影响，目前不确定（因为True和False测试结果一样）
        self.setDragEnabled(True)  # 删除没有影响，（因为True和False测试结果一样）

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():  # 当文件拖入此区域时为True
            event.accept()  # 接受拖入文件
        else:
            event.ignore()  # 忽略拖入文件

    def dropEvent(self, event):    # 本方法为父类方法，本方法中的event为鼠标放事件对象
        urls = [u for u in event.mimeData().urls()]  # 范围文件路径的Qt内部类型对象列表，由于支持多个文件同时拖入所以使用列表存放
        for url in urls:
            self.setText(url.path()[1:])   # 将Qt内部类型转换为字符串类型