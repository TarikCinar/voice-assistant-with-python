# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\e-posta.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_E(object):
    def setupUi_E(self, Form):
        Form.setObjectName("Form")
        Form.resize(490, 390)
        Form.setMinimumSize(QtCore.QSize(490, 390))
        Form.setMaximumSize(QtCore.QSize(490, 390))
        Form.setStyleSheet("background-color: rgb(40,40,211);")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 451, 311))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(20, 0, 10, 20)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"background-color: rgb(40,40,211);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.kimeLabel = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.kimeLabel.setFont(font)
        self.kimeLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.kimeLabel.setObjectName("kimeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.kimeLabel)
        self.basik = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.basik.setFont(font)
        self.basik.setStyleSheet("background-color: rgb(40,40,211);\n"
"color: rgb(255, 255, 255);")
        self.basik.setObjectName("basik")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.basik)
        self.baslikLabel = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.baslikLabel.setFont(font)
        self.baslikLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.baslikLabel.setObjectName("baslikLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.baslikLabel)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(40,40,211);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.konuLabel = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.konuLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.konuLabel.setObjectName("konuLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.konuLabel)
        self.gonder_button = QtWidgets.QPushButton(Form)
        self.gonder_button.setGeometry(QtCore.QRect(380, 350, 75, 23))
        self.gonder_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gonder_button.setObjectName("gonder_button")
        self.iptal_button = QtWidgets.QPushButton(Form)
        self.iptal_button.setGeometry(QtCore.QRect(290, 350, 75, 23))
        self.iptal_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.iptal_button.setObjectName("iptal_button")
        self.uyari = QtWidgets.QLabel(Form)
        self.uyari.setGeometry(QtCore.QRect(10, 350, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.uyari.setFont(font)
        self.uyari.setStyleSheet("color:rgb(255, 0, 0);")
        self.uyari.setText("")
        self.uyari.setObjectName("uyari")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "e-posta"))
        self.label.setText(_translate("Form", "Kime"))
        self.basik.setText(_translate("Form", "Başlık"))
        self.label_2.setText(_translate("Form", "Konu"))
        self.gonder_button.setText(_translate("Form", "gönder"))
        self.iptal_button.setText(_translate("Form", "iptal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_E()
    ui.setupUi_E(Form)
    Form.show()
    sys.exit(app.exec_())
