import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt

class MayTinhBoTui(QWidget):
    def __init__(self):
        super().__init__()
        self.khoi_tao_giao_dien()
    def khoi_tao_giao_dien(self):
        self.setWindowTitle("May tinh bo tui PyQt")
        self.resize(300, 400)

        # Ô hiển thị kết quả / phép tính
        self.man_hinh = QLineEdit()
        self.man_hinh.setReadOnly(True)
        self.man_hinh.setAlignment(Qt.AlignRight)
        self.man_hinh.setStyleSheet("font-size: 24px; padding: 10px;")
        nut_grid = QGridLayout()
        buttons = [
            ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2)
        ]

        for text, row, col in buttons:
            btn = QPushButton(text)
            btn.setStyleSheet("font-size: 18px; padding: 15px;")
            btn.clicked.connect(self.xu_ly_click)
            if text == '=':
                nut_grid.addWidget(btn, row, col, 1, 2)
            else:
                nut_grid.addWidget(btn, row, col)
        layout_chinh = QVBoxLayout()
        layout_chinh.addWidget(self.man_hinh)
        layout_chinh.addLayout(nut_grid)
        self.setLayout(layout_chinh)

    def xu_ly_click(self):
        sender = self.sender()
        text = sender.text()
        hien_tai = self.man_hinh.text()
        if text == 'C':
            self.man_hinh.clear()
        elif text == '=':
            try:
                ket_qua = str(eval(hien_tai))
                self.man_hinh.setText(ket_qua)
            except Exception:
                self.man_hinh.setText("Lỗi")
        else:
            self.man_hinh.setText(hien_tai + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cua_so = MayTinhBoTui()
    cua_so.show()
    sys.exit(app.exec_())