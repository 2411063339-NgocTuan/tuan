import pandas as pd

df = pd.read_csv("diem_sinh_vien.csv")
print("5 dòng đầu tiên:")
print(df.head())
print("\nKích thước (số dòng, số cột):", df.shape)
print("Danh sách tên cột:", df.columns.tolist())

diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()
print("\nĐiểm trung bình theo môn học:")
print(diem_trung_binh_mon)
print("\nĐiểm trung bình toàn bộ:", round(df["diem"].mean(), 2))
print("Điểm cao nhất:", df["diem"].max())
print("Điểm thấp nhất:", df["diem"].min())

diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)
print("\nĐiểm trung bình từng sinh viên:")
print(diem_tb_sv)

sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]
sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]

print("Sinh viên đạt:")
print(sinh_vien_dat)
print("Sinh viên không đạt:")
print(sinh_vien_khong_dat)