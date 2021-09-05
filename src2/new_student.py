# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_student.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog, QMessageBox
import studentdb as db
import sqlite3

STUDENT_DB = "student.db"

CLASSES = []
conn = sqlite3.connect(STUDENT_DB)
c = conn.cursor()
c.execute("SELECT grade FROM classes")
data = c.fetchall()

for i in data:
    CLASSES.append(i)


class Ui_AddStudentForm(QDialog):
    def setupUi(self, AddStudentForm):
        AddStudentForm.setObjectName("AddStudentForm")
        AddStudentForm.resize(862, 354)
        AddStudentForm.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.std_entry_form = QtWidgets.QGroupBox(AddStudentForm)
        self.std_entry_form.setGeometry(QtCore.QRect(0, 0, 441, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.std_entry_form.setFont(font)
        self.std_entry_form.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.std_entry_form.setObjectName("std_entry_form")
        self.formLayoutWidget = QtWidgets.QWidget(self.std_entry_form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 50, 361, 181))
        self.formLayoutWidget.setStyleSheet("background-color: rgb(119, 171, 255);")
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
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.surname = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.surname.setFont(font)
        self.surname.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.surname.setObjectName("surname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.surname)
        self.surname_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.surname_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.surname_input.setObjectName("surname_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.surname_input)
        self.DoB = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DoB.setFont(font)
        self.DoB.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.DoB.setObjectName("DoB")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.DoB)
        self.dob_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.dob_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dob_input.setObjectName("dob_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dob_input)
        self.gender = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gender.setFont(font)
        self.gender.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.gender.setObjectName("gender")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.gender)
        self.gender_combo = QtWidgets.QComboBox(self.formLayoutWidget)
        self.gender_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gender_combo.setObjectName("gender_combo")
        self.gender_combo.addItem('', 'female')
        self.gender_combo.addItem('', 'male')
        self.gender_combo.addItem('', 'other')
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.gender_combo)
        self.address = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.address.setFont(font)
        self.address.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.address.setObjectName("address")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.address)
        self.address_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.address_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.address_input.setObjectName("address_input")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.address_input)
        self.assign_class = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.assign_class.setFont(font)
        self.assign_class.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.assign_class.setObjectName("assign_class")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.assign_class)
        self.assign_class_combo = QtWidgets.QComboBox(self.formLayoutWidget)
        self.assign_class_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.assign_class_combo.setObjectName("assign_class_combo")
        self.assign_class_combo.addItem('', CLASSES[0][0])
        self.assign_class_combo.addItem('', CLASSES[1][0])
        self.assign_class_combo.addItem('', CLASSES[2][0])
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.assign_class_combo)
        self.prt_enrty_form = QtWidgets.QGroupBox(AddStudentForm)
        self.prt_enrty_form.setGeometry(QtCore.QRect(450, 0, 411, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.prt_enrty_form.setFont(font)
        self.prt_enrty_form.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.prt_enrty_form.setObjectName("prt_enrty_form")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.prt_enrty_form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 351, 181))
        self.formLayoutWidget_2.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.parent_title = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.parent_title.setFont(font)
        self.parent_title.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.parent_title.setObjectName("parent_title")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.parent_title)
        self.parent_name = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.parent_name.setFont(font)
        self.parent_name.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.parent_name.setObjectName("parent_name")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.parent_name)
        self.prt_names_input = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.prt_names_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.prt_names_input.setObjectName("prt_names_input")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.prt_names_input)
        self.phone_home = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.phone_home.setFont(font)
        self.phone_home.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.phone_home.setObjectName("phone_home")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.phone_home)
        self.tel_home_input = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.tel_home_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tel_home_input.setObjectName("tel_home_input")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tel_home_input)
        self.phone_work = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.phone_work.setFont(font)
        self.phone_work.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.phone_work.setObjectName("phone_work")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.phone_work)
        self.parent_email = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.parent_email.setFont(font)
        self.parent_email.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.parent_email.setObjectName("parent_email")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.parent_email)
        self.parent_relation = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.parent_relation.setFont(font)
        self.parent_relation.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.parent_relation.setObjectName("parent_relation")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.parent_relation)
        self.relation_input = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.relation_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.relation_input.setObjectName("relation_input")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.relation_input)
        self.prt_title_combo = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.prt_title_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.prt_title_combo.setObjectName("prt_title_combo")
        self.prt_title_combo.addItem('', "Mr.")
        self.prt_title_combo.addItem('', "Mrs.")
        self.prt_title_combo.addItem('', "Dr.")
        self.prt_title_combo.addItem('', "Other.")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.prt_title_combo)
        self.email_input = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.email_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.email_input.setObjectName("email_input")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.email_input)
        self.tel_work_input = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.tel_work_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tel_work_input.setObjectName("tel_work_input")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tel_work_input)
        self.frame = QtWidgets.QFrame(AddStudentForm)
        self.frame.setGeometry(QtCore.QRect(130, 260, 621, 80))
        self.frame.setStyleSheet("background-color: rgb(119, 171, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, -30, 571, 152))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.upload_csv_button = QtWidgets.QPushButton(self.horizontalLayoutWidget,
                                                       clicked=lambda: self.open_csv_file())
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.upload_csv_button.setFont(font)
        self.upload_csv_button.setStyleSheet("background-color: rgb(125, 205, 127);")
        self.upload_csv_button.setObjectName("upload_csv_button")
        self.horizontalLayout.addWidget(self.upload_csv_button)
        self.add_std_button = QtWidgets.QPushButton(self.horizontalLayoutWidget,
                                                    clicked=lambda: self.add_student_info())
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.add_std_button.setFont(font)
        self.add_std_button.setStyleSheet("background-color: rgb(125, 205, 127);")
        self.add_std_button.setObjectName("add_std_button")
        self.horizontalLayout.addWidget(self.add_std_button)
        self.reset_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.reset_button.setFont(font)
        self.reset_button.setStyleSheet("background-color: rgb(125, 205, 127);")
        self.reset_button.setObjectName("reset_button")
        self.horizontalLayout.addWidget(self.reset_button)
        self.preview_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.preview_button.setFont(font)
        self.preview_button.setStyleSheet("background-color: rgb(125, 205, 127);")
        self.preview_button.setObjectName("preview_button")
        self.horizontalLayout.addWidget(self.preview_button)

        self.retranslateUi(AddStudentForm)
        QtCore.QMetaObject.connectSlotsByName(AddStudentForm)

    def retranslateUi(self, AddStudentForm):
        _translate = QtCore.QCoreApplication.translate
        AddStudentForm.setWindowTitle(_translate("AddStudentForm", "Add Student"))
        self.std_entry_form.setTitle(_translate("AddStudentForm", "Manage student info"))
        self.label.setText(_translate("AddStudentForm", "First name:"))
        self.surname.setText(_translate("AddStudentForm", "Surname:"))
        self.DoB.setText(_translate("AddStudentForm", "DoB:"))
        self.gender.setText(_translate("AddStudentForm", "Gender:"))
        self.address.setText(_translate("AddStudentForm", "Address:"))
        self.assign_class.setText(_translate("AddStudentForm", "Assign class:"))
        self.prt_enrty_form.setTitle(_translate("AddStudentForm", "Parent/Guardian details"))
        self.gender_combo.setItemText(0, _translate("AddStudentForm", "Female"))
        self.gender_combo.setItemText(1, _translate("AddStudentForm", "Male"))
        self.gender_combo.setItemText(2, _translate("AddStudentForm", "Other"))
        self.assign_class_combo.setItemText(0, _translate("AddStudentForm", CLASSES[0][0]))
        self.assign_class_combo.setItemText(1, _translate("AddStudentForm", CLASSES[1][0]))
        self.assign_class_combo.setItemText(2, _translate("AddStudentForm", CLASSES[2][0]))
        self.prt_title_combo.setItemText(0, _translate("AddStudentForm", "Mr"))
        self.prt_title_combo.setItemText(1, _translate("AddStudentForm", "Mrs"))
        self.prt_title_combo.setItemText(2, _translate("AddStudentForm", "Dr"))
        self.prt_title_combo.setItemText(3, _translate("AddStudentForm", "Other"))
        self.parent_title.setText(_translate("AddStudentForm", "Title:"))
        self.parent_name.setText(_translate("AddStudentForm", "Full names:"))
        self.phone_home.setText(_translate("AddStudentForm", "Telephone  home:"))
        self.phone_work.setText(_translate("AddStudentForm", "Telephone  Work:"))
        self.parent_email.setText(_translate("AddStudentForm", "Email:"))
        self.parent_relation.setText(_translate("AddStudentForm", "Relationship"))
        self.upload_csv_button.setText(_translate("AddStudentForm", "Upload csv"))
        self.add_std_button.setText(_translate("AddStudentForm", "Add"))
        self.reset_button.setText(_translate("AddStudentForm", "Reset"))
        self.preview_button.setText(_translate("AddStudentForm", "Preview"))

    # ================================functions
    def open_csv_file(self):
        import csv
        fields = []
        rows = []
        try:
            filename = QFileDialog.getOpenFileName(self, 'Open csv file', 'C:\\Users\\USER\\Documents',
                                                   "CSV files(*.csv)")

            with open(filename[0], 'r') as file:
                csvreader = csv.reader(file)
                fields = next(csvreader)

                print('fields:', fields)
                for std in csvreader:
                    rows.append(std)
                    print('stds:', rows[0])

        except Exception as e:
            print("something went wrong")
            print(e)

    # add single student
    def add_student_info(self):
        try:
            # select data from tables
            conn = sqlite3.connect(STUDENT_DB)
            c = conn.cursor()

            # Get parent data from input fields
            title = f"{self.prt_title_combo.currentData()}".upper()
            names = self.prt_names_input.text().upper()
            tel_home = self.tel_home_input.text()
            tel_work = self.tel_work_input.text()
            email = self.email_input.text()
            relationship = self.relation_input.text().upper()

            # Get student data from input fields
            parent_id = self.relation_input.text().upper()
            class_id = 2
            firstname = self.lineEdit.text().upper()
            surname = self.surname_input.text().upper()
            dob = self.dob_input.text().upper()
            gender = f'{self.gender_combo.currentData()}'.upper()
            address = self.address_input.text().upper()
            assign_class = f'{self.assign_class_combo.currentData()}'.upper()

            # Put data into tuples
            # Student data
            rows_student = (parent_id, class_id, firstname, surname, dob, gender, address, assign_class)
            # Parent data
            rows_parent = (title, names, tel_home, tel_work, email, relationship)

            # check whether parent already exists
            # if exists don't add to table else add parent and student to db
            c.execute("SELECT relationship FROM parents WHERE relationship=?", (relationship,))
            chk = c.fetchall()

            if len(chk) == 0:
                # write parent data to database
                db.insert_data("parent", rows_parent)
                # write student data to database
                db.insert_data("student", rows_student)

                # success message box
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Student Management System")
                msg.setText("Student data Successfully added")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            else:
                # Ask user to confirm addition of existing parent
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Student management System")
                msg.setText("This parent relation already exists\n do you want to continue?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
                res = msg.exec_()

                if res == QMessageBox.Yes:
                    # continue with adding student data
                    db.insert_data("student", rows_student)
                    # success message box
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Student Management System")
                    msg.setText("Student Successfully added")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()


        except Exception as e:
            print(e)
            print("something wrong in writing new record")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AddStudentForm = QtWidgets.QWidget()
    ui = Ui_AddStudentForm()
    ui.setupUi(AddStudentForm)
    AddStudentForm.show()
    sys.exit(app.exec_())
