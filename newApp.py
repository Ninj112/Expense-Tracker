import sys
from functools import partial
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QTableWidget,
    QTableWidgetItem, QComboBox, QHeaderView, QFileDialog, QLineEdit, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont , QIcon
from collections import defaultdict
import Report
import SavedData


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
            # Calculate the total amount spent
            # amount = sum(float(expense[1]) for expense in self.expenses if isinstance(expense[1], (int, float, str)) and str(expense[1]).replace('.', '', 1).isdigit())
            amount = 0 
            for array in self.expenses:
                amount += array[1]

            # Save the calculated total amount
            self.total_amount = amount

            # Create and style the total label
            self.total_label = QLabel(f"Total Spend\n{self.currency_symbol}{amount:.2f}")
            self.total_label.setAlignment(Qt.AlignCenter)
            total_font = QFont("Arial", 22, QFont.Bold)
            self.total_label.setFont(total_font)
            self.total_label.setStyleSheet("""
                background-color: #1E90FF;
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
        from AccountLayout import Ui_MainWindow
        self.Account = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.Account)
        self.Account.showMaximized()
        self.close()
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
        self.expense_table = QTableWidget(len(self.expenses), 4)  # 4 columns: Description, Amount, Category, Action
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
            self.expense_table.setItem(row, 0, QTableWidgetItem(str(expense[0])))  # Description
            self.expense_table.setItem(row, 1, QTableWidgetItem(str(expense[1])))  # Amount
            self.expense_table.setItem(row, 2, QTableWidgetItem(str(expense[3])))  # Category
            
            # Add remove button
            remove_button = QPushButton("Remove")
            remove_button.clicked.connect(partial(self.remove_expense, row))
            self.expense_table.setCellWidget(row, 3, remove_button)

        self.layout.addWidget(self.expense_table)


    def remove_expense(self, row):
        
        
        if 0 <= row < len(self.expenses):
            del self.expenses[row]  # Remove from in-memory list
            
            amount = 0 
            for array in self.expenses:
                amount += array[1]
        

            # Save the calculated total amount
            self.total_amount = amount
            
            self.total_label.setText((f"Total Spend\n{self.currency_symbol}{amount:.2f}"))
            
            
            self.update_budget_status()
            # Save updated expenses to the file
            SavedData.save_data(self.expenses)
            
            # Refresh the table to reflect the updated data
            self.refresh_table()


    def refresh_table(self):
        self.expense_table.setRowCount(len(self.expenses))  # Update row count
        for row, expense in enumerate(self.expenses):
            self.expense_table.setItem(row, 0, QTableWidgetItem(expense[0]))
            self.expense_table.setItem(row, 1, QTableWidgetItem(str(expense[2])))
            self.expense_table.setItem(row, 2, QTableWidgetItem(expense[3]))


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
        self.close()

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
            daily_totals[expense[3]] += expense[1]

        highest_day = max(daily_totals, key=daily_totals.get, default="N/A")
        return current_month_total, highest_day, last_month_total



    def load_expenses(self):
        expenses = SavedData.load_data()
        userDataList = SavedData.load_user_data()
        self.currency_symbol = "$"

        self.total_amount = 0
        self.budget_limit = userDataList[2]
        return expenses, self.total_amount

    def open_report(self):
        current_month_total, highest_day, last_month_total = self.calculate_report_data()
        print(current_month_total)
        print(highest_day)
        print(last_month_total)

        self.report_window = Report.ReportPage(current_month_total, highest_day, last_month_total, self.expenses, self.currency_symbol, self)
        self.report_window.showMaximized()
        self.hide()


    def openExpenseAdd(self):
        # Local import to avoid circular dependency
        from PurchaseLayout import Ui_MainWindow
        self.purchase = QMainWindow()
        self.ui = Ui_MainWindow(self)
        self.ui.setupUi(self.purchase)
        self.purchase.showMaximized()
        self.close()

# ------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ExpenseTracker()
    main_window.show()
    main_window.showMaximized()
    sys.exit(app.exec_())
