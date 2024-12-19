import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QComboBox, QGridLayout, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from datetime import datetime
from collections import defaultdict


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize currency symbol
        self.currency_symbol = "$"  # Default currency is USD

        # Set up the main window
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(650, 300, 700, 500)

        # Set layout and initialize sections
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create sections
        self.create_total_section()
        self.create_currency_section()
        self.create_recent_purchases_section()
        self.create_add_expense_section()
        self.create_view_report_button()

        # Initialize expense data
        self.expenses = []  # Store expenses as tuples (description, amount, category, date)
        self.total_amount = 0.0

    def create_total_section(self):
        # Total spend label
        self.total_label = QLabel(f"Total Spend\n{self.currency_symbol}0.00")
        self.total_label.setAlignment(Qt.AlignCenter)
        total_font = QFont("Arial", 22, QFont.Bold)
        self.total_label.setFont(total_font)
        self.total_label.setStyleSheet("""
            background-color: #1E90FF;  /* Dodger Blue */
            color: white;
            padding: 20px;
            border-radius: 15px;
        """)
        self.layout.addWidget(self.total_label)

    def create_currency_section(self):
        # Currency selector
        self.currency_selector = QComboBox()
        self.currency_selector.addItems(["USD ($)", "EUR (€)", "EGP (£)"])  # Add options for currencies
        self.currency_selector.setFont(QFont("Arial", 14))
        self.currency_selector.setStyleSheet("""
            QComboBox {
                border: 2px solid #87CEEB;
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
                background-color: #E0FFFF;
            }
        """)
        self.currency_selector.currentIndexChanged.connect(self.update_currency)
        self.layout.addWidget(self.currency_selector)

    def create_recent_purchases_section(self):
        # Recent purchases label
        self.recent_purchases_label = QLabel("Recent Purchases")
        self.recent_purchases_label.setAlignment(Qt.AlignLeft)
        self.recent_purchases_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.layout.addWidget(self.recent_purchases_label)

        # Create table for recent purchases
        self.expense_table = QTableWidget(0, 3)  # 3 columns: Description, Amount, Category
        self.expense_table.setHorizontalHeaderLabels(["Description", "Amount", "Category"])

        # Customize headers
        self.expense_table.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #1E90FF;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 5px;
            }
        """)
        self.expense_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)  # Stretch description
        self.expense_table.setStyleSheet("""
            QTableWidget {
                background-color: #F0F8FF;
                alternate-background-color: #E6E6FA;
                gridline-color: #ADD8E6;
            }
        """)
        self.layout.addWidget(self.expense_table)

    def create_add_expense_section(self):
        input_layout = QGridLayout()

        # Description input
        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Enter description")
        self.description_input.setFont(QFont("Arial", 14))
        self.description_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #87CEEB;
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
                background-color: #E0FFFF;
            }
        """)
        input_layout.addWidget(self.description_input, 0, 0, 1, 2)

        # Amount input
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount")
        self.amount_input.setFont(QFont("Arial", 14))
        self.amount_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #87CEEB;
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
                background-color: #E0FFFF;
            }
        """)
        input_layout.addWidget(self.amount_input, 0, 2, 1, 2)

        # Category selection
        self.category_input = QComboBox()
        self.category_input.addItems(["Select...", "Food", "Transportation", "Entertainment", "Bills", "Other"])
        self.category_input.setFont(QFont("Arial", 14))
        self.category_input.setStyleSheet("""
            QComboBox {
                border: 2px solid #87CEEB;
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
                background-color: #E0FFFF;
            }
        """)
        input_layout.addWidget(self.category_input, 0, 4, 1, 2)

        # Add button
        self.add_button = QPushButton("Add Expense")
        self.add_button.setFont(QFont("Arial", 14))
        self.add_button.setStyleSheet("""
            QPushButton {
                background-color: #4682B4;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #5F9EA0;
            }
        """)
        self.add_button.clicked.connect(self.add_expense)
        input_layout.addWidget(self.add_button, 0, 6, 1, 1)

        self.layout.addLayout(input_layout)

    def add_expense(self):
        description = self.description_input.text()
        amount_text = self.amount_input.text()
        category = self.category_input.currentText()

        if not description or not amount_text or category == "Select...":
            self.amount_input.setPlaceholderText("All fields are required!")
            return

        try:
            amount = float(amount_text)
        except ValueError:
            self.amount_input.clear()
            self.amount_input.setPlaceholderText("Enter a valid number")
            return

        # Get the current date
        current_date = datetime.now().strftime("%Y-%m-%d")

        # Add expense to the table
        row_position = self.expense_table.rowCount()
        self.expense_table.insertRow(row_position)
        self.expense_table.setItem(row_position, 0, QTableWidgetItem(description))
        self.expense_table.setItem(row_position, 1, QTableWidgetItem(f"{self.currency_symbol}{amount:.2f}"))
        self.expense_table.setItem(row_position, 2, QTableWidgetItem(category))

        # Store expense in the list with the date
        self.expenses.append((description, amount, category, current_date))
        self.total_amount += amount
        self.total_label.setText(f"Total Spend\n{self.currency_symbol}{self.total_amount:.2f}")

        # Clear input fields
        self.description_input.clear()
        self.amount_input.clear()

    def create_view_report_button(self):
        # Create button to open the report page
        self.view_report_button = QPushButton("View Report")
        self.view_report_button.setFont(QFont("Arial", 14))
        self.view_report_button.setStyleSheet("""
            QPushButton {
                background-color: #4682B4;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #5F9EA0;
            }
        """)
        self.view_report_button.clicked.connect(self.open_report)
        self.layout.addWidget(self.view_report_button)

    def open_report(self):
        # Fetch data for the report page
        current_month_total, highest_day, last_month_total = self.calculate_report_data()

        # Open report window
        self.report_window = ReportPage(current_month_total, highest_day, last_month_total)
        self.report_window.show()
        self.hide()  # Hide the current window (Expense Tracker) when opening the report page

    def update_currency(self):
        currency_text = self.currency_selector.currentText()
        if "USD" in currency_text:
            self.currency_symbol = "$"
        elif "EUR" in currency_text:
            self.currency_symbol = "\u20ac"
        elif "EGP" in currency_text:
            self.currency_symbol = "\u00a3"

        # Update total label with new currency symbol
        self.total_label.setText(f"Total Spend\n{self.currency_symbol}{self.total_amount:.2f}")

    def calculate_report_data(self):
        current_month_total = self.total_amount
        last_month_total = self.total_amount * 0.9  # Placeholder for last month's spend

        # Calculate highest spending day
        daily_totals = defaultdict(float)
        for _, amount, _, date in self.expenses:
            daily_totals[date] += amount

        if daily_totals:
            highest_day = max(daily_totals, key=daily_totals.get)
        else:
            highest_day = "N/A"  # Handle case where no expenses exist

        return current_month_total, highest_day, last_month_total


class ReportPage(QMainWindow):
    def __init__(self, current_month_spent, highest_day, last_month_spent):
        super().__init__()

        self.setWindowTitle("Expense Report")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.title_label = QLabel("Expense Report")
        self.title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont("Arial", 24, QFont.Bold)
        self.title_label.setFont(title_font)
        self.layout.addWidget(self.title_label)

        self.monthly_spent_label = QLabel(f"Current Month Spend: ${current_month_spent:.2f}")
        self.monthly_spent_label.setAlignment(Qt.AlignCenter)
        self.monthly_spent_label.setFont(QFont("Arial", 18))
        self.layout.addWidget(self.monthly_spent_label)

        self.compare_spent_label = QLabel(f"Last Month Spend: ${last_month_spent:.2f}")
        self.compare_spent_label.setAlignment(Qt.AlignCenter)
        self.compare_spent_label.setFont(QFont("Arial", 18))
        self.layout.addWidget(self.compare_spent_label)

        self.highest_day_label = QLabel(f"Highest Day of Spending: {highest_day}")
        self.highest_day_label.setAlignment(Qt.AlignCenter)
        self.highest_day_label.setFont(QFont("Arial", 18))
        self.layout.addWidget(self.highest_day_label)

        self.return_button = QPushButton("Return to Tracker")
        self.return_button.setFont(QFont("Arial", 14))
        self.return_button.setStyleSheet("""
            QPushButton {
                background-color: #4682B4;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #5F9EA0;
            }
        """)
        self.return_button.clicked.connect(self.return_to_tracker)
        self.layout.addWidget(self.return_button)

    def return_to_tracker(self):
        self.close()  # Close the ReportPage window
        self.main_window = ExpenseTracker()
        self.main_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    sys.exit(app.exec_())
