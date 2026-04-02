class CanBo:
    def __init__(self,ho_ten,tuoi,gioi_tinh,dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
    def hien_thi(self):
        print(f"Tên: {self.ho_ten}, Tuổi: {self.tuoi}, GT: {self.gioi_tinh}, ĐC: {self.dia_chi}")
class CongNhan(CanBo):
    def __init__(self,ho_ten,tuoi,gioi_tinh,dia_chi,bac):
        super().__init__(ho_ten,tuoi,gioi_tinh,dia_chi)
        self.bac=bac
class KySu(CanBo):
    def __init__(self,ho_ten,tuoi,gioi_tinh,dia_chi,nganh_dao_tao):
        super().__init__(ho_ten,tuoi,gioi_tinh,dia_chi)
        self.nganh_dao_tao = nganh_dao_tao
class NhanVien(CanBo):
    def __init__(self,ho_ten,tuoi,gioi_tinh,dia_chi,cong_viec):
        super().__init__(ho_ten,tuoi,gioi_tinh,dia_chi)
        self.cong_viec = cong_viec
class QLCB:
    def __init__(self):
        self.danh_sach = []
    def hienthi_Ds(self):
     for cb in self.danh_sach:
        cb.hien_thi()
    def them_Canbo(self):
        self.ho_ten = input("Họ và tên: ")
        self.tuoi = input("Tuổi: ")
        self.gioi_tinh = input("Giới tính: ")
        self.dia_chi = input("Địa chỉ: ")
        cb = CanBo(self.ho_ten,self.tuoi,self.gioi_tinh,self.dia_chi)
        self.danh_sach.append(cb)
    def hien_thi(self):
        print(f"Tên: {self.ho_ten}, Tuổi: {self.tuoi}, GT: {self.gioi_tinh}, ĐC: {self.dia_chi}")
    def timtheo_Ten(self):
        ten_can_tim = input("Nhập tên cần tìm: ")
        found = False
        for cb in self.danh_sach:
            if ten_can_tim.lower() in cb.ho_ten.lower():
                cb.hien_thi()
                found = True
        if not found:
            print("Không tìm thấy!")
ql = QLCB()
while True:
    print("\n ===== MENU =====")
    print("1. Thêm mới cán bộ")
    print("2. Tìm kiếm theo họ tên")
    print("3. Hiển thị danh sách thông tin cán bộ")
    print("0. Thoát khỏi chương trình")
    choice = input("Chọn: ")
    if choice == "1":
        ql.them_Canbo()
    elif choice == "2":
        ql.timtheo_Ten()
    elif choice == "3":
        ql.hienthi_Ds()
    elif choice == "0":
        print(">> Thoát chương trình")
        break
    else:
        print(">> Lựa chọn không hợp lệ!")

