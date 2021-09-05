# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(969, 588)
        MainWindow.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Term = QtWidgets.QLabel(self.centralwidget)
        self.label_Term.setGeometry(QtCore.QRect(210, 0, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_Term.setFont(font)
        self.label_Term.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.label_Term.setObjectName("label_Term")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 161, 541))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 161, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.display_all_Button = QtWidgets.QPushButton(self.verticalLayoutWidget, clicked=lambda: self.load_data())
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.display_all_Button.setFont(font)
        self.display_all_Button.setStyleSheet("background-color: rgb(125, 205, 127);\n"
"")
        self.display_all_Button.setObjectName("display_all_Button")
        self.verticalLayout.addWidget(self.display_all_Button)
        self.dsp_owe_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.dsp_owe_Button.setFont(font)
        self.dsp_owe_Button.setObjectName("dsp_owe_Button")
        self.verticalLayout.addWidget(self.dsp_owe_Button)
        self.dsp_full_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.dsp_full_Button.setFont(font)
        self.dsp_full_Button.setObjectName("dsp_full_Button")
        self.verticalLayout.addWidget(self.dsp_full_Button)
        spacerItem = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.new_std_Button_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.new_std_Button_2.setFont(font)
        self.new_std_Button_2.setObjectName("new_std_Button_2")
        self.verticalLayout.addWidget(self.new_std_Button_2)
        self.new_std_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.new_std_Button.setFont(font)
        self.new_std_Button.setObjectName("new_std_Button")
        self.verticalLayout.addWidget(self.new_std_Button)
        self.add_tr_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.add_tr_Button.setFont(font)
        self.add_tr_Button.setObjectName("add_tr_Button")
        self.verticalLayout.addWidget(self.add_tr_Button)
        self.create_class_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.create_class_Button.setFont(font)
        self.create_class_Button.setObjectName("create_class_Button")
        self.verticalLayout.addWidget(self.create_class_Button)
        self.create_list_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.create_list_button.setFont(font)
        self.create_list_button.setObjectName("create_list_button")
        self.verticalLayout.addWidget(self.create_list_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.rmv_std_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.rmv_std_Button.setFont(font)
        self.rmv_std_Button.setObjectName("rmv_std_Button")
        self.verticalLayout.addWidget(self.rmv_std_Button)
        self.rmv_tr_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.rmv_tr_Button.setFont(font)
        self.rmv_tr_Button.setObjectName("rmv_tr_Button")
        self.verticalLayout.addWidget(self.rmv_tr_Button)
        self.delete_class_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.delete_class_Button.setFont(font)
        self.delete_class_Button.setObjectName("delete_class_Button")
        self.verticalLayout.addWidget(self.delete_class_Button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.exit_Button_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.exit_Button_2.setFont(font)
        self.exit_Button_2.setObjectName("exit_Button_2")
        self.verticalLayout.addWidget(self.exit_Button_2)
        self.exit_button = QtWidgets.QPushButton(self.verticalLayoutWidget, clicked=lambda: self.iexit())
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout.addWidget(self.exit_button)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(170, 70, 791, 451))
        self.tableWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(181, 181, 181))
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
        font.setKerning(True)
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
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(560, 0, 381, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.term_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2, clicked = lambda: self.set_term())
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.term_button.setFont(font)
        self.term_button.setObjectName("term_button")
        self.horizontalLayout_2.addWidget(self.term_button)
        self.term_combo_box = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.term_combo_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.term_combo_box.setObjectName("term_combo_box")
        self.term_combo_box.addItem("", 1)
        self.term_combo_box.addItem("", 2)
        self.term_combo_box.addItem("", 3)
        self.horizontalLayout_2.addWidget(self.term_combo_box)
        self.year_combo = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.year_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.year_combo.setObjectName("year_combo")
        self.year_combo.addItem("")
        self.year_combo.addItem("")
        self.year_combo.addItem("")
        self.horizontalLayout_2.addWidget(self.year_combo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 969, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuManage_Accounts = QtWidgets.QMenu(self.menu_File)
        self.menuManage_Accounts.setObjectName("menuManage_Accounts")
        self.menuManage_Classrooms = QtWidgets.QMenu(self.menu_File)
        self.menuManage_Classrooms.setObjectName("menuManage_Classrooms")
        self.menuSchool_Term = QtWidgets.QMenu(self.menubar)
        self.menuSchool_Term.setObjectName("menuSchool_Term")
        self.menuOther = QtWidgets.QMenu(self.menubar)
        self.menuOther.setObjectName("menuOther")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Close = QtWidgets.QAction(MainWindow)
        self.action_Close.triggered.connect(self.iexit)
        self.action_Close.setObjectName("action_Close")
        self.actionAdd_user = QtWidgets.QAction(MainWindow)
        self.actionAdd_user.setObjectName("actionAdd_user")
        self.actionTerm_1 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.actionTerm_1.setFont(font)
        self.actionTerm_1.setObjectName("actionTerm_1")
        self.actionTerm_2 = QtWidgets.QAction(MainWindow)
        self.actionTerm_2.setObjectName("actionTerm_2")
        self.actionTerm_3 = QtWidgets.QAction(MainWindow)
        self.actionTerm_3.setObjectName("actionTerm_3")
        self.actionAdd = QtWidgets.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionRemove = QtWidgets.QAction(MainWindow)
        self.actionRemove.setObjectName("actionRemove")
        self.actionAdd_Student = QtWidgets.QAction(MainWindow)
        self.actionAdd_Student.setObjectName("actionAdd_Student")
        self.actionRemove_Student = QtWidgets.QAction(MainWindow)
        self.actionRemove_Student.setObjectName("actionRemove_Student")
        self.actionAdd_Teacher_s = QtWidgets.QAction(MainWindow)
        self.actionAdd_Teacher_s.setObjectName("actionAdd_Teacher_s")
        self.actionDisplay = QtWidgets.QAction(MainWindow)
        self.actionDisplay.setObjectName("actionDisplay")
        self.actionCreate_New_Class = QtWidgets.QAction(MainWindow)
        self.actionCreate_New_Class.setObjectName("actionCreate_New_Class")
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.setObjectName("actionLogout")
        self.actionGeneratesports_house_list = QtWidgets.QAction(MainWindow)
        self.actionGeneratesports_house_list.setObjectName("actionGeneratesports_house_list")
        self.actionCreate_sports_houses = QtWidgets.QAction(MainWindow)
        self.actionCreate_sports_houses.setObjectName("actionCreate_sports_houses")
        self.actionChange_password = QtWidgets.QAction(MainWindow)
        self.actionChange_password.setObjectName("actionChange_password")
        self.actionBackup_database = QtWidgets.QAction(MainWindow)
        self.actionBackup_database.setObjectName("actionBackup_database")
        self.menuManage_Accounts.addAction(self.actionAdd)
        self.menuManage_Accounts.addSeparator()
        self.menuManage_Accounts.addAction(self.actionUpdate)
        self.menuManage_Accounts.addSeparator()
        self.menuManage_Accounts.addAction(self.actionRemove)
        self.menuManage_Accounts.addSeparator()
        self.menuManage_Classrooms.addAction(self.actionCreate_New_Class)
        self.menuManage_Classrooms.addSeparator()
        self.menuManage_Classrooms.addAction(self.actionAdd_Student)
        self.menuManage_Classrooms.addSeparator()
        self.menuManage_Classrooms.addAction(self.actionAdd_Teacher_s)
        self.menuManage_Classrooms.addSeparator()
        self.menuManage_Classrooms.addAction(self.actionDisplay)
        self.menuManage_Classrooms.addSeparator()
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.menuManage_Accounts.menuAction())
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.menuManage_Classrooms.menuAction())
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionAdd_user)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionLogout)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionChange_password)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Close)
        self.menuSchool_Term.addAction(self.actionTerm_1)
        self.menuSchool_Term.addSeparator()
        self.menuSchool_Term.addAction(self.actionTerm_2)
        self.menuSchool_Term.addSeparator()
        self.menuSchool_Term.addAction(self.actionTerm_3)
        self.menuSchool_Term.addSeparator()
        self.menuOther.addAction(self.actionCreate_sports_houses)
        self.menuOther.addSeparator()
        self.menuOther.addAction(self.actionGeneratesports_house_list)
        self.menuOther.addSeparator()
        self.menuOther.addAction(self.actionBackup_database)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuSchool_Term.menuAction())
        self.menubar.addAction(self.menuOther.menuAction())

        # call functions by defualt
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.set_term()
        self.load_data()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Management System"))
        self.label_Term.setText(_translate("MainWindow", "Term: "))
        self.display_all_Button.setText(_translate("MainWindow", "Display All"))
        self.dsp_owe_Button.setStyleSheet(_translate("MainWindow", "background-color: rgb(125, 205, 127);\n"
"selection-background-color: rgb(255, 255, 255);"))
        self.dsp_owe_Button.setText(_translate("MainWindow", "Display Owing"))
        self.dsp_full_Button.setStyleSheet(_translate("MainWindow", "background-color: rgb(125, 205, 127);\n"
"selection-background-color: rgb(255, 255, 255);"))
        self.dsp_full_Button.setText(_translate("MainWindow", "Display Fully paid"))
        self.new_std_Button_2.setStyleSheet(_translate("MainWindow", "background-color: rgb(125, 205, 127);\n"
"selection-background-color: rgb(255, 255, 255);"))
        self.new_std_Button_2.setText(_translate("MainWindow", "Upload list of students"))
        self.new_std_Button.setStyleSheet(_translate("MainWindow", "background-color: rgb(125, 205, 127);\n"
"selection-background-color: rgb(255, 255, 255);"))
        self.new_std_Button.setText(_translate("MainWindow", "Add New student"))
        self.add_tr_Button.setStyleSheet(_translate("MainWindow", "background-color: rgb(125, 205, 127);\n"
"selection-background-color: rgb(255, 255, 255);"))
        self.add_tr_Button.setText(_translate("MainWindow", "Add Teacher(s)"))
        self.create_class_Button.setStyleSheet(_translate("MainWindow", "background-color: rgb(125, 205, 127);\n"
"selection-background-color: rgb(255, 255, 255);"))
        self.create_class_Button.setText(_translate("MainWindow", "Create Class"))
        self.create_list_button.setStyleSheet(_translate("MainWindow", "background-color: rgb(125, 205, 127);\n"
"selection-background-color: rgb(255, 255, 255);"))
        self.create_list_button.setText(_translate("MainWindow", "Create A Class List"))
        self.rmv_std_Button.setStyleSheet(_translate("MainWindow", "background-color: rgb(125, 205, 127);\n"
"selection-background-color: rgb(255, 255, 255);"))
        self.rmv_std_Button.setText(_translate("MainWindow", "Remove Student"))
        self.rmv_tr_Button.setStyleSheet(_translate("MainWindow", "background-color: rgb(125, 205, 127);\n"
"selection-background-color: rgb(255, 255, 255);"))
        self.rmv_tr_Button.setText(_translate("MainWindow", "Remove Teachers"))
        self.delete_class_Button.setStyleSheet(_translate("MainWindow", "background-color: rgb(125, 205, 127);\n"
"selection-background-color: rgb(255, 255, 255);"))
        self.delete_class_Button.setText(_translate("MainWindow", "Delete Class"))
        self.exit_Button_2.setStyleSheet(_translate("MainWindow", "background-color: rgb(125, 205, 127);\n"
"selection-background-color: rgb(255, 255, 255);"))
        self.exit_Button_2.setText(_translate("MainWindow", "Log out"))
        self.exit_button.setStyleSheet(_translate("MainWindow", "background-color: rgb(125, 205, 127);\n"
"selection-background-color: rgb(255, 255, 255);"))
        self.exit_button.setText(_translate("MainWindow", "Close"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Std ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Firstname"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Surname"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "DoB"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Class"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Address"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Mobile"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Account status"))
        self.term_button.setText(_translate("MainWindow", "Select Term/Year"))
        self.term_combo_box.setItemText(0, _translate("MainWindow", "Term 1"))
        self.term_combo_box.setItemText(1, _translate("MainWindow", "Term 2"))
        self.term_combo_box.setItemText(2, _translate("MainWindow", "Term 3"))
        self.year_combo.setItemText(0, _translate("MainWindow", "2021"))
        self.year_combo.setItemText(1, _translate("MainWindow", "2022"))
        self.year_combo.setItemText(2, _translate("MainWindow", "2023"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menuManage_Accounts.setTitle(_translate("MainWindow", "Manage Accounts"))
        self.menuManage_Classrooms.setTitle(_translate("MainWindow", "Manage Classrooms"))
        self.menuSchool_Term.setTitle(_translate("MainWindow", "School Term"))
        self.menuOther.setTitle(_translate("MainWindow", "Other"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_Close.setText(_translate("MainWindow", "Exit"))
        self.actionAdd_user.setText(_translate("MainWindow", "Add user"))
        self.actionTerm_1.setText(_translate("MainWindow", "Term 1"))
        self.actionTerm_2.setText(_translate("MainWindow", "Term 2"))
        self.actionTerm_3.setText(_translate("MainWindow", "Term 3"))
        self.actionAdd.setText(_translate("MainWindow", "Add"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionRemove.setText(_translate("MainWindow", "Remove"))
        self.actionAdd_Student.setText(_translate("MainWindow", "Add/Remove Student(s)"))
        self.actionRemove_Student.setText(_translate("MainWindow", "Remove Student"))
        self.actionAdd_Teacher_s.setText(_translate("MainWindow", "Add/Remove Teacher(s)"))
        self.actionDisplay.setText(_translate("MainWindow", "Display"))
        self.actionCreate_New_Class.setText(_translate("MainWindow", "Create/Remove Class"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))
        self.actionGeneratesports_house_list.setText(_translate("MainWindow", "Generate a sports house list"))
        self.actionCreate_sports_houses.setText(_translate("MainWindow", "Create sports houses"))
        self.actionChange_password.setText(_translate("MainWindow", "Change password"))
        self.actionBackup_database.setText(_translate("MainWindow", "Backup database"))



    #=================================== Functions=========================================================

    # Change label to set schoolterm and year
    def set_term(self):
        try:
            self.label_Term.setText(f'Term: {self.term_combo_box.currentData()} {self.year_combo.currentText()}')
        except Exception:
            print("Something went wrong")

    def iexit(self):
        try:
            # create message box
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Confirm database exit!")
            msg.setText("Are you sure you want to exit?")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            res = msg.exec_()
        # close the main window
            if res == QMessageBox.Ok:
                time.sleep(3)
                sys.exit()
        except(AttributeError) as e:
            print("Something went wrong")
            print(e)
        except Exception as p:
            print("Error")
            print(p)
    def load_data(self):
        try:
            students = [{"std_id": "1253","firstname":"Bupe","surname":"Sanane","Dob":"12/04/2014","Gender":"female","class":'3',"address":"garnatone","mobile":"26096965230"},
            {"std_id": "1254","firstname":"Wane","surname":"Sanane","Dob":"12/04/2016","Gender":"male","class":"reception","address":"garnatone","mobile":"26096965230"}]
            row = 0
            self.tableWidget.setRowCount(len(students))
            for std in students:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(std["std_id"]))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(std["firstname"]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(std["surname"]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(std["Dob"]))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(std["Gender"]))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(std["class"]))
                self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(std["address"]))
                self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(std["mobile"]))
                row+=1
        except Exception as e:
            print("Something went wrong")
            print(e)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())