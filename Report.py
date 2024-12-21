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
    main_window = ReportPage()
    main_window.show()
    main_window.showFullScreen()
    sys.exit(app.exec_())
