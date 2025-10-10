import (QtWidgets,  QVBoxLayout, QLineEdit,  QRadioButton, QPushButton,  QMessageBox, QLabel )
from PyQt6W

import _tkinter as tk
from tkinter import ttk

class Calculadora():
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora con PyQt6")

        # Layout principal
        layout = QVBoxLayout()

        # Cajas de texto
        self.txt_num1 = QLineEdit()
        self.txt_num1.setPlaceholderText("Ingrese el primer número")
        self.txt_num2 = QLineEdit()
        self.txt_num2.setPlaceholderText("Ingrese el segundo número")
        layout.addWidget(self.txt_num1)
        layout.addWidget(self.txt_num2)

        # RadioButtons
        self.radio_suma = QRadioButton("Suma (+)")
        self.radio_resta = QRadioButton("Resta (-)")
        self.radio_mult = QRadioButton("Multiplicación (*)")
        self.radio_div = QRadioButton("División (/)")
        layout.addWidget(self.radio_suma)
        layout.addWidget(self.radio_resta)
        layout.addWidget(self.radio_mult)
        layout.addWidget(self.radio_div)

        # Etiqueta de resultado
        self.lbl_resultado = QLabel("Resultado: ")
        layout.addWidget(self.lbl_resultado)

        # Botones
        botones_layout = QHBoxLayout()
        self.btn_ejecutar = QPushButton("Ejecutar")
        self.btn_salir = QPushButton("Salir")
        botones_layout.addWidget(self.btn_ejecutar)
        botones_layout.addWidget(self.btn_salir)
        layout.addLayout(botones_layout)

        # Conectar eventos
        self.btn_ejecutar.clicked.connect(self.calcular)
        self.btn_salir.clicked.connect(self.close)

        self.setLayout(layout)

    def calcular(self):
        try:
            num1 = float(self.txt_num1.text())
            num2 = float(self.txt_num2.text())

            if self.radio_suma.isChecked():
                resultado = num1 + num2
            elif self.radio_resta.isChecked():
                resultado = num1 - num2
            elif self.radio_mult.isChecked():
                resultado = num1 * num2
            elif self.radio_div.isChecked():
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    QMessageBox.warning(self, "Error", "No se puede dividir entre 0")
                    return
            else:
                QMessageBox.warning(self, "Error", "Seleccione una operación")
                return



            self.lbl_resultado.setText(f"Resultado: {resultado}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese números válidos")