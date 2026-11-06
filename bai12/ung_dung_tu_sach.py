
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import csdl_sach as db


DANH_SACH_THE_LOAI = [
    "Ky nang song",
    "Tieu thuyet",
    "Lich su",
    "Khoa hoc",
    "Kinh te",
    "Khac"
]


class UngDungTuSach(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Quan ly Tu sach ca nhan")
        self.geometry("560x480")
        self.resizable(False, False)

        db.tao_bang_neu_chua_co()

        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach_sach()

    # =====================================
    # KHOI TAO GIAO DIEN
    # =====================================

    def khoi_tao_giao_dien(self):

        khung_nhap = tk.Frame(self)
        khung_nhap.pack(
            pady=10,
            padx=10,
            fill="x"
        )

        # Ten sach
        tk.Label(
            khung_nhap,
            text="Ten sach:"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=5
        )

        self.o_nhap_ten_sach = tk.Entry(
            khung_nhap,
            width=30
        )

        self.o_nhap_ten_sach.grid(
            row=0,
            column=1,
            padx=10,
            pady=5
        )

        # Tac gia
        tk.Label(
            khung_nhap,
            text="Tac gia:"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=5
        )

        self.o_nhap_tac_gia = tk.Entry(
            khung_nhap,
            width=30
        )

        self.o_nhap_tac_gia.grid(
            row=1,
            column=1,
            padx=10,
            pady=5
        )

        # The loai
        tk.Label(
            khung_nhap,
            text="The loai:"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=5
        )

        self.chon_the_loai = ttk.Combobox(
            khung_nhap,
            values=DANH_SACH_THE_LOAI,
            width=27,
            state="readonly"
        )

        self.chon_the_loai.current(0)

        self.chon_the_loai.grid(
            row=2,
            column=1,
            padx=10,
            pady=5
        )

        # Nut them sach
        ttk.Button(
            khung_nhap,
            text="Them sach",
            command=self.xu_ly_them_sach
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            pady=10
        )

        # =================================
        # DANH SACH SACH
        # =================================

        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(
            pady=5,
            padx=10,
            fill="both",
            expand=True
        )

        self.listbox_sach = tk.Listbox(
            khung_danh_sach,
            width=75,
            height=14,
            selectmode=tk.SINGLE,
            exportselection=False
        )

        self.listbox_sach.pack(
            side="left",
            fill="both",
            expand=True
        )

        thanh_cuon = tk.Scrollbar(
            khung_danh_sach,
            orient="vertical",
            command=self.listbox_sach.yview
        )

        thanh_cuon.pack(
            side="right",
            fill="y"
        )

        self.listbox_sach.config(
            yscrollcommand=thanh_cuon.set
        )

        # =================================
        # CAC NUT CHUC NANG
        # =================================

        khung_nut_thao_tac = tk.Frame(self)
        khung_nut_thao_tac.pack(pady=10)

        ttk.Button(
            khung_nut_thao_tac,
            text="Danh dau da doc",
            command=self.xu_ly_danh_dau_da_doc
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        ttk.Button(
            khung_nut_thao_tac,
            text="Xoa sach",
            command=self.xu_ly_xoa_sach
        ).grid(
            row=0,
            column=1,
            padx=5
        )

        ttk.Button(
            khung_nut_thao_tac,
            text="Thong ke theo the loai",
            command=self.xu_ly_thong_ke
        ).grid(
            row=0,
            column=2,
            padx=5
        )

    # =====================================
    # TAI LAI DANH SACH SACH
    # =====================================

    def tai_lai_danh_sach_sach(self):

        self.listbox_sach.delete(0, tk.END)

        self.danh_sach_hien_tai = db.lay_toan_bo_sach()

        for sach in self.danh_sach_hien_tai:

            id_sach, ten_sach, tac_gia, the_loai, da_doc = sach

            trang_thai = (
                "[Da doc]" if da_doc == 1
                else "[Chua doc]"
            )

            self.listbox_sach.insert(
                tk.END,
                f"{trang_thai} {ten_sach} - "
                f"{tac_gia} - ({the_loai})"
            )

    # =====================================
    # THEM SACH
    # =====================================

    def xu_ly_them_sach(self):

        ten_sach = self.o_nhap_ten_sach.get().strip()
        tac_gia = self.o_nhap_tac_gia.get().strip()
        the_loai = self.chon_the_loai.get()

        if ten_sach == "" or tac_gia == "":

            messagebox.showerror(
                "Loi",
                "Vui long nhap day du ten sach va tac gia."
            )
            return

        db.them_sach(
            ten_sach,
            tac_gia,
            the_loai
        )

        self.o_nhap_ten_sach.delete(0, tk.END)
        self.o_nhap_tac_gia.delete(0, tk.END)

        self.tai_lai_danh_sach_sach()

        messagebox.showinfo(
            "Thanh cong",
            f"Da them sach: {ten_sach}"
        )

    # =====================================
    # XOA SACH
    # =====================================

    def xu_ly_xoa_sach(self):

        lua_chon = self.listbox_sach.curselection()

        if not lua_chon:

            messagebox.showerror(
                "Loi",
                "Vui long chon mot cuon sach de xoa."
            )
            return

        id_sach = self.danh_sach_hien_tai[lua_chon[0]][0]

        db.xoa_sach(id_sach)

        self.tai_lai_danh_sach_sach()

    # =====================================
    # DANH DAU DA DOC
    # =====================================

    def xu_ly_danh_dau_da_doc(self):

        lua_chon = self.listbox_sach.curselection()

        if not lua_chon:

            messagebox.showerror(
                "Loi",
                "Vui long chon mot cuon sach de danh dau da doc."
            )
            return

        id_sach = self.danh_sach_hien_tai[lua_chon[0]][0]

        db.danh_dau_da_doc(id_sach)

        self.tai_lai_danh_sach_sach()


    # =====================================
    # THONG KE THEO THE LOAI
    # =====================================

    def xu_ly_thong_ke(self):

        du_lieu_thong_ke = db.thong_ke_theo_the_loai()

        if not du_lieu_thong_ke:
            messagebox.showinfo(
                "Thong bao",
                "Chua co du lieu sach de thong ke."
            )
            return

        cac_the_loai = [
            dong[0] for dong in du_lieu_thong_ke
        ]

        so_luong = [
            dong[1] for dong in du_lieu_thong_ke
        ]

        # Tao cua so bieu do
        cua_so = tk.Toplevel(self)
        cua_so.title("Thong ke theo the loai")
        cua_so.geometry("720x480")

        # Tao bieu do Matplotlib
        hinh = Figure(figsize=(7, 4), dpi=100)
        truc = hinh.add_subplot(111)

        truc.bar(
            cac_the_loai,
            so_luong,
            color="cornflowerblue"
        )

        truc.set_title("So luong sach theo the loai")
        truc.set_xlabel("The loai")
        truc.set_ylabel("So luong sach")
        truc.set_ylim(0, max(so_luong) + 1)

        hinh.tight_layout()

        # Luu anh vao thu muc chua co so du lieu
        duong_dan_anh = (
            Path(db.TEN_FILE_CSDL).parent
            / "thong_ke_the_loai.png"
        )

        hinh.savefig(duong_dan_anh, dpi=150)

        # Hien thi bieu do trong cua so Tkinter
        canvas = FigureCanvasTkAgg(
            hinh,
            master=cua_so
        )

        canvas.draw()
        canvas.get_tk_widget().pack(
            fill=tk.BOTH,
            expand=True
        )

        cua_so.canvas = canvas
        cua_so.lift()
# =====================================
# CHAY CHUONG TRINH
# =====================================

if __name__ == "__main__":
    ung_dung = UngDungTuSach()
    ung_dung.mainloop()
