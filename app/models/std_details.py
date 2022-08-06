# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'std_details.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_std_form(object):
    def setupUi(self, std_form):
        std_form.setObjectName("std_form")
        std_form.resize(1001, 489)
        std_form.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.groupBox = QtWidgets.QGroupBox(std_form)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 251, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 231, 76))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.groupBox_2 = QtWidgets.QGroupBox(std_form)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 160, 251, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 201, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.change_tr = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.change_tr.setFont(font)
        self.change_tr.setStyleSheet("background-color: rgb(125, 205, 127);")
        self.change_tr.setObjectName("change_tr")
        self.verticalLayout.addWidget(self.change_tr)
        self.remove_std = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.remove_std.setFont(font)
        self.remove_std.setStyleSheet("background-color: rgb(125, 205, 127);")
        self.remove_std.setObjectName("remove_std")
        self.verticalLayout.addWidget(self.remove_std)
        self.remove_std_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.remove_std_2.setFont(font)
        self.remove_std_2.setStyleSheet("background-color: rgb(125, 205, 127);")
        self.remove_std_2.setObjectName("remove_std_2")
        self.verticalLayout.addWidget(self.remove_std_2)
        self.remove_std_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.remove_std_4.setFont(font)
        self.remove_std_4.setStyleSheet("background-color: rgb(125, 205, 127);")
        self.remove_std_4.setObjectName("remove_std_4")
        self.verticalLayout.addWidget(self.remove_std_4)
        self.groupBox_3 = QtWidgets.QGroupBox(std_form)
        self.groupBox_3.setGeometry(QtCore.QRect(270, 210, 721, 261))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget.setGeometry(QtCore.QRect(0, 20, 731, 231))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(std_form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(390, 10, 381, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.label_Term = QtWidgets.QLabel(std_form)
        self.label_Term.setGeometry(QtCore.QRect(520, 110, 122, 49))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_Term.setFont(font)
        self.label_Term.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.label_Term.setObjectName("label_Term")

        self.retranslateUi(std_form)
        QtCore.QMetaObject.connectSlotsByName(std_form)

    def retranslateUi(self, std_form):
        _translate = QtCore.QCoreApplication.translate
        std_form.setWindowTitle(_translate("std_form", "student details"))
        self.groupBox.setTitle(_translate("std_form", "Search Student"))
        self.label.setText(_translate("std_form", "Find by:"))
        self.comboBox.setItemText(0, _translate("std_form", "Name"))
        self.comboBox.setItemText(1, _translate("std_form", "ID"))
        self.label_2.setText(_translate("std_form", "Search:"))
        self.pushButton.setText(_translate("std_form", "Search"))
        self.groupBox_2.setTitle(_translate("std_form", "Manage Student Details"))
        self.change_tr.setText(_translate("std_form", "Update details"))
        self.remove_std.setText(_translate("std_form", "Delete Student"))
        self.remove_std_2.setText(_translate("std_form", "Change Class"))
        self.remove_std_4.setText(_translate("std_form", "Generate ID"))
        self.groupBox_3.setTitle(_translate("std_form", "Student details"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("std_form", "Std ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("std_form", "Grade"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("std_form", "Firstname"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("std_form", "Surname"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("std_form", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("std_form", "Address"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("std_form", "Fees Paid"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("std_form", "Fees Balance"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("std_form", "Parents name"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("std_form", "Mobile"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("std_form", "Email"))
        self.pushButton_2.setText(_translate("std_form", "Select Term/Year"))
        self.comboBox_2.setItemText(0, _translate("std_form", "Term 1"))
        self.comboBox_2.setItemText(1, _translate("std_form", "Term 2"))
        self.comboBox_2.setItemText(2, _translate("std_form", "Term 3"))
        self.comboBox_3.setItemText(0, _translate("std_form", "2021"))
        self.comboBox_3.setItemText(1, _translate("std_form", "2022"))
        self.comboBox_3.setItemText(2, _translate("std_form", "2023"))
        self.label_Term.setText(_translate("std_form", "Term: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    std_form = QtWidgets.QWidget()
    ui = Ui_std_form()
    ui.setupUi(std_form)
    std_form.show()
    sys.exit(app.exec_())