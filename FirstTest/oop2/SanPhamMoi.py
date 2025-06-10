class SanPhamMoi(SanPham):
    def __init__(self, MaSP,TenSP,NgayBan,SoNamBaoHanh,GiaBan,NgaySuaChua):
        super().__init__(MaSP,TenSP)
        self.__NgayBan = NgayBan
        self.__SoNamBaoHanh = SoNamBaoHanh
        self.__GiaBan = GiaBan
        self.__NgaySuaChua = NgaySuaChua
    @property
    def Ngayban(self):
        return self.__NgayBan
    @NgayBan.setter
    def NgayBan(self,NgayBan):
        self.__NgayBan = NgayBan
    @property
    def SoNamBaoHanh(self):
        return self.__SoNamBaoHanh
    @SoNamBaoHanh.setter
    def TenSP(self,SoNamBaoHanh):
        self.__TenSP = SoNamBaoHanh
    @property
    def GiaBan(self):
        return self.__GiaBan
    @GiaBan.setter
    def GiaBan(self,GiaBan):
        self.__GiaBan = GiaBan
    @property
    def NgaySuaChua(self):
        return self.__NgaySuaChua
    @NgaySuaChua.setter
    def NgaySuaChua(self,NgaySuaChua):
        self.__NgaySuaChua = NgaySuaChua

    def chiPhiSuaChua(self):
        pass

    def __str__(self):
        return f"{self.__MaSP} {self.__TenSP}"