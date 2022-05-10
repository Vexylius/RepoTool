# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.15.4

from PyQt5 import QtCore, QtGui, QtWidgets
from selprgui import Ui_SelectPR
import loader

class Ui_LoadRepoWindow(object):
    def setupUi(self, LoadRepoWindow):
        LoadRepoWindow.setObjectName("LoadRepoWindow")
        LoadRepoWindow.setEnabled(True)
        LoadRepoWindow.resize(440, 110)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoadRepoWindow.sizePolicy().hasHeightForWidth())
        LoadRepoWindow.setSizePolicy(sizePolicy)
        LoadRepoWindow.setMinimumSize(QtCore.QSize(440, 110))
        LoadRepoWindow.setMaximumSize(QtCore.QSize(440, 110))
        LoadRepoWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        LoadRepoWindow.setAcceptDrops(False)
        LoadRepoWindow.setWindowTitle("RepoTool")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("repoTool.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoadRepoWindow.setWindowIcon(icon)
        LoadRepoWindow.setToolTip("")
        LoadRepoWindow.setAccessibleDescription("")
        LoadRepoWindow.setWindowFilePath("")
        LoadRepoWindow.setIconSize(QtCore.QSize(50, 50))
        LoadRepoWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(LoadRepoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.repoLinkInput = QtWidgets.QLineEdit(self.centralwidget)
        self.repoLinkInput.setGeometry(QtCore.QRect(10, 30, 421, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setItalic(True)
        self.repoLinkInput.setFont(font)
        self.repoLinkInput.setText("")
        self.repoLinkInput.setPlaceholderText("https://github.com/organisation/repository")
        self.repoLinkInput.setObjectName("repoLinkInput")
        self.loadRepoButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonPressed())
        self.loadRepoButton.setGeometry(QtCore.QRect(10, 60, 421, 23))
        self.loadRepoButton.setObjectName("loadRepoButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(200, 10, 231, 20))
        self.errorLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.errorLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.errorLabel.setText("")
        self.errorLabel.setTextFormat(QtCore.Qt.RichText)
        self.errorLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.errorLabel.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.errorLabel.setObjectName("errorLabel")
        LoadRepoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoadRepoWindow)
        self.statusbar.setObjectName("statusbar")
        LoadRepoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoadRepoWindow)
        QtCore.QMetaObject.connectSlotsByName(LoadRepoWindow)

    def retranslateUi(self, LoadRepoWindow):
        _translate = QtCore.QCoreApplication.translate
        self.loadRepoButton.setText(_translate("LoadRepoWindow", "Load the repo"))
        self.label.setText(_translate("LoadRepoWindow", "Link to the repository:"))

    def openSelPR(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SelectPR()
        self.ui.setupUi(self.window)
        self.window.show()

    def buttonPressed(self):
        repo = self.repoLinkInput.text()
        errTxt = "".join(["<span style='color:#ff0000;'> ", "ERR: Unknown Error"])
        if repo != '':
            if loader.loadRepo(repo):
                errTxt = "".join(["<span style='color:#00ff00;'> ", "Repo loaded!"])
                self.openSelPR(repo)
            else:
                errTxt = "".join(["<span style='color:#ff0000;'> ", "ERR: Invalid repo link"])
        else:
            errTxt = "".join(["<span style='color:#ff0000;'> ", "ERR: No link given"])
        self.errorLabel.setText(errTxt)
