def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def bscnn(a, b):
    return a * b // uscln(a, b)
def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n
print("--- Hoạt động 1 ---")
print("USCLN(24, 36):", uscln(24, 36))
print("BSCNN(4, 6):", bscnn(4, 6))
print("Kiểm tra nguyên tố (29):", kiem_tra_nguyen_to(29))
print("Kiểm tra số hoàn thiện (28):", kiem_tra_so_hoan_thien(28))
def in_loi_chao(ten):
    print(f"Xin chao, {ten}!")
    return 
def chia_lay_thuong_du(a, b):
    return a // b, a % b 
in_loi_chao("An")
thuong, du = chia_lay_thuong_du(17, 5)
print(f"Thuong: {thuong}, du: {du}")
def gioi_thieu(ten, tuoi=18, lop="Chua ro"):
    print(f"Ten: {ten} - Tuoi: {tuoi} - Lop: {lop}")
print("\n--- Hoạt động 2 ---")
gioi_thieu("An")
gioi_thieu("Binh", 20)
gioi_thieu("Chi", lop="CNTT01")
gioi_thieu(ten="Dung", lop="CNTT02", tuoi=19) 
def tinh_tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong
print("\n--- Hoạt động 3.1 (*args) ---")
print(tinh_tong(1, 2, 3))
print(tinh_tong(5, 10, 15, 20, 25))
print(tinh_tong())
def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"Ho ten: {ho_ten} - Tuoi: {tuoi}")
    for khoa, gia_tri in kwargs.items():
        print(f"  {khoa}: {gia_tri}")
print("\n--- Hoạt động 3.2 (**kwargs) ---")
in_thong_tin("Nguyen Van A", 20, lop="CNTT01", que_quan="Ha Noi")
in_thong_tin("Tran Thi B", 21, email="b@example.com")