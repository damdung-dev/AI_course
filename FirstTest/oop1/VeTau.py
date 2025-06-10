from abc import ABC, abstractmethod, abstractclassmethod
class VeTau(ABC):
    list_MaTau=["SE1","SE2","SE3","SE4","TN1","TN2"]
    def __init__(self, MaVe, MaTau, DonGia, SoLuong):
        self.__MaVe = MaVe
        self.__MaTau = MaTau
        self.__DonGia = DonGia
        self.__SoLuong = SoLuong
    @property
    def ma_ve(self):
        return self.__MaVe
    @ma_ve.setter
    def ma_ve(self, MaVe):
        self.__MaVe = MaVe
    @property
    def ma_tau(self):
        return self.__MaTau
    @ma_tau.setter
    def ma_tau(self, MaTau):
        self.__MaTau = MaTau
    @property
    def don_gia(self):
        return self.__DonGia
    @don_gia.setter
    def don_gia(self, DonGia):
        self.__DonGia = DonGia
    @property
    def so_luong(self):
        return self.__SoLuong
    @so_luong.setter
    def so_luong(self, SoLuong):
        self.__SoLuong = SoLuong

    def thanhTien(self):
        pass
    def __str__(self):
        if self.__MaTau in self.list_MaTau:
            st="{:<20} | {:<20} | {:<20} ".format(self.__MaVe, self.__MaTau, self.__DonGia, self.__SoLuong)
            return st
        else:
            return "Vui lòng nhập lại mã tàu! "