import sys
import json
from functools import partial
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QTableWidget,
    QTableWidgetItem, QComboBox, QHeaderView, QFileDialog, QLineEdit, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from datetime import datetime
from collections import defaultdict

# Mock SavedData Module for Demo
class SavedData:
    @staticmethod
    def load_data():
        return [
            ["Groceries", 100.0, "Food", "2024-12-01"],
            ["Rent", 1200.0, "Housing", "2024-12-01"],
            ["Utilities", 200.0, "Bills", "2024-12-02"]
        ]

    @staticmethod
    def save_data(expenses):
        with open("expenses.json", "w") as f:
            json.dump(expenses, f)

# Report Page Class
class ReportPage(QMainWindow):
    def __init__(self, current_month_spent, highest_day, last_month_spent, expenses, currency_symbol, main_window):
        super().__init__()
        self.expenses = expenses
        self.currency_symbol = currency_symbol
        self.main_window = main_window
        self.setWindowTitle("Expense Report")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Title
        self.title_label = QLabel("Expense Report")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.layout.addWidget(self.title_label)

        # Current Month Spending
        self.monthly_spent_label = QLabel(f"Current Month Spend: {self.currency_symbol}{current_month_spent:.2f}")
        self.monthly_spent_label.setAlignment(Qt.AlignCenter)
        self.monthly_spent_label.setFont(QFont("Arial", 18))
        self.layout.addWidget(self.monthly_spent_label)

        # Highest Day
        self.highest_day_label = QLabel(f"Highest Day of Spending: {highest_day}")
        self.highest_day_label.setAlignment(Qt.AlignCenter)
        self.highest_day_label.setFont(QFont("Arial", 18))
        self.layout.addWidget(self.highest_day_label)

        # Download Report Button
        self.download_button = QPushButton("Download Report")
        self.download_button.setFont(QFont("Arial", 14))
        self.download_button.clicked.connect(self.download_report)
        self.layout.addWidget(self.download_button)

        # Return to Tracker Button
        self.return_button = QPushButton("Return to Tracker")
        self.return_button.setFont(QFont("Arial", 14))
        self.return_button.clicked.connect(self.return_to_tracker)
        self.layout.addWidget(self.return_button)

    def return_to_tracker(self):
        self.main_window.show()
        self.close()

    def download_report(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Report", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, "w") as file:
                report = f"Current Month Spend: {self.monthly_spent_label.text()}\n" \
                         f"Highest Day of Spending: {self.highest_day_label.text()}\nExpenses:\n"
                for expense in self.expenses:
                    report += f"- {expense[0]}: {self.currency_symbol}{expense[1]:.2f}, {expense[2]}, {expense[3]}\n"
                file.write(report)