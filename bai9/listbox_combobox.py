import tkinter as tk
from tkinter import ttk

cua_so = tk.Tk()
cua_so.title("Ví dụ Listbox & Combobox")
cua_so.geometry("320x330")

tk.Label(cua_so, text="Chọn môn học:", font=("Arial", 11, "bold")).pack(pady=5)
listbox_mon_hoc = tk.Listbox(cua_so, selectmode="single", height=5)
for mon in ["Toan", "Ly", "Hoa", "Van", "Anh"]:
    listbox_mon_hoc.insert(tk.END, mon)
listbox_mon_hoc.pack(pady=5)

def xem_mon_da_chon():
    lua_chon = listbox_mon_hoc.curselection()
    if lua_chon:
        nhan_ket_qua_lb.config(text=f"Mon da chon: {listbox_mon_hoc.get(lua_chon[0])}")

tk.Button(cua_so, text="Xem mon da chon", command=xem_mon_da_chon).pack(pady=2)
nhan_ket_qua_lb = tk.Label(cua_so, text="", fg="blue")
nhan_ket_qua_lb.pack(pady=2)

tk.Label(cua_so, text="Chọn thành phố:", font=("Arial", 11, "bold")).pack(pady=5)
combobox_thanh_pho = ttk.Combobox(cua_so, values=["Ha Noi", "Da Nang", "TP.HCM", "Hue"])
combobox_thanh_pho.current(0)
combobox_thanh_pho.pack(pady=5)

def xem_thanh_pho():
    nhan_ket_qua_cb.config(text=f"Ban chon: {combobox_thanh_pho.get()}")

tk.Button(cua_so, text="Xac nhan", command=xem_thanh_pho).pack(pady=2)
nhan_ket_qua_cb = tk.Label(cua_so, text="", fg="blue")
nhan_ket_qua_cb.pack(pady=2)

cua_so.mainloop()