import POO21

list_courseName = ["java", ".net", "C/C++"]

def display():
    print("Bạn có muốn quay lại: ")
    sel2=input("\n1. Có\n2. Không")
    return sel2

while True:
    print("WELCOME TO STUDENT MANAGEMENT\n"
          "\t 1.Create"
          "\t 2.Find and Sort"
          "\t 3.Update/Delete"
          "\t 4.Report"
          "\t 5.Exit")
    sel1 = input("Please type one of the numbers above: ")
    if sel1=="1":
        dem = 1
        print("===================Dữ liệu nhập vào=============================")
        while True:
            studentName = input(f"Tên học sinh {dem}: ")
            id = input("ID: ")
            semester = input("Kỳ học: ")
            courseName = input("Tên khóa học: ")

            if courseName not in list_courseName:
                print("Hiện không có khóa học của bạn")
                continue
            POO21.Students(id, studentName, semester, courseName).create()
            print("-------------------------------------------------------------")
            dem += 1
            if dem > 3:
                print("Bạn có muốn nhập tiếp")
                sel2 = input("1.yes\n2.no  ")
                if sel2 == "yes" or sel2 == "y" or sel2 == "1":
                    continue
                elif sel2 == "no" or sel2 == "n" or sel2 == "2":
                    break
                else:
                    break
    elif sel1=="2":
        POO21.Students.find_and_sort("find")
    elif sel1=="3":
        POO21.Students.upgrade_delete("update")
    elif sel1=="4":
        POO21.Students.report("report")
    else:
        exit()
