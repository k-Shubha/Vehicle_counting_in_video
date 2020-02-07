# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1203, 554)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_count = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_count.setGeometry(QtCore.QRect(990, 10, 211, 341))
        self.groupBox_count.setObjectName("groupBox_count")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_count)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_count = QtWidgets.QGridLayout()
        self.gridLayout_count.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_count.setSpacing(6)
        self.gridLayout_count.setObjectName("gridLayout_count")
        self.label_Heavy_Moving_Vehicle = QtWidgets.QLabel(self.groupBox_count)
        self.label_Heavy_Moving_Vehicle.setObjectName("label_Heavy_Moving_Vehicle")
        self.gridLayout_count.addWidget(self.label_Heavy_Moving_Vehicle, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(self.groupBox_count)
        self.label_7.setObjectName("label_7")
        self.gridLayout_count.addWidget(self.label_7, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.groupBox_count)
        self.label_5.setObjectName("label_5")
        self.gridLayout_count.addWidget(self.label_5, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.groupBox_count)
        self.label_6.setObjectName("label_6")
        self.gridLayout_count.addWidget(self.label_6, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_HM_Vehicle_multiaxle = QtWidgets.QLabel(self.groupBox_count)
        self.label_HM_Vehicle_multiaxle.setObjectName("label_HM_Vehicle_multiaxle")
        self.gridLayout_count.addWidget(self.label_HM_Vehicle_multiaxle, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_Medium_Vehicle = QtWidgets.QLabel(self.groupBox_count)
        self.label_Medium_Vehicle.setObjectName("label_Medium_Vehicle")
        self.gridLayout_count.addWidget(self.label_Medium_Vehicle, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)

        
        
        self.label_12 = QtWidgets.QLabel(self.groupBox_count)
        self.label_12.setObjectName("label_12")
        self.gridLayout_count.addWidget(self.label_12, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.groupBox_count)
        self.label_3.setObjectName("label_3")
        self.gridLayout_count.addWidget(self.label_3, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_sum = QtWidgets.QLabel(self.groupBox_count)
        self.label_sum.setObjectName("label_sum")
        self.gridLayout_count.addWidget(self.label_sum, 5, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_Light_Moving_Vehicle = QtWidgets.QLabel(self.groupBox_count)
        self.label_Light_Moving_Vehicle.setObjectName("label_Light_Moving_Vehicle")
        self.gridLayout_count.addWidget(self.label_Light_Moving_Vehicle, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.groupBox_count)
        self.label_4.setObjectName("label_4")
        self.gridLayout_count.addWidget(self.label_4, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.gridLayout_count)
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(10, 10, 960, 540))
        self.label_image.setStyleSheet("background-color: rgb(233, 185, 110);")
        self.label_image.setText("")
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image.setObjectName("label_image")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1020, 360, 151, 181))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_openVideo = QtWidgets.QPushButton(self.widget)
        self.pushButton_openVideo.setObjectName("pushButton_openVideo")
        self.verticalLayout.addWidget(self.pushButton_openVideo)
        self.pushButton_selectArea = QtWidgets.QPushButton(self.widget)
        self.pushButton_selectArea.setObjectName("pushButton_selectArea")
        self.verticalLayout.addWidget(self.pushButton_selectArea)
        self.pushButton_start = QtWidgets.QPushButton(self.widget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout.addWidget(self.pushButton_start)
        self.pushButton_pause = QtWidgets.QPushButton(self.widget)
        self.pushButton_pause.setObjectName("pushButton_pause")
        self.verticalLayout.addWidget(self.pushButton_pause)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Vehicle Counter"))
        self.groupBox_count.setTitle(_translate("mainWindow", "Counting Results"))
        self.label_Heavy_Moving_Vehicle.setText(_translate("mainWindow", "0"))
        
        self.label_5.setText(_translate("mainWindow", "Heavy_Moving_Vehicle"))
        self.label_6.setText(_translate("mainWindow", "HM_Vehicle_multiaxle"))
        self.label_HM_Vehicle_multiaxle.setText(_translate("mainWindow", "0"))
        self.label_Medium_Vehicle.setText(_translate("mainWindow", "0"))
        
        self.label_12.setText(_translate("mainWindow", "sum"))
        self.label_3.setText(_translate("mainWindow", "Light_Moving_Vehicle"))
        self.label_sum.setText(_translate("mainWindow", "0"))
        self.label_Light_Moving_Vehicle.setText(_translate("mainWindow", "0"))
        self.label_4.setText(_translate("mainWindow", "Medium_Vehicle"))
        self.pushButton_openVideo.setText(_translate("mainWindow", "Open Video"))
        self.pushButton_selectArea.setText(_translate("mainWindow", "Select Area"))
        self.pushButton_start.setText(_translate("mainWindow", "Start"))
        self.pushButton_pause.setText(_translate("mainWindow", "Pause"))
