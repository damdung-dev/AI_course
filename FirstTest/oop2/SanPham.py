from abc import ABC, abstractmethod

class SanPham(ABC):
    def __init__(self, MaSP,TenSP):
        self.__MaSP = MaSP
        self.__TenSP = TenSP
    @property
    def MaSP(self):
        return self.__MaSP
    @MaSP.setter
    def MaSP(self,MaSP):
        self.__MaSP = MaSP
    @property
    def TenSP(self):
        return self.__TenSP
    @TenSP.setter
    def TenSP(self,TenSP):
        self.__TenSP = TenSP
    @abstractmethod
    def chiPhiSuaChua(self):
        pass
    def __str__(self):
        return f"{self.__MaSP} {self.__TenSP}"