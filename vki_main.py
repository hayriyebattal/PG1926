from vki_arayuz import Ui_Form as Arayuz_ui
import sys
from PyQt5 import QtWidgets

class Arayuz_main(QtWidgets.QWidget,Arayuz_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hesapla.clicked.connect(self.hesap)

    def hesap(self):
        kilo = float(self.kilo_bilgisi.text())
        boy = float(self.boy_bilgisi.text())
        vki = kilo / ((boy / 100) ** 2)
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

if __name__=="__main__":
    uygulama= QtWidgets.QApplication(sys.argv)
    ekran= Arayuz_main()
    ekran.show()
    sys.exit(uygulama.exec_())