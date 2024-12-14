import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QComboBox,
    QGridLayout, QHeaderView
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 800, 600)

        # Main layout and central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Total amount display
        self.total_label = QLabel("Total: $0.00")
        self.total_label.setAlignment(Qt.AlignCenter)
        total_font = QFont("Times New Roman", 18, QFont.Bold)
        total_font.setItalic(True)
        self.total_label.setFont(total_font)
        self.total_label.setStyleSheet("""
            background-color: #1E90FF;  /* Dodger Blue */
            color: white;
            padding: 10px;
            border-radius: 10px;
            font-size: 18px;
        """)
        self.layout.addWidget(self.total_label)

        # Input section and expense table
        self.create_input_section()
        self.create_expense_table()

        # Initialize expense data
        self.expenses = []
        self.total_amount = 0.0

    def create_input_section(self):
        input_layout = QGridLayout()

        # Description input
        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Enter description")
        self.description_input.setFont(QFont("Arial", 14))
        self.description_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #87CEEB;  /* Sky Blue */
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
                background-color: #E0FFFF;  /* Light Cyan */
            }
        """)
        input_layout.addWidget(self.description_input, 0, 0, 1, 2)

        # Amount input
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount")
        self.amount_input.setFont(QFont("Arial", 14))
        self.amount_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #87CEEB;  /* Sky Blue */
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
                background-color: #E0FFFF;  /* Light Cyan */
            }
        """)
        input_layout.addWidget(self.amount_input, 0, 2, 1, 2)

        # Category selection
        self.category_input = QComboBox()
        self.category_input.addItems(["Select...","Food", "Transportation", "Entertainment", "Bills", "Other"])
        self.category_input.setFont(QFont("Arial", 14))
        self.category_input.setStyleSheet("""
            QComboBox {
                border: 2px solid #87CEEB;  /* Sky Blue */
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
                background-color: #E0FFFF;  /* Light Cyan */
            }
        """)
        input_layout.addWidget(self.category_input, 0, 4, 1, 2)

        # Add button
        self.add_button = QPushButton("Add Expense")
        self.add_button.setFont(QFont("Arial", 14))
        self.add_button.setStyleSheet("""
            QPushButton {
                background-color:rgb(142, 173, 199);  /* Steel Blue */
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #5F9EA0;  /* Cadet Blue */
            }
        """)
        self.add_button.clicked.connect(self.add_expense)
        input_layout.addWidget(self.add_button, 0, 6, 1, 1)

        self.layout.addLayout(input_layout)

    def create_expense_table(self):
        # Create table
        self.expense_table = QTableWidget(0, 4)  # 4 columns: Description, Amount, Category, Remove
        self.expense_table.setHorizontalHeaderLabels(["Description", "Amount", "Category", "Remove"])

        # Customize headers
        self.expense_table.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #1E90FF;  /* Dodger Blue */
                color: white;
                font-size: 16px;
                font-weight: bold;
                border: 1px solid #4682B4;
                border-radius: 5px;
                padding: 5px;
            }
        """)

        # Stretch first column, set fixed sizes for others
        self.expense_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)  # Description column
        for col in range(1, 4):  # Fixed widths for Amount, Category, Remove
            self.expense_table.setColumnWidth(col, 150)

        self.expense_table.setAlternatingRowColors(True)
        self.expense_table.setStyleSheet("""
            QTableWidget {
                background-color: #E0FFFF;  /* Light Cyan */
                alternate-background-color: #B0E0E6;  /* Powder Blue */
                gridline-color: #87CEEB;  /* Sky Blue */
            }
        """)

        self.layout.addWidget(self.expense_table)

    def add_expense(self):
        description = self.description_input.text()
        amount_text = self.amount_input.text()
        category = self.category_input.currentText()

        if not description or not amount_text:
            self.amount_input.setPlaceholderText("All fields are required!")
            return

        try:
            amount = float(amount_text)
        except ValueError:
            self.amount_input.clear()
            self.amount_input.setPlaceholderText("Enter a valid number")
            return

        # Add expense to the table
        row_position = self.expense_table.rowCount()
        self.expense_table.insertRow(row_position)
        self.expense_table.setItem(row_position, 0, QTableWidgetItem(description))
        self.expense_table.setItem(row_position, 1, QTableWidgetItem(f"${amount:.2f}"))
        self.expense_table.setItem(row_position, 2, QTableWidgetItem(category))

        # Remove button
        remove_button = QPushButton("Remove")
        remove_button.setStyleSheet("""
            QPushButton {
                background-color: #4682B4;  /* Steel Blue */
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #5F9EA0;  /* Cadet Blue */
            }
        """)
        remove_button.clicked.connect(lambda _, row=row_position: self.remove_expense(row))
        self.expense_table.setCellWidget(row_position, 3, remove_button)

        # Update total amount
        self.expenses.append((description, amount, category))
        self.total_amount += amount
        self.total_label.setText(f"Total: ${self.total_amount:.2f}")

        # Clear input fields
        self.description_input.clear()
        self.amount_input.clear()

    def remove_expense(self, row):
        # Adjust for dynamic row deletion
        amount_text = self.expense_table.item(row, 1).text()
        amount = float(amount_text.replace("$", ""))

        self.expense_table.removeRow(row)
        self.total_amount -= amount
        self.total_label.setText(f"Total: ${self.total_amount:.2f}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    sys.exit(app.exec_())
