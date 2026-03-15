class ConCho:
    def __init__(self,ten,mau_sac,giong,cam_xuc):
        self.ten=ten
        self.mau_sac=mau_sac
        self.giong=giong
        self.cam_xuc=cam_xuc

    def Sua(self):
        print(self.ten,"đang sủa.")
    def Vay_duoi(self):
        print(self.ten,"đang vẫy đuôi.")
    def An(self):
        print(self.ten,"đang ăn.")
    def Chay(self):
        print(self.ten,"đang chạy.")
    
con_cho = ConCho("Mike","Màu nâu","Giống poodle","Vui vẻ")
con_cho.Sua()

class Oto:
    def __init__(self,hang,kich_thuoc,mau,gia):
        self.hang=hang
        self.kich_thuoc=kich_thuoc
        self.mau=mau
        self.gia=gia

    def Tang_toc(self):
        print("Xe",self.hang,"đang tăng tốc.")
    def Giam_toc(self):
        print("Xe",self.hang,"đang giảm tốc.")
    def Dam(self):
        print("Xe",self.hang,"đâm.")

o_to = Oto("Porche","to","Màu đỏ","1 tỉ")
o_to.Tang_toc()

class TaiKhoan:
    def __init__(self,ten_tk,so_tk,ngan_hang,so_du):
        self.ten_tk=ten_tk
        self.so_tk=so_tk
        self.ngan_hang=ngan_hang
        self.so_du=so_du

    def Rut(self):
        print("Tài khoản",self.ten_tk,"rút 1,000,000vnđ.")
    def Gui(self):
        print("Tài khoản",self.ten_tk,"gửi 100,000vnđ.")
    def Kiem_tra_so_du(self):
        print("Tài khoản",self.ten_tk,"còn 300,000vnđ.")

tai_khoan = TaiKhoan("NGUYEN VU HUONG LY","027xxx935","Techcombank","100,000vnđ")
tai_khoan.Gui()


