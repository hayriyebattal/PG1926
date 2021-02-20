# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vki_arayuzz.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(413, 389)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 60, 261, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.boyCmLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.boyCmLabel.setFont(font)
        self.boyCmLabel.setObjectName("boyCmLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.boyCmLabel)
        self.boy_bilgisi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.boy_bilgisi.setObjectName("boy_bilgisi")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.boy_bilgisi)
        self.kiloKgLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.kiloKgLabel.setFont(font)
        self.kiloKgLabel.setObjectName("kiloKgLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.kiloKgLabel)
        self.hesapla = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hesapla.setFont(font)
        self.hesapla.setObjectName("hesapla")
        self.hesapla.clicked.connect(self.hesap)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.hesapla)
        self.kilo_bilgisi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.kilo_bilgisi.setObjectName("kilo_bilgisi")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.kilo_bilgisi)
        self.degerlendirme = QtWidgets.QTextBrowser(Form)
        self.degerlendirme.setGeometry(QtCore.QRect(10, 250, 401, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.degerlendirme.setFont(font)
        self.degerlendirme.setObjectName("degerlendirme")
        self.durum = QtWidgets.QTextBrowser(Form)
        self.durum.setGeometry(QtCore.QRect(190, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.durum.setFont(font)
        self.durum.setObjectName("durum")
        self.sonuc = QtWidgets.QTextBrowser(Form)
        self.sonuc.setGeometry(QtCore.QRect(110, 200, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sonuc.setFont(font)
        self.sonuc.setObjectName("sonuc")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 20, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Vücut Kitle İndeksi"))
        self.boyCmLabel.setText(_translate("Form", "Boy(cm):"))
        self.kiloKgLabel.setText(_translate("Form", "Kilo(kg):"))
        self.hesapla.setText(_translate("Form", "Hesapla"))
        self.degerlendirme.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.durum.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.sonuc.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Form", "Vücut Kitle İndeksi Hesaplama"))

    def hesap(self):
        kilo=float(self.kilo_bilgisi.text())
        boy=float(self.boy_bilgisi.text())
        vki=kilo/((boy/100)**2)
        self.sonuc.setText(str(vki.__round__(1)))

        if vki < 18:
            self.durum.setText(str("Zayıf"))
            self.degerlendirme.setText(str("Boyunuza göre uygun ağırlıkta olmadığınızı, zayıf olduğunuzu gösterir. Zayıflık, bazı hastalıklar için risk oluşturan ve istenmeyen bir durumdur. Boyunuza uygun ağırlığa erişmeniz için yeterli ve dengeli beslenmeli, beslenme alışkanlıklarınızı geliştirmeye özen göstermelisiniz."))
        elif vki >= 18 and vki < 25:
            self.durum.setText(str("Normal"))
            self.degerlendirme.setText(str("Boyunuza göre uygun ağırlıkta olduğunuzu gösterir. Yeterli ve dengeli beslenerek ve düzenli fiziksel aktivite yaparak bu ağırlığınızı korumaya özen gösteriniz."))
        elif vki >= 25 and vki < 30:
            self.durum.setText(str("Kilolu"))
            self.degerlendirme.setText(str("Boyunuza göre vücut ağırlığınızın fazla olduğunu gösterir. Fazla kilolu olma durumu gerekli önlemler alınmadığı takdirde pek çok hastalık için risk faktörü olan obeziteye (şişmanlık) yol açar."))
        elif vki >= 30 and vki < 35:
            self.durum.setText(str("Obez Riski"))
            self.degerlendirme.setText(str("Boyunuza göre vücut ağırlığınızın fazla olduğunun, bir başka deyişle şişman olduğunuzun bir göstergesidir. Şişmanlık, kalp-damar hastalıkları, diyabet, hipertansiyon v.b. kronik hastalıklar için risk faktörüdür. Bir sağlık kuruluşuna başvurarak hekim / diyetisyen kontrolünde zayıflayarak normal ağırlığa ulaşmanız sağlığınız açısından çok önemlidir."))
        else:
            self.durum.setText(str("Ciddi Obez Riski"))
            self.degerlendirme.setText(str("Boyunuza göre vücut ağırlığınızın fazla olduğunun, bir başka deyişle şişman olduğunuzun bir göstergesidir. Şişmanlık, kalp-damar hastalıkları, diyabet, hipertansiyon v.b. kronik hastalıklar için risk faktörüdür. Bir sağlık kuruluşuna başvurarak hekim / diyetisyen kontrolünde zayıflayarak normal ağırlığa ulaşmanız sağlığınız açısından çok önemlidir."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

