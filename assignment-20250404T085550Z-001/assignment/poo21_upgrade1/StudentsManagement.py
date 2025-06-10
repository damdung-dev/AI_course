class StudentManagement:
  # Attributes: students[]
  # Constructor
  def __init__(self):
    self.__students = []
  # getters/ setters
  @property
  def students(self):
    return self.__students
  @students.setter
  def students(self, Students):
    self.__students = Students
  # Method
  def create(self):
    # create student
    print(f"Please input information of student: ")
    name     = input("\t- Input name: ")
    semester = int(input("\t- Input semester: "))
    course   = input("\t- Input course: ")
    s        = Student(name, semester, course)
    # insert student
    self.__students.append(s)
  def checkID(self, ID):
    return ID in [ x.__ID for x in self.__students ]
  def report(self):
    print("ID        |Name      |Semester  |Course")
    print(f"-"*40)
    for x in self.__students:
      print(x)
  def delete(self,ID):
    user_id=input("Please input student ID: ")
    if checkID(user_id)==True:
      system=input("Do you want to delete this student ID?\n1. Yes    2. No \nYour choice:")
      self.__students.remove(user_id)
    else:

  def run(self):
    while(True):
      print(f"WELCOME TO STUDENT MANAGEMENT")
      print(f"1.	Create")
      print(f"2.	Find and Sort")
      print(f"3.	Update/Delete")
      print(f"4.	Report")
      print(f"5.	Exit")
      print("Please choose 1 to Create, 2 to Find and Sort, 3 to Update/Delete, 4 to Report and 5 to Exit program")
      n = int(input("n: "))
      if n == 1:
        self.create()
      elif n == 2:
        self.find()
      elif n==4:
        self.report()
      elif n==5:
        break
