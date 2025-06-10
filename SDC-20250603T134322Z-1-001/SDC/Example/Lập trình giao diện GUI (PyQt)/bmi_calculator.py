import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tính chỉ số BMI")
        self.setGeometry(800, 400, 350, 300)
        self.setup_ui()

    def setup_ui(self):
        label_style = "font-size: 16px; font-weight: bold; color: #333;"
        input_style = "font-size: 16px; padding: 8px; border: 1px solid #ccc; border-radius: 5px;"

        self.height_label = QLabel("Chiều cao (m):")
        self.height_label.setStyleSheet(label_style)
        self.height_input = QLineEdit()
        self.height_input.setStyleSheet(input_style)
        self.height_input.setFixedHeight(40)

        self.weight_label = QLabel("Cân nặng (kg):")
        self.weight_label.setStyleSheet(label_style)
        self.weight_input = QLineEdit()
        self.weight_input.setStyleSheet(input_style)
        self.weight_input.setFixedHeight(40)

        self.result_label = QLabel("Chỉ số BMI: ")
        self.result_label.setStyleSheet("font-size: 16px; color: #555;")

        self.category_label = QLabel("Đánh giá cơ thể: ")
        self.category_label.setStyleSheet("font-size: 16px; color: #555;")

        self.color_circle = QLabel()
        self.color_circle.setFixedSize(30, 30)
        self.color_circle.setStyleSheet("background-color: #f0f0f0; border-radius: 15px;")

        self.calc_button = QPushButton("Tính BMI")
        self.calc_button.clicked.connect(self.calculate_bmi)
        self.calc_button.setStyleSheet("""
            QPushButton {
                background-color: #1E90FF;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px 20px;
                border-radius: 5px;
                border: none;
                outline: none;
            }
            QPushButton:hover {
                background-color: #4682B4;
            }
        """)
        self.calc_button.setFixedHeight(40)

        category_layout = QHBoxLayout()
        category_layout.addWidget(self.category_label)
        category_layout.addWidget(self.color_circle)
        category_layout.setAlignment(Qt.AlignLeft)

        layout = QVBoxLayout()
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.calc_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.result_label, alignment=Qt.AlignLeft)
        layout.addLayout(category_layout)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        self.setLayout(layout)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())
            if height <= 0:
                raise ValueError("Chiều cao không hợp lệ.")
            
            bmi = weight / (height ** 2)
            category = self.get_bmi_category(bmi)
            self.result_label.setText(f"Chỉ số BMI: {bmi:.2f}")
            self.category_label.setText(f"Đánh giá cơ thể: {category}")

            color = self.get_bmi_color(bmi)
            self.color_circle.setStyleSheet(f"background-color: {color}; border-radius: 15px;")
            
        except ValueError:
            self.result_label.setText("Dữ liệu không hợp lệ!")
            self.category_label.setText("Đánh giá cơ thể: ")
            self.color_circle.setStyleSheet("background-color: #f0f0f0; border-radius: 15px;")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Gầy (Underweight)"
        elif 18.5 <= bmi < 25:
            return "Bình thường (Healthy)"
        elif 25 <= bmi < 30:
            return "Thừa cân (Overweight)"
        elif 30 <= bmi < 35:
            return "Béo phì (Obese)"
        else:
            return "Béo phì nghiêm trọng (Extremely Obese)"

    def get_bmi_color(self, bmi):
        if bmi < 18.5:
            return "#59c8f3"  # (Underweight)
        elif 18.5 <= bmi < 25:
            return "#03b306"  # (Healthy)
        elif 25 <= bmi < 30:
            return "#f9f807"  # (Overweight)
        elif 30 <= bmi < 35:
            return "#f77908"  # (Obese)"
        else:
            return "#f10102"  # (Extremely Obese)"

if __name__ == "__main__":1
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec_())