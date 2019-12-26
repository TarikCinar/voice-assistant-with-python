# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayuz.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.setWindowModality(QtCore.Qt.NonModal)
        widget.resize(400, 550)
        widget.setMinimumSize(QtCore.QSize(400, 550))
        widget.setMaximumSize(QtCore.QSize(400, 550))
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(40, 40, 211))
        gradient.setColorAt(1.0, QtGui.QColor(99, 136, 153))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(40, 40, 211))
        gradient.setColorAt(1.0, QtGui.QColor(99, 136, 153))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(40, 40, 211))
        gradient.setColorAt(1.0, QtGui.QColor(99, 136, 153))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(40, 40, 211))
        gradient.setColorAt(1.0, QtGui.QColor(99, 136, 153))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(40, 40, 211))
        gradient.setColorAt(1.0, QtGui.QColor(99, 136, 153))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(40, 40, 211))
        gradient.setColorAt(1.0, QtGui.QColor(99, 136, 153))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(40, 40, 211))
        gradient.setColorAt(1.0, QtGui.QColor(99, 136, 153))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(40, 40, 211))
        gradient.setColorAt(1.0, QtGui.QColor(99, 136, 153))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(40, 40, 211))
        gradient.setColorAt(1.0, QtGui.QColor(99, 136, 153))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        widget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setBold(True)
        font.setWeight(75)
        widget.setFont(font)
        widget.setFocusPolicy(QtCore.Qt.NoFocus)
        widget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        widget.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/widgedİcon/yeni_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        widget.setWindowIcon(icon)
        widget.setAutoFillBackground(False)
        widget.setStyleSheet("#widget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(40,40,211) , stop:1 rgb(99,136,153) );\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.ses_butonu = QtWidgets.QPushButton(widget)
        self.ses_butonu.setGeometry(QtCore.QRect(150, 470, 91, 71))
        self.ses_butonu.setStyleSheet("#ses_butonu{\n"
"border-image: url(:/icon_bas/icon_bas.ico);\n"
"}\n"
"#ses_butonu:pressed{\n"
"   \n"
"    border-image: url(:/icon_dur/icon_dur.ico);\n"
"\n"
"   }\n"
"")
        self.ses_butonu.setText("")
        self.ses_butonu.setObjectName("ses_butonu")
        self.lineEdit = QtWidgets.QLineEdit(widget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 420, 381, 41))
        self.lineEdit.setStyleSheet("#lineEdit{\n"
"border-radius:20px;\n"
"padding-right:40px;\n"
"padding-left:10px;\n"
"font: 75 15pt \"Consolas\";\n"
"}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.text_b = QtWidgets.QTextBrowser(widget)
        self.text_b.setGeometry(QtCore.QRect(10, 90, 381, 301))
        self.text_b.setAcceptDrops(False)
        self.text_b.setStyleSheet("#text_b{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(40,40,211) , stop:1 rgb(99,136,153) );\n"
"padding-left:30px;\n"
"font: 75 12pt \"Consolas\";\n"
"border-radius:10px;\n"
"\n"
"\n"
"}")
        self.text_b.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_b.setObjectName("text_b")
        self.close = QtWidgets.QPushButton(widget)
        self.close.setGeometry(QtCore.QRect(350, 10, 45, 25))
        self.close.setStyleSheet("#close:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}")
        self.close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/close.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon1)
        self.close.setFlat(True)
        self.close.setObjectName("close")
        self.minus = QtWidgets.QPushButton(widget)
        self.minus.setGeometry(QtCore.QRect(310, 10, 45, 25))
        self.minus.setStyleSheet("#minus:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.minus.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/minus.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minus.setIcon(icon2)
        self.minus.setFlat(True)
        self.minus.setObjectName("minus")
        self.asistan = QtWidgets.QPushButton(widget)
        self.asistan.setGeometry(QtCore.QRect(10, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.asistan.setFont(font)
        self.asistan.setToolTip("")
        self.asistan.setStyleSheet("#asistan{\n"
"color:rgb(255,255,255);\n"
"background-color: rgb(38, 49, 112);\n"
"    border-top-color: rgb(38, 49, 112);\n"
"}")
        self.asistan.setIcon(icon)
        self.asistan.setIconSize(QtCore.QSize(30, 30))
        self.asistan.setAutoDefault(False)
        self.asistan.setDefault(False)
        self.asistan.setFlat(True)
        self.asistan.setObjectName("asistan")
        self.gonder = QtWidgets.QPushButton(widget)
        self.gonder.setGeometry(QtCore.QRect(350, 420, 41, 41))
        self.gonder.setStyleSheet("#gonder{\n"
"border-image: url(:/newPrefix/gonder.ico);\n"
"}\n"
"\n"
"#gonder:pressed{\n"
"border-image: url(:/newPrefix/gonder_bas.ico);\n"
"}\n"
"")
        self.gonder.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/send/gonder.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gonder.setIcon(icon3)
        self.gonder.setIconSize(QtCore.QSize(60, 60))
        self.gonder.setAutoDefault(False)
        self.gonder.setDefault(False)
        self.gonder.setFlat(False)
        self.gonder.setObjectName("gonder")

        self.retranslateUi(widget)
        self.ses_butonu.clicked.connect(widget.dinle)
        self.close.clicked.connect(widget.kapat)
        self.minus.clicked.connect(widget.kucult)
        self.asistan.clicked.connect(widget.help)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Asistan"))
        self.text_b.setHtml(_translate("widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:12pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.close.setToolTip(_translate("widget", "kapat"))
        self.minus.setToolTip(_translate("widget", "küçült"))
        self.asistan.setText(_translate("widget", "Asistan"))
import close_rc
import gonderPress_rc
import gonder_rc
import icon_bas_rc
import icon_dur_rc
import icon_rc
import minus_rc
import resim_rc
import widget_icon_rc
