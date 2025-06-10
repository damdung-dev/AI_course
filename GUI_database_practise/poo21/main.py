import sys
import pyodbc

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMainWindow


from create_student import CreateStudent
from home import Home
from find_sort import FindAndSort
from update import Update

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Home = Home()
        self.Home.setupUi(self)
        self.Home.createbtn.clicked.connect(self.showCreateStudentGUI)
        self.Home.findSortbtn.clicked.connect(self.showFindSortStudentGUI)
        self.Home.updatebtn.clicked.connect(self.showUpdateStudentGUI)

    def showCreateStudentGUI(self):
        self.CreateStudent=CreateStudent()
        self.CreateStudent.setupUi(self)

    def showFindSortStudentGUI(self):
        self.FindAndSort=FindAndSort()
        self.FindAndSort.setupUi(self)

    def showUpdateStudentGUI(self):
        self.Update = Update()
        self.Update.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui=MainWindow()
    ui.show()
    sys.exit(app.exec_())