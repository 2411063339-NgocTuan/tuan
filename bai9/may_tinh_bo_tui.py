import tkinter as tk
from tkinter import messagebox

def khi_click(gia_tri):
    hien_tai = bien_hien_thi.get()
    if hien_tai == "Loi" or hien_tai == "0":
        bien_hien_thi.set(str(gia_tri))
    else:
        bien_hien_thi.set(hien_tai + str(gia_tri))
def xoa_man_hinh():
    bien_hien_thi.set("0")
def tinh_ket_qua():
    bieu_thuc = bien_hien_thi.get()
    try:
        ket_qua = eval(bieu_thuc.replace('x', '*').replace('÷', '/'))
        bien_hien_thi.set(str(ket_qua))
    except ZeroDivisionError:
        messagebox.showerror("Loi", "Khong the chia cho so 0!")
        bien_hien_thi.set("Loi")
    except Exception:
        messagebox.showerror("Loi", "Bieu thuc khong hop le!")
        bien_hien_thi.set("Loi")
cua_so = tk.Tk()
cua_so.title("Máy tính bỏ túi")
cua_so.geometry("310x400")
cua_so.resizable(False, False)

bien_hien_thi = tk.StringVar(value="0")

man_hinh = tk.Entry(cua_so, textvariable=bien_hien_thi, font=("Arial", 18), justify="right", bd=5, relief="sunken")
man_hinh.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=8, sticky="we")

tk.Button(cua_so, text="C", width=5, height=2, font=("Arial", 11), bg="#ff9999", command=xoa_man_hinh).grid(row=1, column=0, padx=5, pady=5)
tk.Button(cua_so, text="÷", width=5, height=2, font=("Arial", 11), bg="#e0e0e0", command=lambda: khi_click('÷')).grid(row=1, column=1, padx=5, pady=5)
tk.Button(cua_so, text="x", width=5, height=2, font=("Arial", 11), bg="#e0e0e0", command=lambda: khi_click('x')).grid(row=1, column=2, padx=5, pady=5)
tk.Button(cua_so, text="-", width=5, height=2, font=("Arial", 11), bg="#e0e0e0", command=lambda: khi_click('-')).grid(row=1, column=3, padx=5, pady=5)

tk.Button(cua_so, text="7", width=5, height=2, font=("Arial", 11), command=lambda: khi_click(7)).grid(row=2, column=0, padx=5, pady=5)
tk.Button(cua_so, text="8", width=5, height=2, font=("Arial", 11), command=lambda: khi_click(8)).grid(row=2, column=1, padx=5, pady=5)
tk.Button(cua_so, text="9", width=5, height=2, font=("Arial", 11), command=lambda: khi_click(9)).grid(row=2, column=2, padx=5, pady=5)
tk.Button(cua_so, text="+", width=5, height=2, font=("Arial", 11), bg="#e0e0e0", command=lambda: khi_click('+')).grid(row=2, column=3, padx=5, pady=5)

tk.Button(cua_so, text="4", width=5, height=2, font=("Arial", 11), command=lambda: khi_click(4)).grid(row=3, column=0, padx=5, pady=5)
tk.Button(cua_so, text="5", width=5, height=2, font=("Arial", 11), command=lambda: khi_click(5)).grid(row=3, column=1, padx=5, pady=5)
tk.Button(cua_so, text="6", width=5, height=2, font=("Arial", 11), command=lambda: khi_click(6)).grid(row=3, column=2, padx=5, pady=5)
tk.Button(cua_so, text="=", width=5, height=5, font=("Arial", 11), bg="#99ccff", command=tinh_ket_qua).grid(row=3, column=3, rowspan=2, padx=5, pady=5, sticky="ns")

tk.Button(cua_so, text="1", width=5, height=2, font=("Arial", 11), command=lambda: khi_click(1)).grid(row=4, column=0, padx=5, pady=5)
tk.Button(cua_so, text="2", width=5, height=2, font=("Arial", 11), command=lambda: khi_click(2)).grid(row=4, column=1, padx=5, pady=5)
tk.Button(cua_so, text="3", width=5, height=2, font=("Arial", 11), command=lambda: khi_click(3)).grid(row=4, column=2, padx=5, pady=5)

tk.Button(cua_so, text="0", width=12, height=2, font=("Arial", 11), command=lambda: khi_click(0)).grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")
tk.Button(cua_so, text=".", width=5, height=2, font=("Arial", 11), command=lambda: khi_click('.')).grid(row=5, column=2, padx=5, pady=5)

if __name__ == "__main__":
    cua_so.mainloop()