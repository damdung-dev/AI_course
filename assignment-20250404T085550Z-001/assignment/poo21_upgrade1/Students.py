class Students:
    #Attributes:
    list_studentName = []
    list_id = []
    list_semester = []
    listcourseName_input = []
    count=0
    #Constructor:
    def __init__(self, ID, studentName, Semester, courseName):
        self.__student_name=studentName
        self.__semester=Semester
        self.__course_name=courseName
        Students.count += 1
        self.__id = Students.count
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, ID):
        self.__id = ID

    @property
    def student_name(self):
        return self.__student_name

    @student_name.setter
    def student_name(self, studentName):
        self.__student_name = studentName

    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, Semester):
        self.__semester = Semester

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, courseName):
        self.__course_name = courseName
