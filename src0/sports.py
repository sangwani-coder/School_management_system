# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sports.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sports(object):
    def setupUi(self, sports):
        sports.setObjectName("sports")
        sports.resize(598, 261)
        sports.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.prt_enrty_form = QtWidgets.QGroupBox(sports)
        self.prt_enrty_form.setGeometry(QtCore.QRect(120, 10, 401, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.prt_enrty_form.setFont(font)
        self.prt_enrty_form.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.prt_enrty_form.setObjectName("prt_enrty_form")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.prt_enrty_form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 361, 131))
        self.formLayoutWidget_2.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.frame = QtWidgets.QFrame(sports)
        self.frame.setGeometry(QtCore.QRect(30, 200, 551, 51))
        self.frame.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 481, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(125, 205, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(125, 205, 127);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(125, 205, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(sports)
        QtCore.QMetaObject.connectSlotsByName(sports)

    def retranslateUi(self, sports):
        _translate = QtCore.QCoreApplication.translate
        sports.setWindowTitle(_translate("sports", "sports"))
        self.prt_enrty_form.setTitle(_translate("sports", "Create houses"))
        self.label_12.setText(_translate("sports", "House name:"))
        self.label_13.setText(_translate("sports", "House colors:"))
        self.label_14.setText(_translate("sports", "House Master:"))
        self.label_15.setText(_translate("sports", "Practice days:"))
        self.comboBox_2.setItemText(0, _translate("sports", "Monday"))
        self.comboBox_2.setItemText(1, _translate("sports", "Tuesday"))
        self.comboBox_2.setItemText(2, _translate("sports", "Wednesday"))
        self.comboBox_2.setItemText(3, _translate("sports", "Thursday"))
        self.comboBox_2.setItemText(4, _translate("sports", "Friday"))
        self.pushButton_3.setText(_translate("sports", "Create house"))
        self.pushButton_4.setText(_translate("sports", "Generate house list"))
        self.pushButton_2.setText(_translate("sports", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sports = QtWidgets.QWidget()
    ui = Ui_sports()
    ui.setupUi(sports)
    sports.show()
    sys.exit(app.exec_())
