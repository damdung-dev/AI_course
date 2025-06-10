from VeTau import VeTau
class VeNgoi(VeTau):
    def __init__(self, MaVe, MaTau, DonGia, SoLuong, Loai):
        super().__init__(MaVe,MaTau, DonGia, SoLuong)
        self.__Loai = Loai
    @property
    def loai(self):
        return self.__Loai
    @loai.setter
    def loai(self, Loai):
        self.__Loai = Loai

    def thanhTien(self):
        if self.loai=="A":
            return str(super().so_luong*super().don_gia*1.1)
        elif self.loai=="B":
            return str(super().so_luong*super().don_gia)
        else:
            return "Loại vé của bạn không có sẵn"
    def __str__(self):
        if super().ma_tau in super().list_MaTau:
            if self.loai=="A":
                st=super().__str__()
                st+="Ghế mềm, điều hòa"
                return st
            elif self.loai=="B":
                st = super().__str__()
                st += "Ghế cứng"
                return st
            else:
                return "Không có loại ghế quý khách đã chọn"
        else:
            return "Lỗi xin vui lòng thử lại"