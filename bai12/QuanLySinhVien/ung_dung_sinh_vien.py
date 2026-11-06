"""Do an Buoi 12: Quan ly sinh vien co giao dien Tkinter."""

import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

import csdl_sinh_vien as db


class UngDungSinhVien(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly sinh vien")
        self.geometry("890x610")
        self.minsize(760, 520)

        db.tao_bang_neu_chua_co()
        self.danh_sach_hien_tai = []
        self.ma_sv_dang_chon = None

        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach_sinh_vien()
    # -------------------------------------
    # HOAT DONG 4: GIAO DIEN
    # -------------------------------------
    def khoi_tao_giao_dien(self):
        ttk.Label(
            self, text="QUAN LY SINH VIEN", font=("Arial", 19, "bold")
        ).pack(pady=(16, 8))

        khung_nhap = ttk.LabelFrame(self, text="Thong tin sinh vien", padding=12)
        khung_nhap.pack(padx=15, pady=7, fill="x")
        khung_nhap.columnconfigure(1, weight=1)
        khung_nhap.columnconfigure(3, weight=1)

        ttk.Label(khung_nhap, text="Ma SV:").grid(row=0, column=0, sticky="w", pady=6)
        self.o_ma_sv = ttk.Entry(khung_nhap, width=22)
        self.o_ma_sv.grid(row=0, column=1, padx=(8, 18), pady=6, sticky="ew")

        ttk.Label(khung_nhap, text="Ho ten:").grid(row=0, column=2, sticky="w", pady=6)
        self.o_ho_ten = ttk.Entry(khung_nhap, width=30)
        self.o_ho_ten.grid(row=0, column=3, padx=8, pady=6, sticky="ew")

        ttk.Label(khung_nhap, text="Lop:").grid(row=1, column=0, sticky="w", pady=6)
        self.o_lop = ttk.Entry(khung_nhap, width=22)
        self.o_lop.grid(row=1, column=1, padx=(8, 18), pady=6, sticky="ew")

        ttk.Label(khung_nhap, text="Diem TB (0-10):").grid(
            row=1, column=2, sticky="w", pady=6
        )
        self.o_diem_tb = ttk.Entry(khung_nhap, width=30)
        self.o_diem_tb.grid(row=1, column=3, padx=8, pady=6, sticky="ew")

        khung_nut = ttk.Frame(self)
        khung_nut.pack(pady=8)
        ttk.Button(khung_nut, text="Them SV", command=self.xu_ly_them).grid(
            row=0, column=0, padx=5
        )
        ttk.Button(khung_nut, text="Sua SV", command=self.xu_ly_sua).grid(
            row=0, column=1, padx=5
        )
        ttk.Button(khung_nut, text="Xoa SV", command=self.xu_ly_xoa).grid(
            row=0, column=2, padx=5
        )
        ttk.Button(khung_nut, text="Lam moi", command=self.xu_ly_lam_moi).grid(
            row=0, column=3, padx=5
        )
        ttk.Button(
            khung_nut, text="Thong ke xep loai", command=self.xu_ly_thong_ke
        ).grid(row=0, column=4, padx=5)

        khung_tim = ttk.Frame(self)
        khung_tim.pack(padx=15, pady=(5, 3), fill="x")
        ttk.Label(khung_tim, text="Tim kiem (ma, ten, lop):").pack(side="left")
        self.o_tim_kiem = ttk.Entry(khung_tim)
        self.o_tim_kiem.pack(side="left", fill="x", expand=True, padx=(10, 0))
        self.o_tim_kiem.bind(
            "<KeyRelease>", lambda event: self.tai_lai_danh_sach_sinh_vien()
        )

        khung_danh_sach = ttk.LabelFrame(
            self, text="Danh sach sinh vien", padding=10
        )
        khung_danh_sach.pack(
            padx=15, pady=(8, 5), fill="both", expand=True
        )

        self.listbox_sinh_vien = tk.Listbox(
            khung_danh_sach,
            font=("Menlo", 11),
            height=12,
            selectmode=tk.SINGLE,
            exportselection=False,
        )
        self.listbox_sinh_vien.pack(side="left", fill="both", expand=True)
        self.listbox_sinh_vien.bind(
            "<<ListboxSelect>>", self.khi_chon_sinh_vien
        )

        thanh_cuon = ttk.Scrollbar(
            khung_danh_sach,
            orient="vertical",
            command=self.listbox_sinh_vien.yview,
        )
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_sinh_vien.configure(yscrollcommand=thanh_cuon.set)

        self.nhan_trang_thai = ttk.Label(self, text="", anchor="w")
        self.nhan_trang_thai.pack(padx=18, pady=(3, 10), fill="x")

    # -------------------------------------
    # LAY VA HIEN THI DU LIEU
    # -------------------------------------
    def tai_lai_danh_sach_sinh_vien(self, ma_can_chon=None):
        # Tim kiem hay tai lai moi se bo chon dong cu de tranh sua/xoa nham.
        if ma_can_chon is None:
            self.xoa_o_nhap()
        tu_khoa = self.o_tim_kiem.get().strip()
        self.danh_sach_hien_tai = db.tim_kiem_sinh_vien(tu_khoa)
        self.listbox_sinh_vien.delete(0, tk.END)

        vi_tri_can_chon = None
        for vi_tri, (ma_sv, ho_ten, lop, diem_tb) in enumerate(
            self.danh_sach_hien_tai
        ):
            dong = (
                f"{ma_sv:<11} | {ho_ten:<27} | "
                f"{lop:<12} | DTB: {diem_tb:4.2f} | {db.xep_loai(diem_tb)}"
            )
            self.listbox_sinh_vien.insert(tk.END, dong)
            if ma_sv == ma_can_chon:
                vi_tri_can_chon = vi_tri

        if vi_tri_can_chon is not None:
            self.listbox_sinh_vien.selection_set(vi_tri_can_chon)
            self.listbox_sinh_vien.see(vi_tri_can_chon)
            self._hien_thi_sinh_vien(self.danh_sach_hien_tai[vi_tri_can_chon])

        self.nhan_trang_thai.config(
            text=f"Dang hien thi {len(self.danh_sach_hien_tai)} sinh vien."
        )

    def _hien_thi_sinh_vien(self, sinh_vien):
        ma_sv, ho_ten, lop, diem_tb = sinh_vien
        self.ma_sv_dang_chon = ma_sv
        self.o_ma_sv.config(state="normal")
        self.o_ma_sv.delete(0, tk.END)
        self.o_ma_sv.insert(0, ma_sv)
        self.o_ma_sv.config(state="readonly")

        for o_nhap, gia_tri in (
            (self.o_ho_ten, ho_ten),
            (self.o_lop, lop),
            (self.o_diem_tb, f"{diem_tb:g}"),
        ):
            o_nhap.delete(0, tk.END)
            o_nhap.insert(0, gia_tri)

    def khi_chon_sinh_vien(self, event=None):
        lua_chon = self.listbox_sinh_vien.curselection()
        if lua_chon and lua_chon[0] < len(self.danh_sach_hien_tai):
            self._hien_thi_sinh_vien(self.danh_sach_hien_tai[lua_chon[0]])

    def doc_du_lieu_nhap(self):
        ma_sv = self.o_ma_sv.get().strip().upper()
        ho_ten = self.o_ho_ten.get().strip()
        lop = self.o_lop.get().strip().upper()
        diem_chuoi = self.o_diem_tb.get().strip().replace(",", ".")

        if not ma_sv or not ho_ten or not lop or not diem_chuoi:
            messagebox.showerror("Loi", "Vui long nhap day du thong tin.")
            return None
        try:
            diem_tb = float(diem_chuoi)
        except ValueError:
            messagebox.showerror("Loi", "Diem trung binh phai la mot so.")
            return None
        if not (0 <= diem_tb <= 10):
            messagebox.showerror("Loi", "Diem trung binh phai tu 0 den 10.")
            return None
        return ma_sv, ho_ten, lop, diem_tb

    def xoa_o_nhap(self):
        self.ma_sv_dang_chon = None
        self.o_ma_sv.config(state="normal")
        for o_nhap in (self.o_ma_sv, self.o_ho_ten, self.o_lop, self.o_diem_tb):
            o_nhap.delete(0, tk.END)
        self.listbox_sinh_vien.selection_clear(0, tk.END)

    # -------------------------------------
    # CRUD: THEM / SUA / XOA / TIM KIEM
    # -------------------------------------
    def xu_ly_them(self):
        if self.ma_sv_dang_chon is not None:
            messagebox.showwarning(
                "Thong bao", "Nhan 'Lam moi' truoc khi them sinh vien moi."
            )
            return
        du_lieu = self.doc_du_lieu_nhap()
        if du_lieu is None:
            return
        try:
            db.them_sinh_vien(*du_lieu)
        except sqlite3.IntegrityError:
            messagebox.showerror("Loi", "Ma sinh vien da ton tai!")
            return
        self.xoa_o_nhap()
        self.tai_lai_danh_sach_sinh_vien()
        messagebox.showinfo("Thanh cong", "Da them sinh vien thanh cong!")

    def xu_ly_sua(self):
        if self.ma_sv_dang_chon is None:
            messagebox.showwarning("Thong bao", "Hay chon sinh vien can sua.")
            return
        du_lieu = self.doc_du_lieu_nhap()
        if du_lieu is None:
            return
        _, ho_ten, lop, diem_tb = du_lieu
        ma_sv = self.ma_sv_dang_chon
        db.sua_sinh_vien(ma_sv, ho_ten, lop, diem_tb)
        self.tai_lai_danh_sach_sinh_vien(ma_sv)
        messagebox.showinfo("Thanh cong", "Da sua sinh vien thanh cong!")

    def xu_ly_xoa(self):
        if self.ma_sv_dang_chon is None:
            messagebox.showwarning("Thong bao", "Hay chon sinh vien can xoa.")
            return
        if not messagebox.askyesno("Xac nhan", "Ban co muon xoa sinh vien nay?"):
            return
        db.xoa_sinh_vien(self.ma_sv_dang_chon)
        self.xoa_o_nhap()
        self.tai_lai_danh_sach_sinh_vien()
        messagebox.showinfo("Thanh cong", "Da xoa sinh vien!")

    def xu_ly_lam_moi(self):
        self.o_tim_kiem.delete(0, tk.END)
        self.xoa_o_nhap()
        self.tai_lai_danh_sach_sinh_vien()

    # -------------------------------------
    # HOAT DONG 5: BIEU DO MATPLOTLIB
    # -------------------------------------
    def xu_ly_thong_ke(self):
        du_lieu = db.thong_ke_xep_loai()
        if sum(so_luong for _, so_luong in du_lieu) == 0:
            messagebox.showinfo("Thong bao", "Chua co sinh vien de thong ke.")
            return

        # Hien thi truc tiep trong cua so Tkinter, on dinh khi dong goi .app.
        from matplotlib.figure import Figure
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

        nhom = [dong[0] for dong in du_lieu]
        so_luong = [dong[1] for dong in du_lieu]
        cua_so = tk.Toplevel(self)
        cua_so.title("Thong ke xep loai sinh vien")
        cua_so.geometry("710x475")

        hinh = Figure(figsize=(7, 4), dpi=100)
        truc = hinh.add_subplot(111)
        truc.bar(nhom, so_luong, color="cornflowerblue")
        truc.set_title("So luong sinh vien theo xep loai")
        truc.set_xlabel("Xep loai")
        truc.set_ylabel("So luong sinh vien")
        truc.set_ylim(0, max(so_luong) + 1)
        truc.yaxis.get_major_locator().set_params(integer=True)
        hinh.tight_layout()
        hinh.savefig(
            db.THU_MUC_DU_LIEU / "thong_ke_xep_loai.png", dpi=150
        )

        canvas = FigureCanvasTkAgg(hinh, master=cua_so)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        cua_so.canvas = canvas
        cua_so.lift()


if __name__ == "__main__":
    UngDungSinhVien().mainloop()
