# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.15.4

from PyQt5 import QtCore, QtGui, QtWidgets
from github import Github

class Ui_SelectPR(object):
    def setupUi(self, SelectPR):
        SelectPR.setObjectName("SelectPR")
        SelectPR.resize(630, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SelectPR.sizePolicy().hasHeightForWidth())
        SelectPR.setSizePolicy(sizePolicy)
        SelectPR.setMinimumSize(QtCore.QSize(630, 650))
        SelectPR.setMaximumSize(QtCore.QSize(630, 650))
        SelectPR.setWindowTitle("RepoTool - Select PRs")
        self.prlistAll = QtWidgets.QListWidget(SelectPR)
        self.prlistAll.setGeometry(QtCore.QRect(10, 70, 301, 511))
        self.prlistAll.setObjectName("prlistAll")
        self.prlistSelected = QtWidgets.QListWidget(SelectPR)
        self.prlistSelected.setGeometry(QtCore.QRect(320, 70, 301, 511))
        self.prlistSelected.setObjectName("prlistSelected")
        self.repoName = QtWidgets.QLabel(SelectPR)
        self.repoName.setGeometry(QtCore.QRect(10, 10, 610, 40))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.repoName.setFont(font)
        self.repoName.setWhatsThis("")
        self.repoName.setTextFormat(QtCore.Qt.AutoText)
        self.repoName.setAlignment(QtCore.Qt.AlignCenter)
        self.repoName.setObjectName("repoName")
        self.pushButton = QtWidgets.QPushButton(SelectPR)
        self.pushButton.setGeometry(QtCore.QRect(10, 590, 611, 51))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(SelectPR)
        self.label.setGeometry(QtCore.QRect(10, 40, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(SelectPR)
        self.label_2.setGeometry(QtCore.QRect(320, 40, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(SelectPR)
        QtCore.QMetaObject.connectSlotsByName(SelectPR)

    def retranslateUi(self, SelectPR):
        _translate = QtCore.QCoreApplication.translate
        self.repoName.setText(_translate("SelectPR", "Organisation/Repo"))
        self.pushButton.setText(_translate("SelectPR", "Check for conflicts"))
        self.label.setText(_translate("SelectPR", "Available PRs"))
        self.label_2.setText(_translate("SelectPR", "Selected PRs"))


    def loadPRs(self, repo):
        gh = Github().get_repo(repo)
        for pr in gh.get_pulls(state='open', sort='created', base='master'):
            pullString = ''.join(["#", str(pr.number), " - ", pr.title])
            self.prlistAll.addItem(pullString)
            print(pullString)
