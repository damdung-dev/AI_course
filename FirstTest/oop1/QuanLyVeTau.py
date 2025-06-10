class QuanLyVeTau:
    def __init__(self):
        self.__vetau_list=[]
    @property
    def vetau_list(self):
        return self.__vetau_list
    @vetau_list.setter
    def vetau_list(self,Vetau_list):
        self.__vetau_list = Vetau_list

    def themVeTau(self,vetau):
        self.__vetau_list.append(vetau)
    def hienThiVeTau(self):
        print("Thông tin vé:")
        print("Mã vé    |   Mã tàu  |   Giá tiền")
        for v in self.vetau_list:
            print(v)
    def tongGiaTien(self):
        sum=0
        for v in self.vetau_list:
            sum=sum+float(v.thanhTien())
        print( f"Tổng tiền: {sum} VND")
            