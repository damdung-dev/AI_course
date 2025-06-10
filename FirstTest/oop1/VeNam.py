from VeTau import VeTau
class VeNam(VeTau):
    def __init__(self, MaVe, MaTau, DonGia, SoLuong, Khoang):
        super().__init__(MaVe,MaTau,DonGia,SoLuong)
        self.__Khoang = Khoang
    @property
    def khoang(self):
        return self.__Khoang
    @khoang.setter
    def khoang(self, Khoang):
        self.__Khoang = Khoang

    def thanhTien(self):
        if self.ma_tau=="TN1" or self.ma_tau=="TN2":
            if self.khoang == "4":
                return str(super().so_luong*super().don_gia*1.2)
            elif self.khoang == "6":
                return str(super().so_luong*super().don_gia)
            else:
                return "Không có khoang tàu, quý khách vui lòng kiểm tra lại"
        elif self.ma_tau=="SE1" or self.ma_tau=="SE2" or self.ma_tau=="SE3" or self.ma_tau=="SE4":
            if self.khoang == "4":
                return str(super().so_luong*super().don_gia*1.2*1.05)
            elif self.khoang == "6":
                return str(super().so_luong*super().don_gia*1.05)
            else:
                return "Không có khoang tàu, quý khách vui lòng kiểm tra lại"
        else:
            return "Mã tàu của quý khách ko đúng, xin vui lòng thử lại"

    def __str__(self):
        st=super().__str__()
        if self.ma_tau=="TN1" or self.ma_tau=="TN2":
            if self.khoang == "4":
                st = super().__str__()
                st+= "Khoang 4 Giường"
                return st
            elif self.khoang == "6":
                st = super().__str__()
                st += "Khoang 6 Giường"
                return st
            else:
                return "Không có khoang tàu, quý khách vui lòng kiểm tra lại"
        elif self.ma_tau=="SE1" or self.ma_tau=="SE2" or self.ma_tau=="SE3" or self.ma_tau=="SE4":
            if self.khoang == "4":
                st = super().__str__()
                st += "Khoang 4 Giường"
                return st
            elif self.khoang == "6":
                st = super().__str__()
                st += "Khoang 6 Giường"
                return st
            else:
                return "Không có khoang tàu, quý khách vui lòng kiểm tra lại"
        else:
            return "Mã tàu của quý khách ko đúng, xin vui lòng thử lại"
