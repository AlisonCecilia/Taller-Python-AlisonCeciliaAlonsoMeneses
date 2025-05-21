import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from PyQt5 import uic

class ventana(QMainWindow):
    def __init__(self,texto):
        super().__init__()
        uic.loadUi("pantalla1.ui",self)
        self.btnNombre.clicked.connect(self.imprimirMensaje)
        self.texto=texto

    def imprimirMensaje(self):
        self.txtValor.setText(self.texto)

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    miventanita=ventana("Hola Mundo")
    miventanita.show()
    sys.exit(app.exec_())