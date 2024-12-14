import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout
)
from PyQt5.QtCore import Qt

class ExpenseTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 1200, 800)

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Total amount display
        self.total_label = QLabel("Total: $0.00", self)
        self.total_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.total_label)

        # Input fields and button
        self.create_input_section()

        # Expense table
        self.create_expense_table()

        # Initialize expense data
        self.expenses = []
        self.total_amount = 0.0

    def create_input_section(self):
        input_layout = QHBoxLayout()

        self.description_input = QLineEdit(self)
        self.description_input.setPlaceholderText("Enter description")
        input_layout.addWidget(self.description_input)

        self.amount_input = QLineEdit(self)
        self.amount_input.setPlaceholderText("Enter amount")
        input_layout.addWidget(self.amount_input)

        self.add_button = QPushButton("Add Expense", self)
        self.add_button.clicked.connect(self.add_expense)
        input_layout.addWidget(self.add_button)

        self.layout.addLayout(input_layout)

    def create_expense_table(self):
        self.expense_table = QTableWidget(0, 2, self)
        self.expense_table.setHorizontalHeaderLabels(["Product", "Amount"])
        self.expense_table.horizontalHeader().setStretchLastSection(True)
        self.layout.addWidget(self.expense_table)

    def add_expense(self):
        description = self.description_input.text()
        amount_text = self.amount_input.text()

        if not description or not amount_text:
            return  # You cant an add empty entry

        try:
            amount = float(amount_text)
        except ValueError:
            self.amount_input.setText("")
            self.amount_input.setPlaceholderText("Enter a valid number")
            return

        # Add expense to the table
        row_position = self.expense_table.rowCount()
        self.expense_table.insertRow(row_position)
        self.expense_table.setItem(row_position, 0, QTableWidgetItem(description))
        self.expense_table.setItem(row_position, 1, QTableWidgetItem(f"${amount:.2f}"))

        # Update total amount
        self.expenses.append((description, amount))
        self.total_amount = amount
        self.total_label.setText(f"Total: ${self.total_amount:.2f}")

        # Clear input fields
        self.description_input.clear()
        self.amount_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout
)
from PyQt5.QtCore import Qt

class ExpenseTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 1200, 800)

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Total amount display
        self.total_label = QLabel("Total: $0.00", self)
        self.total_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.total_label)

        # Input fields and button
        self.create_input_section()

        # Expense table
        self.create_expense_table()

        # Initialize expense data
        self.expenses = []
        self.total_amount = 0.0

    def create_input_section(self):
        input_layout = QHBoxLayout()

        self.description_input = QLineEdit(self)
        self.description_input.setPlaceholderText("Enter description")
        input_layout.addWidget(self.description_input)

        self.amount_input = QLineEdit(self)
        self.amount_input.setPlaceholderText("Enter amount")
        input_layout.addWidget(self.amount_input)

        self.add_button = QPushButton("Add Expense", self)
        self.add_button.clicked.connect(self.add_expense)
        input_layout.addWidget(self.add_button)

        self.layout.addLayout(input_layout)

    def create_expense_table(self):
        self.expense_table = QTableWidget(0, 2, self)
        self.expense_table.setHorizontalHeaderLabels(["Description", "Amount"])
        self.expense_table.horizontalHeader().setStretchLastSection(True)
        self.layout.addWidget(self.expense_table)

    def add_expense(self):
        description = self.description_input.text()
        amount_text = self.amount_input.text()

        if not description or not amount_text:
            return  # Don't add empty entries

        try:
            amount = float(amount_text)
        except ValueError:
            self.amount_input.setText("")
            self.amount_input.setPlaceholderText("Enter a valid number")
            return

        # Add expense to the table
        row_position = self.expense_table.rowCount()
        self.expense_table.insertRow(row_position)
        self.expense_table.setItem(row_position, 0, QTableWidgetItem(description))
        self.expense_table.setItem(row_position, 1, QTableWidgetItem(f"${amount:.2f}"))

        # Update total amount
        self.expenses.append((description, amount))
        self.total_amount = amount + 200
        self.total_label.setText(f"Total: ${self.total_amount:.2f}")

        # Clear input fields
        self.description_input.clear()
        self.amount_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    sys.exit(app.exec_())
