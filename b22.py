class SieuNhan:
    def __init__(self,ten,vu_khi,mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
    def introduce(self):
        print("Nhập tên: ",self.ten)
        print("Nhập vũ khí: ",self.vu_khi)
        print("Nhập màu sắc: ",self.mau_sac)
sieu_nhan_A = SieuNhan("A","Kiếm","Đỏ")
sieu_nhan_B = SieuNhan("B","Khiên","Xanh")
sieu_nhan_A.introduce()
sieu_nhan_B.introduce()
