# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 740)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 731, 661))
        self.tabWidget.setObjectName("tabWidget")
        self.descMD = QtWidgets.QWidget()
        self.descMD.setObjectName("descMD")
        self.widget = QtWidgets.QWidget(self.descMD)
        self.widget.setGeometry(QtCore.QRect(10, 50, 431, 23))
        self.widget.setObjectName("widget")
        self.resourceIdForm = QtWidgets.QFormLayout(self.widget)
        self.resourceIdForm.setContentsMargins(11, 11, 11, 11)
        self.resourceIdForm.setSpacing(6)
        self.resourceIdForm.setObjectName("resourceIdForm")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(59, 0))
        self.label.setObjectName("label")
        self.resourceIdForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.resource_id = QtWidgets.QLineEdit(self.widget)
        self.resource_id.setMinimumSize(QtCore.QSize(200, 0))
        self.resource_id.setObjectName("resource_id")
        self.resourceIdForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.resource_id)
        self.layoutWidget_2 = QtWidgets.QWidget(self.descMD)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 431, 23))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.resourceIdForm_2 = QtWidgets.QFormLayout(self.layoutWidget_2)
        self.resourceIdForm_2.setContentsMargins(11, 11, 11, 11)
        self.resourceIdForm_2.setSpacing(6)
        self.resourceIdForm_2.setObjectName("resourceIdForm_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setMinimumSize(QtCore.QSize(59, 0))
        self.label_2.setObjectName("label_2")
        self.resourceIdForm_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.resource_id_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.resource_id_2.setMinimumSize(QtCore.QSize(200, 0))
        self.resource_id_2.setObjectName("resource_id_2")
        self.resourceIdForm_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.resource_id_2)
        self.widget1 = QtWidgets.QWidget(self.descMD)
        self.widget1.setGeometry(QtCore.QRect(20, 420, 338, 200))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.language_list = QtWidgets.QListWidget(self.widget1)
        self.language_list.setObjectName("language_list")
        self.verticalLayout_5.addWidget(self.language_list)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.toolButton_6 = QtWidgets.QToolButton(self.widget1)
        self.toolButton_6.setObjectName("toolButton_6")
        self.horizontalLayout_4.addWidget(self.toolButton_6)
        self.toolButton_5 = QtWidgets.QToolButton(self.widget1)
        self.toolButton_5.setObjectName("toolButton_5")
        self.horizontalLayout_4.addWidget(self.toolButton_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.languagelist_upbutton = QtWidgets.QPushButton(self.widget1)
        self.languagelist_upbutton.setEnabled(False)
        self.languagelist_upbutton.setObjectName("languagelist_upbutton")
        self.horizontalLayout_4.addWidget(self.languagelist_upbutton)
        self.languagelist_downbutton = QtWidgets.QPushButton(self.widget1)
        self.languagelist_downbutton.setEnabled(False)
        self.languagelist_downbutton.setObjectName("languagelist_downbutton")
        self.horizontalLayout_4.addWidget(self.languagelist_downbutton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.widget2 = QtWidgets.QWidget(self.descMD)
        self.widget2.setGeometry(QtCore.QRect(20, 80, 301, 200))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.description_list = QtWidgets.QListWidget(self.widget2)
        self.description_list.setObjectName("description_list")
        self.verticalLayout.addWidget(self.description_list)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButton = QtWidgets.QToolButton(self.widget2)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.toolButton_2 = QtWidgets.QToolButton(self.widget2)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.descriptionlist_upbutton = QtWidgets.QPushButton(self.widget2)
        self.descriptionlist_upbutton.setEnabled(False)
        self.descriptionlist_upbutton.setObjectName("descriptionlist_upbutton")
        self.horizontalLayout_2.addWidget(self.descriptionlist_upbutton)
        self.descriptionlist_downbutton = QtWidgets.QPushButton(self.widget2)
        self.descriptionlist_downbutton.setEnabled(False)
        self.descriptionlist_downbutton.setObjectName("descriptionlist_downbutton")
        self.horizontalLayout_2.addWidget(self.descriptionlist_downbutton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.widget3 = QtWidgets.QWidget(self.descMD)
        self.widget3.setGeometry(QtCore.QRect(370, 90, 338, 199))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.widget3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.contributor_list = QtWidgets.QListWidget(self.widget3)
        self.contributor_list.setObjectName("contributor_list")
        self.verticalLayout_4.addWidget(self.contributor_list)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.widget3)
        self.toolButton_4.setObjectName("toolButton_4")
        self.horizontalLayout_3.addWidget(self.toolButton_4)
        self.toolButton_3 = QtWidgets.QToolButton(self.widget3)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_3.addWidget(self.toolButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.contributorlist_upbutton = QtWidgets.QPushButton(self.widget3)
        self.contributorlist_upbutton.setEnabled(False)
        self.contributorlist_upbutton.setObjectName("contributorlist_upbutton")
        self.horizontalLayout_3.addWidget(self.contributorlist_upbutton)
        self.contributorlist_downbutton = QtWidgets.QPushButton(self.widget3)
        self.contributorlist_downbutton.setEnabled(False)
        self.contributorlist_downbutton.setObjectName("contributorlist_downbutton")
        self.horizontalLayout_3.addWidget(self.contributorlist_downbutton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.descMD, "")
        self.analogInst = QtWidgets.QWidget()
        self.analogInst.setObjectName("analogInst")
        self.widget4 = QtWidgets.QWidget(self.analogInst)
        self.widget4.setGeometry(QtCore.QRect(10, 10, 331, 49))
        self.widget4.setObjectName("widget4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.analog_id = QtWidgets.QLineEdit(self.widget4)
        self.analog_id.setObjectName("analog_id")
        self.verticalLayout_3.addWidget(self.analog_id)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.widget4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.analog_source = QtWidgets.QLineEdit(self.widget4)
        self.analog_source.setObjectName("analog_source")
        self.verticalLayout_6.addWidget(self.analog_source)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.widget5 = QtWidgets.QWidget(self.analogInst)
        self.widget5.setGeometry(QtCore.QRect(350, 10, 351, 49))
        self.widget5.setObjectName("widget5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget5)
        self.horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.widget5)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.analog_location = QtWidgets.QLineEdit(self.widget5)
        self.analog_location.setObjectName("analog_location")
        self.verticalLayout_7.addWidget(self.analog_location)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.widget5)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9)
        self.analog_date = QtWidgets.QLineEdit(self.widget5)
        self.analog_date.setObjectName("analog_date")
        self.verticalLayout_8.addWidget(self.analog_date)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.tape_type = QtWidgets.QComboBox(self.analogInst)
        self.tape_type.setGeometry(QtCore.QRect(10, 80, 261, 31))
        self.tape_type.setObjectName("tape_type")
        self.tape_type.addItem("")
        self.tape_type.addItem("")
        self.tape_type.addItem("")
        self.analog_tracklayout = QtWidgets.QComboBox(self.analogInst)
        self.analog_tracklayout.setGeometry(QtCore.QRect(10, 180, 261, 31))
        self.analog_tracklayout.setObjectName("analog_tracklayout")
        self.analog_tracklayout.addItem("")
        self.analog_tracklayout.addItem("")
        self.analog_tracklayout.addItem("")
        self.analog_tracklayout.addItem("")
        self.analog_tracklayout.addItem("")
        self.analog_tracklayout.addItem("")
        self.analog_tracklayout.setItemText(5, "")
        self.layoutWidget = QtWidgets.QWidget(self.analogInst)
        self.layoutWidget.setGeometry(QtCore.QRect(290, 70, 411, 551))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.analog_premis_list = QtWidgets.QListWidget(self.layoutWidget)
        self.analog_premis_list.setObjectName("analog_premis_list")
        self.verticalLayout_9.addWidget(self.analog_premis_list)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.toolButton_8 = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton_8.setObjectName("toolButton_8")
        self.horizontalLayout_8.addWidget(self.toolButton_8)
        self.toolButton_7 = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton_7.setObjectName("toolButton_7")
        self.horizontalLayout_8.addWidget(self.toolButton_7)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.analogpremis_upbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.analogpremis_upbutton.setEnabled(False)
        self.analogpremis_upbutton.setObjectName("analogpremis_upbutton")
        self.horizontalLayout_8.addWidget(self.analogpremis_upbutton)
        self.analogpremis_downbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.analogpremis_downbutton.setEnabled(False)
        self.analogpremis_downbutton.setObjectName("analogpremis_downbutton")
        self.horizontalLayout_8.addWidget(self.analogpremis_downbutton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.analog_generation = QtWidgets.QComboBox(self.analogInst)
        self.analog_generation.setGeometry(QtCore.QRect(10, 120, 261, 31))
        self.analog_generation.setObjectName("analog_generation")
        self.analog_generation.addItem("")
        self.analog_generation.addItem("")
        self.analog_generation.addItem("")
        self.analog_generation.setItemText(2, "")
        self.analog_tapespeed = QtWidgets.QComboBox(self.analogInst)
        self.analog_tapespeed.setGeometry(QtCore.QRect(10, 220, 261, 31))
        self.analog_tapespeed.setObjectName("analog_tapespeed")
        self.analog_tapespeed.addItem("")
        self.analog_tapespeed.addItem("")
        self.analog_tapespeed.addItem("")
        self.analog_tapespeed.addItem("")
        self.analog_tapespeed.addItem("")
        self.analog_tapespeed.setItemText(4, "")
        self.tape_type.raise_()
        self.analog_tracklayout.raise_()
        self.layoutWidget.raise_()
        self.analog_generation.raise_()
        self.analog_tapespeed.raise_()
        self.tabWidget.addTab(self.analogInst, "")
        self.digitalInst = QtWidgets.QWidget()
        self.digitalInst.setObjectName("digitalInst")
        self.layoutWidget_7 = QtWidgets.QWidget(self.digitalInst)
        self.layoutWidget_7.setGeometry(QtCore.QRect(10, 20, 701, 601))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_11.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.digitalinstantiation_list = QtWidgets.QListWidget(self.layoutWidget_7)
        self.digitalinstantiation_list.setObjectName("digitalinstantiation_list")
        self.verticalLayout_16.addWidget(self.digitalinstantiation_list)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.toolButton_10 = QtWidgets.QToolButton(self.layoutWidget_7)
        self.toolButton_10.setObjectName("toolButton_10")
        self.horizontalLayout_12.addWidget(self.toolButton_10)
        self.toolButton_9 = QtWidgets.QToolButton(self.layoutWidget_7)
        self.toolButton_9.setObjectName("toolButton_9")
        self.horizontalLayout_12.addWidget(self.toolButton_9)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.digitalinstantiation_upbutton = QtWidgets.QPushButton(self.layoutWidget_7)
        self.digitalinstantiation_upbutton.setEnabled(False)
        self.digitalinstantiation_upbutton.setObjectName("digitalinstantiation_upbutton")
        self.horizontalLayout_12.addWidget(self.digitalinstantiation_upbutton)
        self.digitalinstantiation_downbutton = QtWidgets.QPushButton(self.layoutWidget_7)
        self.digitalinstantiation_downbutton.setEnabled(False)
        self.digitalinstantiation_downbutton.setObjectName("digitalinstantiation_downbutton")
        self.horizontalLayout_12.addWidget(self.digitalinstantiation_downbutton)
        self.verticalLayout_16.addLayout(self.horizontalLayout_12)
        self.verticalLayout_11.addLayout(self.verticalLayout_16)
        self.layoutWidget_7.raise_()
        self.digitalinstantiation_list.raise_()
        self.tabWidget.addTab(self.digitalInst, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 740, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionBlow_away = QtWidgets.QAction(MainWindow)
        self.actionBlow_away.setObjectName("actionBlow_away")
        self.actionFoot = QtWidgets.QAction(MainWindow)
        self.actionFoot.setObjectName("actionFoot")
        self.actionHead = QtWidgets.QAction(MainWindow)
        self.actionHead.setObjectName("actionHead")
        self.actionFingers = QtWidgets.QAction(MainWindow)
        self.actionFingers.setObjectName("actionFingers")
        self.actionFoo = QtWidgets.QAction(MainWindow)
        self.actionFoo.setObjectName("actionFoo")
        self.actionBar = QtWidgets.QAction(MainWindow)
        self.actionBar.setObjectName("actionBar")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionClose)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PBCore Editor"))
        self.label.setText(_translate("MainWindow", "Resource ID:"))
        self.label_2.setText(_translate("MainWindow", "Resource Title:"))
        self.label_7.setText(_translate("MainWindow", "Language(s):"))
        self.toolButton_6.setText(_translate("MainWindow", "Add"))
        self.toolButton_5.setText(_translate("MainWindow", "Remove"))
        self.languagelist_upbutton.setText(_translate("MainWindow", "↑"))
        self.languagelist_downbutton.setText(_translate("MainWindow", "↓"))
        self.label_3.setText(_translate("MainWindow", "Description(s):"))
        self.toolButton.setText(_translate("MainWindow", "Add"))
        self.toolButton_2.setText(_translate("MainWindow", "Remove"))
        self.descriptionlist_upbutton.setText(_translate("MainWindow", "↑"))
        self.descriptionlist_downbutton.setText(_translate("MainWindow", "↓"))
        self.label_6.setText(_translate("MainWindow", "Contributor(s):"))
        self.toolButton_4.setText(_translate("MainWindow", "Add"))
        self.toolButton_3.setText(_translate("MainWindow", "Remove"))
        self.contributorlist_upbutton.setText(_translate("MainWindow", "↑"))
        self.contributorlist_downbutton.setText(_translate("MainWindow", "↓"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.descMD), _translate("MainWindow", "Descriptive Metadata"))
        self.label_4.setText(_translate("MainWindow", "Identifier:"))
        self.label_5.setText(_translate("MainWindow", "Source:"))
        self.label_8.setText(_translate("MainWindow", "Location:"))
        self.label_9.setText(_translate("MainWindow", "Date:"))
        self.tape_type.setItemText(0, _translate("MainWindow", "1/4\" audio tape"))
        self.tape_type.setItemText(1, _translate("MainWindow", "Cassette tape"))
        self.tape_type.setItemText(2, _translate("MainWindow", "Microcassette"))
        self.analog_tracklayout.setItemText(0, _translate("MainWindow", "Half-track stereo"))
        self.analog_tracklayout.setItemText(1, _translate("MainWindow", "Half-track mono"))
        self.analog_tracklayout.setItemText(2, _translate("MainWindow", "Full-track mono"))
        self.analog_tracklayout.setItemText(3, _translate("MainWindow", "Quarter-track stereo"))
        self.analog_tracklayout.setItemText(4, _translate("MainWindow", "Four-track"))
        self.label_10.setText(_translate("MainWindow", "PREMIS event(s):"))
        self.toolButton_8.setText(_translate("MainWindow", "Add"))
        self.toolButton_7.setText(_translate("MainWindow", "Remove"))
        self.analogpremis_upbutton.setText(_translate("MainWindow", "↑"))
        self.analogpremis_downbutton.setText(_translate("MainWindow", "↓"))
        self.analog_generation.setItemText(0, _translate("MainWindow", "Original"))
        self.analog_generation.setItemText(1, _translate("MainWindow", "Copy"))
        self.analog_tapespeed.setItemText(0, _translate("MainWindow", "7.5 ips"))
        self.analog_tapespeed.setItemText(1, _translate("MainWindow", "3.75 ips"))
        self.analog_tapespeed.setItemText(2, _translate("MainWindow", "1.875 ips"))
        self.analog_tapespeed.setItemText(3, _translate("MainWindow", "15 ips"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analogInst), _translate("MainWindow", "Analog Instantiation"))
        self.toolButton_10.setText(_translate("MainWindow", "Add"))
        self.toolButton_9.setText(_translate("MainWindow", "Remove"))
        self.digitalinstantiation_upbutton.setText(_translate("MainWindow", "↑"))
        self.digitalinstantiation_downbutton.setText(_translate("MainWindow", "↓"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.digitalInst), _translate("MainWindow", "Digital Instantiations"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New..."))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
        self.actionBlow_away.setText(_translate("MainWindow", "Blow away..."))
        self.actionFoot.setText(_translate("MainWindow", "Foot"))
        self.actionHead.setText(_translate("MainWindow", "Head"))
        self.actionFingers.setText(_translate("MainWindow", "Fingers"))
        self.actionFoo.setText(_translate("MainWindow", "Foo"))
        self.actionBar.setText(_translate("MainWindow", "Bar"))

