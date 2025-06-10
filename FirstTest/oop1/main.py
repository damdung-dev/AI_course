from VeNgoi import VeNgoi
from VeNam import VeNam
from oop1.QuanLyVeTau import QuanLyVeTau

obj1=VeNgoi("11","SE1",780000,3,"A")
obj2=VeNam("77","SE3",1680000,3,"6")
system=QuanLyVeTau()
system.themVeTau(obj1)
system.themVeTau(obj2)
system.hienThiVeTau()
system.tongGiaTien()