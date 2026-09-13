ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000

print("Họ tên:", ten)
print("Điểm Toán:", diem_toan)
print("Điểm Văn:", diem_van)
print("Số lượng môn học:", so_luong_mon_hoc)
print("Mức lương tối thiểu:", MUC_LUONG_TOI_THIEU)
print()

a = 17
b = 5
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print(f"a ** b = {a ** b}")

diem = 6.5
tuoi = 20
la_loai_kha = diem >= 6.5 and diem < 8.0
chua_du_18_hoac_tren_60 = tuoi < 18 or tuoi > 60
phu_dinh_dieu_kien = not (tuoi < 18 or tuoi > 60)

print("Đạt loại Khá?", la_loai_kha)
print("Chưa đủ 18 hoặc trên 60?", chua_du_18_hoac_tren_60)
print("Phủ định điều kiện tuổi:", phu_dinh_dieu_kien)

x = 10
x += 5
print("x sau += 5:", x)
x -= 3
print("x sau -= 3:", x)
x *= 2
print("x sau *= 2:", x)
x /= 4
print("x sau /= 4:", x)
x **= 2
print("x sau **= 2:", x)

danh_sach = [1, 2, 3, "python"]
print("3 có trong danh_sach không?", 3 in danh_sach)
a_list = [1, 2, 3]
b_list = a_list
print("a_list is b_list:", a_list is b_list)

print("Biểu thức 1:", 2 + 3 * 4 ** 2)
print("Biểu thức 2:", (2 + 3) * 4 ** 2)
print("Biểu thức 3:", 10 > 5 and 31 or not False)
print()

bien = 10
print(bien, type(bien))
bien = "Xin chao"
print(bien, type(bien))
bien = 3.14
print(bien, type(bien))
bien = True
print(bien, type(bien))

ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3
la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(ho_ten, "DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))