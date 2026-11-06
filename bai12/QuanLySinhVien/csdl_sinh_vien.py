
import sqlite3
import sys
from pathlib import Path


if getattr(sys, "frozen", False):
    THU_MUC_DU_LIEU = (
        Path.home() / "Library" / "Application Support" / "QuanLySinhVien"
    )
else:
    THU_MUC_DU_LIEU = Path(__file__).resolve().parent

THU_MUC_DU_LIEU.mkdir(parents=True, exist_ok=True)
TEN_FILE_CSDL = THU_MUC_DU_LIEU / "sinh_vien.db"


def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)


def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    try:
        ket_noi.execute("""
            CREATE TABLE IF NOT EXISTS sinh_vien (
                ma_sv TEXT PRIMARY KEY,
                ho_ten TEXT NOT NULL,
                lop TEXT NOT NULL,
                diem_tb REAL NOT NULL CHECK (diem_tb BETWEEN 0 AND 10)
            )
        """)
        ket_noi.commit()
    finally:
        ket_noi.close()


def them_sinh_vien(ma_sv, ho_ten, lop, diem_tb):
    ket_noi = ket_noi_csdl()
    try:
        ket_noi.execute(
            "INSERT INTO sinh_vien (ma_sv, ho_ten, lop, diem_tb) VALUES (?, ?, ?, ?)",
            (ma_sv, ho_ten, lop, diem_tb),
        )
        ket_noi.commit()
    finally:
        ket_noi.close()


def lay_toan_bo_sinh_vien():
    ket_noi = ket_noi_csdl()
    try:
        return ket_noi.execute(
            "SELECT ma_sv, ho_ten, lop, diem_tb FROM sinh_vien ORDER BY ma_sv"
        ).fetchall()
    finally:
        ket_noi.close()


def sua_sinh_vien(ma_sv, ho_ten, lop, diem_tb):
    ket_noi = ket_noi_csdl()
    try:
        con_tro = ket_noi.execute(
            "UPDATE sinh_vien SET ho_ten = ?, lop = ?, diem_tb = ? WHERE ma_sv = ?",
            (ho_ten, lop, diem_tb, ma_sv),
        )
        ket_noi.commit()
        return con_tro.rowcount
    finally:
        ket_noi.close()


def xoa_sinh_vien(ma_sv):
    ket_noi = ket_noi_csdl()
    try:
        con_tro = ket_noi.execute(
            "DELETE FROM sinh_vien WHERE ma_sv = ?", (ma_sv,)
        )
        ket_noi.commit()
        return con_tro.rowcount
    finally:
        ket_noi.close()


def tim_kiem_sinh_vien(tu_khoa):
    ket_noi = ket_noi_csdl()
    try:
        mau = "%" + tu_khoa.strip() + "%"
        return ket_noi.execute(
            """SELECT ma_sv, ho_ten, lop, diem_tb
               FROM sinh_vien
               WHERE ma_sv LIKE ? OR ho_ten LIKE ? OR lop LIKE ?
               ORDER BY ma_sv""",
            (mau, mau, mau),
        ).fetchall()
    finally:
        ket_noi.close()


def xep_loai(diem_tb):
    if diem_tb >= 8:
        return "Gioi"
    if diem_tb >= 6.5:
        return "Kha"
    if diem_tb >= 5:
        return "Trung binh"
    return "Yeu"


def thong_ke_xep_loai():
    """Tra ve so luong sinh vien theo bon nhom diem (nguong minh hoa)."""
    ket_noi = ket_noi_csdl()
    try:
        ket_qua = ket_noi.execute("""
            SELECT
                CASE
                    WHEN diem_tb >= 8 THEN 'Gioi'
                    WHEN diem_tb >= 6.5 THEN 'Kha'
                    WHEN diem_tb >= 5 THEN 'Trung binh'
                    ELSE 'Yeu'
                END AS xep_loai,
                COUNT(*)
            FROM sinh_vien
            GROUP BY xep_loai
        """).fetchall()
    finally:
        ket_noi.close()

    thong_ke = {"Gioi": 0, "Kha": 0, "Trung binh": 0, "Yeu": 0}
    thong_ke.update(dict(ket_qua))
    return list(thong_ke.items())


if __name__ == "__main__":
    tao_bang_neu_chua_co()
    print("Da tao/kiem tra CSDL tai:", TEN_FILE_CSDL)
    print("So sinh vien:", len(lay_toan_bo_sinh_vien()))
