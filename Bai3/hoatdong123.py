# ==========================================
# HOAT DONG 1: LIST CO BAN
# ==========================================

print("===== BAI 1.1 =====")

diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]

print(diem_so[0])       # phan tu dau tien
print(diem_so[-1])      # phan tu cuoi cung
print(diem_so[1:4])     # tu vi tri 1 den truoc 4
print(diem_so[::2])     # step = 2
print(diem_so[::-1])    # dao nguoc danh sach


# Bai tap 1.2
print("\n===== BAI 1.2 =====")

ten_sv = ["An", "Binh", "Chi"]

ten_sv.append("Dung")
ten_sv.insert(1, "Em")
print(ten_sv)

ten_sv.remove("Chi")

pop_ra = ten_sv.pop()
print(ten_sv, "- da xoa:", pop_ra)

ten_sv.sort()
print(ten_sv)

ten_sv.reverse()
print(ten_sv)

ten_sv.extend(["Giang", "Hoa"])
print(ten_sv)


# ==========================================
# HOAT DONG 2: DUYET LIST VA MA TRAN
# ==========================================

# Bai tap 2.1
print("\n===== BAI 2.1 =====")

diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]

tong = 0

for diem in diem_so:
    print(diem)
    tong = tong + diem

print("Tong diem:", tong)
print("Diem trung binh:", round(tong / len(diem_so), 2))


# Bai tap 2.2
print("\n===== BAI 2.2 =====")

ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# In theo tung hang
for hang in ma_tran:
    print(hang)

# In tung phan tu
for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
    print()

# Tinh tong tat ca phan tu trong ma tran
tong = 0

for hang in ma_tran:
    for phan_tu in hang:
        tong = tong + phan_tu

print("Tong cac phan tu trong ma tran:", tong)


# ==========================================
# HOAT DONG 3: LIST COMPREHENSION
# ==========================================

# Bai tap 3.1
print("\n===== BAI 3.1 =====")

day_so = list(range(1, 21))

so_chan = [x for x in day_so if x % 2 == 0]
so_le = [x for x in day_so if x % 2 != 0]

print("So chan:", so_chan)
print("So le:", so_le)


# Bai tap 3.2
print("\n===== BAI 3.2 =====")

diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]

diem_cong = [round(diem + 0.5, 2) for diem in diem_so]

print("Diem ban dau:", diem_so)
print("Diem sau khi cong:", diem_cong)