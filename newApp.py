import sys
import json
from functools import partial
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QTableWidget,
    QTableWidgetItem, QComboBox, QHeaderView, QFileDialog, QLineEdit, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont , QIcon
from datetime import datetime
from collections import defaultdict
from redirect import ExpenseTracker
from PurchaseLayout import Ui_MainWindow
class ExpenseTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize your UI setup here
        self.setWindowTitle("Expense Tracker")
        self.setWindowIcon(QIcon("C:/Users/TM/Desktop/logo.ico"))

        # Initialize currency symbol and budget limit
        self.currency_symbol = "$"  # Default currency is USD
        self.budget_limit = 0.00  # Default budget limit

        # Load expenses from JSON
        self.expenses, self.total_amount = self.load_expenses()

        # Set up the main window
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(650, 300, 700, 600)

        # Set layout and initialize sections
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create sections
        self.create_total_section()
        self.create_budget_section()
        self.create_currency_section()
        self.create_recent_purchases_section()
        self.create_add_expense_section()
        self.create_view_report_button()

    def create_total_section(self):
        # Total spend label
        self.total_label = QLabel(f"Total Spend\n{self.currency_symbol}{self.total_amount:.2f}")
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

    def create_budget_section(self):
        # Budget layout
        budget_layout = QHBoxLayout()

        # Budget input
        self.budget_input = QLineEdit()
        self.budget_input.setPlaceholderText("Set Budget Limit")
        self.budget_input.setFont(QFont("Arial", 14))
        self.budget_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #87CEEB;
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
            }
        """)
        budget_layout.addWidget(self.budget_input)

        # Set Budget button
        self.set_budget_button = QPushButton("Set Budget")
        self.set_budget_button.setFont(QFont("Arial", 14))
        self.set_budget_button.setStyleSheet("""
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
        self.set_budget_button.clicked.connect(self.set_budget_limit)
        budget_layout.addWidget(self.set_budget_button)

        self.layout.addLayout(budget_layout)

        # Budget status label
        self.budget_status_label = QLabel("")
        self.budget_status_label.setAlignment(Qt.AlignCenter)
        self.budget_status_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.layout.addWidget(self.budget_status_label)

        self.update_budget_status()

    def set_budget_limit(self):
        try:
            self.budget_limit = float(self.budget_input.text())
            self.update_budget_status()
        except ValueError:
            self.budget_status_label.setText("Invalid budget amount.")
            self.budget_status_label.setStyleSheet("color: red;")

    def update_budget_status(self):
        if self.budget_limit > 0:
            remaining_budget = self.budget_limit - self.total_amount
            if remaining_budget >= 0:
                self.budget_status_label.setText(f"Remaining Budget: {self.currency_symbol}{remaining_budget:.2f}")
                self.budget_status_label.setStyleSheet("color: green;")
            else:
                self.budget_status_label.setText(f"Over Budget: {self.currency_symbol}{remaining_budget:.2f}")
                self.budget_status_label.setStyleSheet("color: red;")
        else:
            self.budget_status_label.setText("No budget set.")
            self.budget_status_label.setStyleSheet("color: black;")

    def create_currency_section(self):
        # Currency selector
        self.currency_selector = QComboBox()
        self.currency_selector.addItems(["USD ($)", "EUR (€)", "EGP (£)", "SAR (رس)"])  # Add options for currencies
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
        self.expense_table = QTableWidget(len(self.expenses), 4)  # 3 columns: Description, Amount, Category
        self.expense_table.setHorizontalHeaderLabels(["Description", "Amount", "Category", "Action"])

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

        # Populate table with the expenses
        for row, expense in enumerate(self.expenses):
            self.expense_table.setItem(row, 0, QTableWidgetItem(expense['description']))
            self.expense_table.setItem(row, 1, QTableWidgetItem(str(expense['amount'])))
            self.expense_table.setItem(row, 2, QTableWidgetItem(expense['category']))
            
            remove_button = QPushButton("Remove")
    # Connect the button to a method, passing the row index
            remove_button.clicked.connect(partial(self.remove_expense, row))
        self.layout.addWidget(self.expense_table)

    def remove_expense(self, row):
        del self.expenses[row]  # Remove the expense from the data source
        self.populate_table()   # Refresh the table

    def refresh_table(self):
        self.expense_table.setRowCount(len(self.expenses))  # Update row count
        for row, expense in enumerate(self.expenses):
            self.expense_table.setItem(row, 0, QTableWidgetItem(expense['description']))
            self.expense_table.setItem(row, 1, QTableWidgetItem(f"{self.currency_symbol}{expense['amount']:.2f}"))
            self.expense_table.setItem(row, 2, QTableWidgetItem(expense['category']))


    def create_add_expense_section(self):
        # Add button only
        self.add_button = QPushButton("Add Expense")
        self.add_button.setFont(QFont("Arial", 18, QFont.Bold))  # Larger font for emphasis
        self.add_button.setStyleSheet("""
            QPushButton {
                background-color: #4682B4;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 15px;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #5F9EA0;
            }
        """)
        self.add_button.setMinimumHeight(60)  # Increase button height
        self.add_button.clicked.connect(self.openExpenseAdd)  # Placeholder functionality
        self.layout.addWidget(self.add_button)

    def openExpenseAdd(self):
        # Open the purchase layout
        self.purchase = QMainWindow()
        self.ui = Ui_MainWindow(self)
        self.ui.setupUi(self.purchase)
        self.purchase.show()
        self.hide()

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

        # Open report window and pass self as the main window
        self.report_window = ReportPage(current_month_total, highest_day, last_month_total, self.expenses, self.currency_symbol, self)
        self.report_window.show()
        self.hide()  # Hide the current window (Expense Tracker) when opening the report page



    def update_currency(self):
        # Update currency symbol and total display
        currency_text = self.currency_selector.currentText()
        if "USD" in currency_text:
            self.currency_symbol = "$"
        elif "EUR" in currency_text:
            self.currency_symbol = "\u20ac"
        elif "EGP" in currency_text:
            self.currency_symbol = "\u00a3"
        elif "SAR" in currency_text:
            self.currency_symbol = "رس"

        self.total_label.setText(f"Total Spend\n{self.currency_symbol}{self.total_amount:.2f}")
        self.update_budget_status()

    def calculate_report_data(self):
        current_month_total = self.total_amount
        last_month_total = self.total_amount * 0.9  # Placeholder for last month's spend

        # Calculate highest spending day
        daily_totals = defaultdict(float)
        for expense in self.expenses:
            daily_totals[expense['date']] += expense['amount']

        highest_day = max(daily_totals, key=daily_totals.get, default="N/A")
        return current_month_total, highest_day, last_month_total

    def save_expenses(self):
        data = {
            "currency_symbol": self.currency_symbol,
            "total_amount": self.total_amount,
            "expenses": self.expenses,
            "budget_limit": self.budget_limit
        }

        # Open the file for writing and save data in JSON format
        with open('expenses.json', 'w') as file:
            json.dump(data, file, indent=4)

    def load_expenses(self):
        try:
            # Attempt to load data from the saved JSON file
            with open('expenses.json', 'r') as file:
                data = json.load(file)
                self.currency_symbol = data.get("currency_symbol", "$")
                self.total_amount = data.get("total_amount", 0.00)
                self.budget_limit = data.get("budget_limit", 0.00)
                expenses = data.get("expenses", [])
                return expenses, self.total_amount
        except (FileNotFoundError, json.JSONDecodeError):
            # If file doesn't exist or there's an error loading, return default values
            return [], 0.00


