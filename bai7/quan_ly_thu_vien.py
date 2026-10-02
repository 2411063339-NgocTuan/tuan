danhsachsach = [
    {"masach": "S001", "tensach": "Lap Trinh Python Co Ban", "tacgia": "Nguyen Van A", "soluong": 5, "trangthai": "Con sach"},
    {"masach": "S002", "tensach": "Cau Truc Du Lieu Va Giai Thuat", "tacgia": "Tran Van B", "soluong": 2, "trangthai": "Con sach"},
    {"masach": "S003", "tensach": "Co So Thong Tin", "tacgia": "Le Thi C", "soluong": 0, "trangthai": "Het sach"}
]
lichsumuontra = []
def nhapsonguyen(loi_nhac):
    while True:
        try:
            return int(input(loi_nhac))
        except ValueError:
            print("... Du lieu khong hop le, vui long nhap lai mot so nguyen.")
def timsachtheoma(masach):
    for sach in danhsachsach:
        if sach["masach"] == masach:
            return sach
    return None
def hienthidanhsachsach():
    print("\n" + "=" * 75)
    print(f"{'Ma sach': <10}{'Ten sach': <32}{'Tac gia': <18}{'SL': <6}{'Trang thai': <12}")
    print("-" * 75)
    for sach in danhsachsach:
        print(f"{sach['masach']: <10}{sach['tensach']: <32}{sach['tacgia']: <18}{sach['soluong']: <6}{sach['trangthai']: <12}")
    print("=" * 75)
def timkiemsach():
    masach = input("Nhap ma sach can tim: ").strip().upper()
    sach = timsachtheoma(masach)
    if sach:
        print(f"\n=> THÔNG TIN SÁCH TÌM THẤY:")
        print(f"   Mã sách: {sach['masach']} | Tên sách: {sach['tensach']} | Tác giả: {sach['tacgia']} | SL: {sach['soluong']} | Trạng thái: {sach['trangthai']}")
    else:
        print(f"=> Khong tìm thấy sách có mã {masach}.")
def themsachmoi():
    masach = input("Nhap ma sach moi: ").strip().upper()
    if timsachtheoma(masach) is not None:
        print(f"-> Mã sách {masach} đã tồn tại trong thư viện.")
        return
    tensach = input("Nhap ten sach: ").strip().title()
    tacgia = input("Nhap ten tac gia: ").strip().title()
    soluong = nhapsonguyen("Nhap so luong sach: ")
    trangthai = "Con sach" if soluong > 0 else "Het sach"
    danhsachsach.append({
        "masach": masach,
        "tensach": tensach,
        "tacgia": tacgia,
        "soluong": soluong,
        "trangthai": trangthai
    })
    print(f"-> Đã thêm sách '{tensach}' thành công.")
def muonsach():
    masach = input("Nhap ma sach can muon: ").strip().upper()
    sach = timsachtheoma(masach)
    if sach is None:
        print(f"-> Không tìm thấy sách có mã {masach}.")
        return
    if sach["soluong"] <= 0:
        print(f"-> Sách '{sach['tensach']}'đã hết, không thể mượn.")
        return
    tennguoimuon = input("Nhap ten nguoi muon: ").strip().title()
    sach["soluong"] -= 1
    if sach["soluong"] == 0:
        sach["trangthai"] = "Het sach" 
    lichsumuontra.append({
        "masach": masach,
        "tensach": sach['tensach'],
        "nguoi_muon": tennguoimuon,
        "hanh_dong": "Muon"
    })
    print(f"-> Độc giả {tennguoimuon} đã mượn thành công sách '{sach['tensach']}'.")
def trasach():
    masach = input("Nhap ma sach can tra: ").strip().upper()
    sach = timsachtheoma(masach)
    if sach is None:
        print(f"=> Không tìm thấy sách có mã {masach}.")
        return
    tennguoitra = input("Nhap ten nguoi tra: ").strip().title()
    sach["soluong"] += 1
    sach["trangthai"] = "Con sach"
    lichsumuontra.append({
        "masach": masach,
        "tensach": sach['tensach'],
        "nguoi_muon": tennguoitra,
        "hanh_dong": "Tra"
    })
    print(f"-> Độc giả {tennguoitra} đã trả lại sách '{sach['tensach']}' thành công.")
def thongkethuvien():
    print("\n______ THỐNG KÊ HOẠT ĐỘNG THƯ VIỆN ______")
    print(f"- Tổng số đầu sách trong thư viện: {len(danhsachsach)}")
    tongluotgiaodich = len(lichsumuontra)
    print(f"- Tổng số lượt giao dịch mượn/trả: {tongluotgiaodich}")
    if tongluotgiaodich > 0:
        print("\nLịch sử giao dịch gần đây:")
        for gd in lichsumuontra:
            print(f"  + [{gd['hanh_dong']}] Sách: {gd['tensach']} | Độc giả: {gd['nguoi_muon']}")
def hienthimenu():
    print("\n______ QUẢN LÝ THƯ VIỆN SÁCH ______")
    print("1. Hiển thị danh sách toàn bộ sách")
    print("2. Tìm kiếm sách")
    print("3. Thêm sách mới")
    print("4. Mượn sách cho độc giả")
    print("5. Trả sách Thanh toán")
    print("6. Thống kê hoạt động thư viện")
    print("0. Thoát chương trình")
def chaychuongtrinh():
    while True:
        hienthimenu()
        luachon = input("Nhập lựa chọn của bạn (0-6): ").strip()
        if luachon == "1":
            hienthidanhsachsach()
        elif luachon == "2":
            timkiemsach()
        elif luachon == "3":
            themsachmoi()
        elif luachon == "4":
            muonsach()
        elif luachon == "5":
            trasach()
        elif luachon == "6":
            thongkethuvien()
        elif luachon == "0":
            print("Cảm ơn đã sử dụng chương trình thư viện. Tạm biệt!")
            break
        else:
            print("=> Lựa chọn không hợp lệ, vui lòng chọn lại từ 0 đến 6.")
if __name__ == "__main__":
    chaychuongtrinh()