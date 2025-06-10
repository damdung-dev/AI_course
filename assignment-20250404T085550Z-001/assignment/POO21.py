class Students:
    #Attributes:
    list_studentName = []
    list_id = []
    list_semester = []
    listcourseName_input = []

    #Constructor:
    def __init__(self, id, student_name, semester, course_name):
        self.id=id
        self.student_name=student_name
        self.semester=semester
        self.course_name=course_name
    #Methods:
    def create(self):
        Students.list_id.append(self.id)
        Students.list_studentName.append(self.student_name)
        Students.list_semester.append(self.semester)
        Students.listcourseName_input.append(self.course_name)

        print("===================Dữ liệu trong hệ thống======================")
        for i in range(0,len(Students.list_studentName)):
            print(f"Tên học sinh: {Students.list_studentName[i]}\n\t"
                    f"- id: {Students.list_id[i]}\n\t- Kỳ học: {Students.list_semester[i]}\n\t"
                    f"- Tên khóa học: {Students.listcourseName_input[i]}")
    def find_and_sort(self):
        user=input("Bạn cần tìm tên nào: ")
        if user in sorted(Students.list_studentName, reverse=False):
            print(f"Tên {user} có trong hệ thống")
            print(sorted(Students.list_studentName, reverse=False))
            list_studentNameSorted=sorted(Students.list_studentName, reverse=False)
            print(list_studentNameSorted)
            heso=Students.list_studentName.index(user)
            print(f"Tên học sinh: {Students.list_studentName[heso]}\n\t"
                  f"- id: {Students.list_id[heso]}\n\t- Kỳ học: {Students.list_semester[heso]}\n\t"
                  f"- Tên khóa học: {Students.listcourseName_input[heso]}")
        else:
            print(f"Tên bạn đã nhập không có, xin vui lòng thử lại")
    def upgrade_delete(self):
        user = input("Nhập vào ID của bạn: ")
        heso=Students.list_id.index(user)
        print(f"Tên học sinh: {Students.list_studentName[heso]}\n\t"
              f"- id: {Students.list_id[heso]}\n\t- Kỳ học: {Students.list_semester[heso]}\n\t"
              f"- Tên khóa học: {Students.listcourseName_input[heso]}")
        print("------------------------------------------------------")
        user1 = input("Bạn có muốn thay đổi hay muốn xóa ID: \n1. Thay đổi\n2. Xóa")
        if user1=="1":
            newid=input("Nhập vào ID mới bạn muốn thay đổi: ")
            user2=input("Bạn có chắc chắn muốn thay đổi: \n1. Yes\n2. No")
            if user2=="1":
                Students.list_id[heso]=newid
                print(f"Tên học sinh: {Students.list_studentName[heso]}\n\t"
                      f"- id: {Students.list_id[heso]}\n\t- Kỳ học: {Students.list_semester[heso]}\n\t"
                      f"- Tên khóa học: {Students.listcourseName_input[heso]}")
            else:
                print(f"Tên học sinh: {Students.list_studentName[heso]}\n\t"
                      f"- id: {Students.list_id[heso]}\n\t- Kỳ học: {Students.list_semester[heso]}\n\t"
                      f"- Tên khóa học: {Students.listcourseName_input[heso]}")
        if user1=="2":
            Students.list_id.remove(Students.list_id[heso])
            user3 = input("Bạn có chắc chắn muốn thay đổi: \n1. Yes\n2. No")
            if user3 == "1":
                Students.list_id[heso] = newid
                print(f"Tên học sinh: {Students.list_studentName[heso]}\n\t"
                      f"- id: {Students.list_id[heso]}\n\t- Kỳ học: {Students.list_semester[heso]}\n\t"
                      f"- Tên khóa học: {Students.listcourseName_input[heso]}")
            else:
                print(f"Tên học sinh: {Students.list_studentName[heso]}\n\t"
                      f"- id: {Students.list_id[heso]}\n\t- Kỳ học: {Students.list_semester[heso]}\n\t"
                      f"- Tên khóa học: {Students.listcourseName_input[heso]}")
    def report(self):
        list_studentNameSorted = sorted(Students.list_studentName, reverse=False)
        for i in list_studentNameSorted:
            heso1=list_studentNameSorted.index(i)
            heso2=Students.list_studentName.index(i)
            print(f"Tên học sinh: {list_studentNameSorted[heso1]}"
                  f"- Tên khóa học: {Students.listcourseName_input[heso2]}")



