# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_teacher.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_new_teacher(object):
    def setupUi(self, new_teacher):
        new_teacher.setObjectName("new_teacher")
        new_teacher.resize(598, 314)
        new_teacher.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.prt_enrty_form = QtWidgets.QGroupBox(new_teacher)
        self.prt_enrty_form.setGeometry(QtCore.QRect(140, 0, 351, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.prt_enrty_form.setFont(font)
        self.prt_enrty_form.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.prt_enrty_form.setObjectName("prt_enrty_form")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.prt_enrty_form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 331, 181))
        self.formLayoutWidget_2.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.comboBox_5 = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_5.setObjectName("comboBox_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_5)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        self.frame = QtWidgets.QFrame(new_teacher)
        self.frame.setGeometry(QtCore.QRect(40, 250, 551, 80))
        self.frame.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 531, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(125, 205, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(125, 205, 127);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(125, 205, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(new_teacher)
        QtCore.QMetaObject.connectSlotsByName(new_teacher)

    def retranslateUi(self, new_teacher):
        _translate = QtCore.QCoreApplication.translate
        new_teacher.setWindowTitle(_translate("new_teacher", "Add Teacher"))
        self.prt_enrty_form.setTitle(_translate("new_teacher", "Teacher Details"))
        self.label_11.setText(_translate("new_teacher", "Title:"))
        self.label_12.setText(_translate("new_teacher", "First name:"))
        self.label_13.setText(_translate("new_teacher", "Surname:"))
        self.label_14.setText(_translate("new_teacher", "Mobile:"))
        self.label_15.setText(_translate("new_teacher", "Email:"))
        self.label_16.setText(_translate("new_teacher", "Address:"))
        self.pushButton_3.setText(_translate("new_teacher", "Add"))
        self.pushButton_4.setText(_translate("new_teacher", "Reset"))
        self.pushButton_2.setText(_translate("new_teacher", "Preview"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    new_teacher = QtWidgets.QWidget()
    ui = Ui_new_teacher()
    ui.setupUi(new_teacher)
    new_teacher.show()
    sys.exit(app.exec_())