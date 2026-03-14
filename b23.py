class SieuNhan:
    def __init__(self, ten="", mau_sac="", ki_nang=""):
        self.ten = ten
        self.mau_sac = mau_sac
        self.ki_nang = ki_nang

    def input(self):
        self.ten = input("Nhập tên (stop để dừng): ")
        if self.ten.lower() == "stop":
            return False
        self.mau_sac = input("Nhập màu sắc: ")
        self.ki_nang = input("Nhập kĩ năng: ")
        return True

    def output(self):
        print(self.ten)
        print(self.mau_sac)
        print(self.ki_nang)


danh_sach = []

while True:
    sieunhan = SieuNhan()
    if not sieunhan.input():
        break
    danh_sach.append(sieunhan)

for sieunhan in danh_sach:
    sieunhan.output()