class ReportPage(QMainWindow):
    def __init__(self, current_month_spent, highest_day, last_month_spent, expenses, currency_symbol, main_window):
        super().__init__()

        self.expenses = expenses
        self.currency_symbol = currency_symbol
        self.main_window = main_window  # Reference to the main window

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

        self.monthly_spent_label = QLabel(f"Current Month Spend: {self.currency_symbol}{current_month_spent:.2f}")
        self.monthly_spent_label.setAlignment(Qt.AlignCenter)
        self.monthly_spent_label.setFont(QFont("Arial", 18))
        self.layout.addWidget(self.monthly_spent_label)

        self.highest_day_label = QLabel(f"Highest Day of Spending: {highest_day}")
        self.highest_day_label.setAlignment(Qt.AlignCenter)
        self.highest_day_label.setFont(QFont("Arial", 18))
        self.layout.addWidget(self.highest_day_label)

        self.download_button = QPushButton("Download Report")
        self.download_button.setFont(QFont("Arial", 14))
        self.download_button.setStyleSheet("""
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
        self.download_button.clicked.connect(self.download_report)
        self.layout.addWidget(self.download_button)

        # Add Return to Tracker button
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
        self.main_window.show()  # Show the ExpenseTracker window
        self.close()  # Close the ReportPage


    def download_report(self):
    # Generate and download a report as plain text
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Report", "", "Text Files (*.txt)")
        if file_name:
            # Prepare report data
            report_data = [
                f"Current Month Spend: {self.monthly_spent_label.text()}",
                f"Highest Day of Spending: {self.highest_day_label.text()}",
                "Expenses:"
            ]
        
        # Add expense details
            for expense in self.expenses:
                expense_line = f"  - Description: {expense['description']}, Amount: {expense['amount']}, Category: {expense['category']}"
                report_data.append(expense_line)
            
            # Join the report data into a single text string
            report_text = "\n".join(report_data)
            
            # Write the report to the file
            with open(file_name, 'w') as file:
                file.write(report_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ExpenseTracker()
    main_window.show()
    sys.exit(app.exec_())
