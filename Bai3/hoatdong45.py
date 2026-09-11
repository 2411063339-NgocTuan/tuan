# ==========================================
# HOAT DONG 4: TUPLE
# ==========================================

print("===== BAI 4.1 =====")

toa_do = (3, 5)

print(toa_do, type(toa_do))

# Thu gan lai se gay loi TypeError vi tuple bat bien
# toa_do[0] = 10


# Bai tap 4.2 - Unpacking tuple
print("\n===== BAI 4.2 =====")

x, y = toa_do

print("x =", x, "- y =", y)

# Doi gia tri 2 bien bang unpacking
a, b = 10, 20

print("Truoc khi doi:")
print("a =", a, "- b =", b)

a, b = b, a

print("Sau khi doi:")
print("a =", a, "- b =", b)


# Bai tap 4.3 - Tra ve nhieu gia tri
print("\n===== BAI 4.3 =====")

c, d = 17, 5

thuong_du = divmod(c, d)

thuong, du = thuong_du

print(f"{c} chia {d} duoc thuong {thuong}, du {du}")


# ==========================================
# HOAT DONG 5: TOA DO DIEM VA KHOANG CACH
# ==========================================

print("\n===== BAI 5 =====")

import math

diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)

print(
    f"Khoang cach giua {diem_a} va {diem_b} la: "
    f"{round(khoang_cach, 2)}"
)

# Danh sach cac diem
cac_diem = [(0, 0), (3, 4), (6, 8)]

print("\nKhoang cach cac diem den goc toa do (0, 0):")

for diem in cac_diem:
    x, y = diem
    khoang_cach = math.sqrt(x ** 2 + y ** 2)

    print(
        f"Diem {diem} cach goc toa do: "
        f"{round(khoang_cach, 2)}"
    )