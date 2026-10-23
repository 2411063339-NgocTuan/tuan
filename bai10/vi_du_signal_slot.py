import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

class ViDuSignalSlot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vi du Signal Slot")
        self.resize(300, 180)
        
        self.o_nhap = QLineEdit()
        nut_hien_thi = QPushButton("Hien thi noi dung")
        self.nhan_ket_qua = QLabel("Chua co noi dung")
        
        layout = QVBoxLayout()
        layout.addWidget(self.o_nhap)
        layout.addWidget(nut_hien_thi)
        layout.addWidget(self.nhan_ket_qua)
        self.setLayout(layout)
        nut_hien_thi.clicked.connect(self.hien_thi_noi_dung)

    def hien_thi_noi_dung(self):
        noi_dung = self.o_nhap.text()
        self.nhan_ket_qua.setText(f"Ban vua nhap: {noi_dung}")

app = QApplication(sys.argv)
cua_so = ViDuSignalSlot()
cua_so.show()
sys.exit(app.exec_())