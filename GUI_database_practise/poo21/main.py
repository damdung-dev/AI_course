import sys
import pyodbc

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic.Compiler.qtproxies import QtWidgets

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
        self.Home.reportbtn.clicked.connect(self.showReportStudent)

    def showCreateStudentGUI(self):
        self.CreateStudent=CreateStudent()
        self.CreateStudent.setupUi(self)

    def showFindSortStudentGUI(self):
        self.FindAndSort=FindAndSort()
        self.FindAndSort.setupUi(self)

    def showUpdateStudentGUI(self):
        self.Update = Update()
        self.Update.setupUi(self)
    def showReportStudent(self):
        server = 'DESKTOP-PICVBQP\SQLEXPRESS'
        database = 'STUDENTSMANAGEMENT'
        try:
            conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                                  f'SERVER={server};'
                                  f'DATABASE={database};'
                                  f'Trusted_Connection=yes;')
            cursor = conn.cursor()
            print("Connection established")
            cursor.execute('SELECT * FROM students')
            rows = cursor.fetchall()

            if not rows:
                self.display.setText("No student found.")
            else:
                result = ""
                for row in rows:
                    result += f"ID: {row[0]}\nName: {row[1]}\nSemester: {row[2]}\nCourse Name: {row[3]}\n"  # Sửa theo số cột thực tế của bạn
                QMessageBox.information(None, "Report", result)

        except pyodbc.IntegrityError as e:
            QtWidgets.QMessageBox.critical(None, "SQL Error", "Lỗi: ID bị trùng hoặc sai định dạng.\n" + str(e))
        except pyodbc.Error as e:
            QtWidgets.QMessageBox.critical(None, "SQL Error", str(e))
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Unexpected Error", str(e))
        finally:
            try:
                conn.close()
            except:
                pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui=MainWindow()
    ui.show()
    sys.exit(app.exec_())