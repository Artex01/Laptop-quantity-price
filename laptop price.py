import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSpinBox, QLineEdit, QLabel
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.create_spinbox()
        self.show()
    def create_spinbox(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        self.label = QLabel("Laptop price:")
        self.label2 = QLabel("Total price:")
        self.lineEdit = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.spin_selected)
        hbox.addWidget(self.label)
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.label2)
        hbox.addWidget(self.lineEdit2)
        self.setLayout(hbox)

    def spin_selected(self):
        price = int(self.lineEdit.text())
        totalPrice = self.spinbox.value() * price
        self.lineEdit2.setText(str(totalPrice))

app = QApplication(sys.argv)
window = Window()
app.exec_()