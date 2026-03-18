class NhanVien:
    def __init__ (self, tenNhanVien="", luongCoBan=0, heSoLuong=0):
        self.tenNhanVien = tenNhanVien
        self.luongCoBan = luongCoBan
        self.heSoLuong = heSoLuong
    def getTen(self):
        return self.tenNhanVien
    def setTen(self, ten):
        self.tenNhanVien = ten
    def getLuongCoBan(self):
        return self.luongCoBan
    def setLuongCoBan(self, lcb):
        self.luongCoBan = lcb
    def getHeSoLuong(self):
        return self.heSoLuong
    def setHeSoLuong(self, hsl):
        self.heSoLuong = hsl
    def input(self):
        self.tenNhanVien = input("Nhập tên nhân viên: ")
        self.luongCoBan = float(input("Nhập lương cơ bản: "))
        self.heSoLuong = float(input("Nhập hệ số lương: "))
    def tinhLuong(self):
        return self.luongCoBan * self.heSoLuong
    def inTTin(self):
        print("Nhân viên: ",self.tenNhanVien)
        print("Lương cơ bản: ",self.luongCoBan)
        print("Hệ số lương: ",self.heSoLuong)
        print("Lương: ",self.tinhLuong())
    luongMax = 100000000
    def tangLuong(self, delta):
        luongMoi = self.tinhLuong() + delta
        if luongMoi > nv.luongMax:
            print("Vượt quá lương tối đa!")
            return False
        else:
            self.luongCoBan += delta / self.heSoLuong
            return True
nv = NhanVien()
nv.input()
nv.tinhLuong()
nv.inTTin()
nv.tangLuong(100000000)


