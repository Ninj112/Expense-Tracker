from PyQt5 import QtCore, QtGui, QtWidgets

import SavedData
from newApp import ExpenseTracker


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(200, 50))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.navBar = QtWidgets.QFrame(self.centralwidget)
        self.navBar.setMinimumSize(QtCore.QSize(0, 50))
        self.navBar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.navBar.setStyleSheet("background-color: rgb(85, 85, 255)")
        self.navBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navBar.setObjectName("navBar")
        self.verticalLayout.addWidget(self.navBar)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.HeadTitle = QtWidgets.QLabel(self.centralwidget)
        self.HeadTitle.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.HeadTitle.setFont(font)
        self.HeadTitle.setObjectName("HeadTitle")
        self.verticalLayout.addWidget(self.HeadTitle)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.NameandEmailTitlesLayout = QtWidgets.QHBoxLayout()
        self.NameandEmailTitlesLayout.setContentsMargins(30, 5, 30, 5)
        self.NameandEmailTitlesLayout.setSpacing(0)
        self.NameandEmailTitlesLayout.setObjectName("NameandEmailTitlesLayout")
        self.NameTitle = QtWidgets.QLabel(self.centralwidget)
        self.NameTitle.setMinimumSize(QtCore.QSize(0, 0))
        self.NameTitle.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.NameTitle.setFont(font)
        self.NameTitle.setStyleSheet("color: rgb(117, 117, 117);")
        self.NameTitle.setObjectName("NameTitle")
        self.NameandEmailTitlesLayout.addWidget(self.NameTitle)
        self.EmailTitle = QtWidgets.QLabel(self.centralwidget)
        self.EmailTitle.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.EmailTitle.setFont(font)
        self.EmailTitle.setStyleSheet("color: rgb(117, 117, 117);")
        self.EmailTitle.setObjectName("EmailTitle")
        self.NameandEmailTitlesLayout.addWidget(self.EmailTitle)
        self.verticalLayout.addLayout(self.NameandEmailTitlesLayout)
        self.NameandEmailLayout = QtWidgets.QHBoxLayout()
        self.NameandEmailLayout.setContentsMargins(30, -1, 30, 10)
        self.NameandEmailLayout.setObjectName("NameandEmailLayout")

        # Name Input Box
        self.NameBox = QtWidgets.QLineEdit(self.centralwidget)
        self.NameBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NameBox.sizePolicy().hasHeightForWidth())
        self.NameBox.setSizePolicy(sizePolicy)
        self.NameBox.setMinimumSize(QtCore.QSize(0, 40))
        self.NameBox.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NameBox.setFont(font)
        self.NameBox.setStyleSheet("padding-left: 10px")
        self.NameBox.setObjectName("NameBox")

        # Email Box
        self.NameandEmailLayout.addWidget(self.NameBox)
        self.EmailBox = QtWidgets.QLineEdit(self.centralwidget)
        self.EmailBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EmailBox.sizePolicy().hasHeightForWidth())
        self.EmailBox.setSizePolicy(sizePolicy)
        self.EmailBox.setMinimumSize(QtCore.QSize(0, 40))
        self.EmailBox.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.EmailBox.setFont(font)
        self.EmailBox.setStyleSheet("padding-left: 10px")
        self.EmailBox.setClearButtonEnabled(True)
        self.EmailBox.setObjectName("EmailBox")
        self.NameandEmailLayout.addWidget(self.EmailBox)
        self.NameandEmailLayout.setStretch(0, 1)
        self.NameandEmailLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.NameandEmailLayout)

        self.BudgetandCurrencyTitlesLayout = QtWidgets.QHBoxLayout()
        self.BudgetandCurrencyTitlesLayout.setContentsMargins(30, 5, 30, 5)
        self.BudgetandCurrencyTitlesLayout.setSpacing(0)
        self.BudgetandCurrencyTitlesLayout.setObjectName("BudgetandCurrencyTitlesLayout")

        # Budget Title
        self.BudgetTitle = QtWidgets.QLabel(self.centralwidget)
        self.BudgetTitle.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BudgetTitle.setFont(font)
        self.BudgetTitle.setStyleSheet("color: rgb(117, 117, 117);")
        self.BudgetTitle.setObjectName("BudgetTitle")


        self.BudgetandCurrencyTitlesLayout.addWidget(self.BudgetTitle)
        self.CurrencyTitle = QtWidgets.QLabel(self.centralwidget)
        self.CurrencyTitle.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)

        self.CurrencyTitle.setFont(font)
        self.CurrencyTitle.setStyleSheet("color: rgb(117, 117, 117);")
        self.CurrencyTitle.setObjectName("CurrencyTitle")
        self.BudgetandCurrencyTitlesLayout.addWidget(self.CurrencyTitle)
        self.verticalLayout.addLayout(self.BudgetandCurrencyTitlesLayout)
        self.BudgetandCurrencyLayout = QtWidgets.QHBoxLayout()
        self.BudgetandCurrencyLayout.setContentsMargins(30, -1, 30, 10)
        self.BudgetandCurrencyLayout.setObjectName("BudgetandCurrencyLayout")
        self.BudgetBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.BudgetBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BudgetBox.sizePolicy().hasHeightForWidth())
        self.BudgetBox.setSizePolicy(sizePolicy)
        self.BudgetBox.setMinimumSize(QtCore.QSize(0, 40))
        self.BudgetBox.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BudgetBox.setFont(font)
        self.BudgetBox.setFrame(False)
        self.BudgetBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.BudgetBox.setMaximum(10000000.0)
        self.BudgetBox.setProperty("value", 300.0)
        self.BudgetBox.setObjectName("BudgetBox")
        self.BudgetandCurrencyLayout.addWidget(self.BudgetBox)
        self.CurrencyBox = QtWidgets.QComboBox(self.centralwidget)
        self.CurrencyBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CurrencyBox.sizePolicy().hasHeightForWidth())
        self.CurrencyBox.setSizePolicy(sizePolicy)
        self.CurrencyBox.setMinimumSize(QtCore.QSize(0, 40))
        self.CurrencyBox.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CurrencyBox.setFont(font)
        self.CurrencyBox.setStyleSheet("padding-left: 10px")
        self.CurrencyBox.setObjectName("CurrencyBox")
        self.CurrencyBox.addItem("")
        self.CurrencyBox.addItem("")
        self.CurrencyBox.addItem("")
        self.CurrencyBox.addItem("")
        self.BudgetandCurrencyLayout.addWidget(self.CurrencyBox)
        self.verticalLayout.addLayout(self.BudgetandCurrencyLayout)
        self.ThemeTitleLayout = QtWidgets.QHBoxLayout()
        self.ThemeTitleLayout.setContentsMargins(30, 5, 30, 5)
        self.ThemeTitleLayout.setSpacing(0)
        self.ThemeTitleLayout.setObjectName("ThemeTitleLayout")
        self.ThemeTitle = QtWidgets.QLabel(self.centralwidget)
        self.ThemeTitle.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ThemeTitle.setFont(font)
        self.ThemeTitle.setStyleSheet("color: rgb(117, 117, 117);")
        self.ThemeTitle.setObjectName("ThemeTitle")
        self.ThemeTitleLayout.addWidget(self.ThemeTitle)
        self.verticalLayout.addLayout(self.ThemeTitleLayout)
        self.RadioLayout = QtWidgets.QHBoxLayout()
        self.RadioLayout.setContentsMargins(30, -1, 30, 0)
        self.RadioLayout.setSpacing(0)
        self.RadioLayout.setObjectName("RadioLayout")
        self.RadioGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.RadioGroup.setMinimumSize(QtCore.QSize(300, 50))
        self.RadioGroup.setTitle("")
        self.RadioGroup.setAlignment(QtCore.Qt.AlignCenter)
        self.RadioGroup.setFlat(True)
        self.RadioGroup.setObjectName("RadioGroup")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.RadioGroup)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LightRadioButton = QtWidgets.QRadioButton(self.RadioGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LightRadioButton.sizePolicy().hasHeightForWidth())
        self.LightRadioButton.setSizePolicy(sizePolicy)
        self.LightRadioButton.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.LightRadioButton.setFont(font)
        self.LightRadioButton.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;  \n"
"    height: 20px; \n"
"    border-radius: 10px;\n"
"    border: 1px solid gray; \n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    background-color: rgb(85, 85, 255); \n"
"}\n"
"")
        self.LightRadioButton.setIconSize(QtCore.QSize(20, 20))
        self.LightRadioButton.setCheckable(False)
        self.LightRadioButton.setObjectName("radioButton")
        self.LightRadioButton.clicked.connect(lambda: self.setTheme(True))

        self.horizontalLayout.addWidget(self.LightRadioButton)
        self.DarkRadioButton = QtWidgets.QRadioButton(self.RadioGroup)
        self.DarkRadioButton.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.DarkRadioButton.setFont(font)
        self.DarkRadioButton.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;  \n"
"    height: 20px; \n"
"    border-radius: 10px;\n"
"    border: 1px solid gray; \n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    background-color: rgb(85, 85, 255); \n"
"}\n"
"")
        self.DarkRadioButton.setIconSize(QtCore.QSize(50, 50))
        self.DarkRadioButton.setCheckable(False)
        self.DarkRadioButton.setObjectName("DarkRadioButton")
        self.DarkRadioButton.clicked.connect(lambda: self.setTheme(False))

        self.horizontalLayout.addWidget(self.DarkRadioButton)
        self.RadioLayout.addWidget(self.RadioGroup)
        self.verticalLayout.addLayout(self.RadioLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.ButtonLayout = QtWidgets.QHBoxLayout()
        self.ButtonLayout.setContentsMargins(20, -1, 20, -1)
        self.ButtonLayout.setSpacing(10)
        self.ButtonLayout.setObjectName("ButtonLayout")

        # Edit Button
        self.EditButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EditButton.sizePolicy().hasHeightForWidth())
        self.EditButton.setSizePolicy(sizePolicy)
        self.EditButton.setMinimumSize(QtCore.QSize(100, 50))
        self.EditButton.setMaximumSize(QtCore.QSize(500, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.EditButton.setFont(font)
        self.EditButton.setStyleSheet("QPushButton {\n"
"    border-radius:3px;\n"
"    background-color: white;\n"
"transition: 0.3s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 85, 255);\n"
"     color:white\n"
"}\n"
"")
        self.EditButton.setObjectName("EditButton")
        self.EditButton.clicked.connect(self.enableWidgets)


        self.ButtonLayout.addWidget(self.EditButton)
        self.DoneButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DoneButton.sizePolicy().hasHeightForWidth())
        self.DoneButton.setSizePolicy(sizePolicy)
        self.DoneButton.setMinimumSize(QtCore.QSize(200, 0))
        self.DoneButton.setMaximumSize(QtCore.QSize(500, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.DoneButton.setFont(font)
        self.DoneButton.setStyleSheet("QPushButton {\n"
"    border-radius:3px;\n"
"    background-color: white;\n"
"transition: 0.3s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 85, 255);\n"
"     color:white\n"
"}\n"
"")
        self.DoneButton.setFlat(False)
        self.DoneButton.setObjectName("DoneButton")
        self.DoneButton.clicked.connect(self.saveDataFromWidgets)


        self.ButtonLayout.addWidget(self.DoneButton)
        self.verticalLayout.addLayout(self.ButtonLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.loadDataToWidgets()

    def loadDataToWidgets(self):
        dataList = SavedData.load_user_data()
        self.NameBox.setPlaceholderText(dataList[0])
        self.NameBox.setText(dataList[0])

        self.EmailBox.setPlaceholderText(dataList[1])
        self.EmailBox.setText(dataList[1])

        self.BudgetBox.setValue(dataList[2])

        self.CurrencyBox.setCurrentIndex(dataList[3])

        if dataList[4]:
            self.LightRadioButton.setChecked(True)
            self.setTheme(True)
        else:
            self.DarkRadioButton.setChecked(True)
            self.setTheme(False)

    def saveDataFromWidgets(self):
        dataList = ["", "", 0, 0, True]

        dataList[0] = self.NameBox.text()
        dataList[1] = self.EmailBox.text()
        dataList[2] = self.BudgetBox.value()
        dataList[3] = self.CurrencyBox.currentIndex()

        if self.LightRadioButton.isChecked() and self.DarkRadioButton.isChecked() == False:
            dataList[4] = True
        else:
            dataList[4] = False
        SavedData.save_user_data(dataList)

        self.expense_tracker = ExpenseTracker()
        self.expense_tracker.showMaximized()
        QtWidgets.QApplication.activeWindow().close()

    def enableWidgets(self):
        self.NameBox.setEnabled(True)
        self.EmailBox.setEnabled(True)
        self.BudgetBox.setEnabled(True)
        self.CurrencyBox.setEnabled(True)
        self.DarkRadioButton.setCheckable(True)
        self.LightRadioButton.setCheckable(True)

        # dataList = SavedData.load_user_data()
        # print(dataList[4])
        # if dataList[4]:
        #     self.LightRadioButton.setChecked(True)
        # else:
        #     self.DarkRadioButton.setChecked(True)

    def setTheme(self, check):

        if check:
            self.centralwidget.setStyleSheet("background-color: rgb(240, 240, 240);")
            self.NameBox.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.EmailBox.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.BudgetBox.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.CurrencyBox.setStyleSheet("background-color: rgb(255, 255, 255);"
                "border: 3px solid  rgb(104, 104, 147);"
                "border-radius: 10px;"
                "QComboBox::drop-down {\n"
                "border: none;"
                "background-color:  rgb(104, 104, 147);"
                "width: 20px;"
            "}")

            self.HeadTitle.setStyleSheet("color : Black;")
            self.NameTitle.setStyleSheet("color: rgb(120, 120, 120);")
            self.EmailTitle.setStyleSheet("color: rgb(120, 120, 120);")
            self.BudgetTitle.setStyleSheet("color: rgb(120, 120, 120);")
            self.CurrencyTitle.setStyleSheet("color: rgb(120, 120, 120);")
            self.ThemeTitle.setStyleSheet("color: rgb(120, 120, 120);")
            self.RadioGroup.setStyleSheet("color: black;")
        else:
            self.centralwidget.setStyleSheet("background-color: rgb(23, 22, 45);")
            self.HeadTitle.setStyleSheet("color: rgb(255, 255, 255);")
            self.NameBox.setStyleSheet("color: white; background-color: rgb(47, 47, 140); border-radius: 10px;")
            self.EmailBox.setStyleSheet("color: white; background-color: rgb(47, 47, 140); border-radius: 10px;")
            self.BudgetBox.setStyleSheet("color: white; background-color: rgb(47, 47, 140); border-radius: 10px;")
            self.CurrencyBox.setStyleSheet("color: white; background-color: rgb(47, 47, 140); border-radius: 10px;")

            self.NameTitle.setStyleSheet("color: rgb(220, 220, 220);")
            self.EmailTitle.setStyleSheet("color: rgb(220, 220, 220);")
            self.BudgetTitle.setStyleSheet("color: rgb(220, 220, 220);")
            self.CurrencyTitle.setStyleSheet("color: rgb(220, 220, 220);")
            self.ThemeTitle.setStyleSheet("color: rgb(220, 220, 220);")
            self.RadioGroup.setStyleSheet("color: white;")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Expense Tracker"))
        self.HeadTitle.setText(_translate("MainWindow", "  Account"))
        self.NameTitle.setText(_translate("MainWindow", "Name"))
        self.EmailTitle.setText(_translate("MainWindow", "Email"))
        self.NameBox.setPlaceholderText(_translate("MainWindow", "Ahmed"))
        self.EmailBox.setPlaceholderText(_translate("MainWindow", "example@example.com"))
        self.BudgetTitle.setText(_translate("MainWindow", "Set Budget"))
        self.CurrencyTitle.setText(_translate("MainWindow", "Prices Currency"))
        self.CurrencyBox.setItemText(0, _translate("MainWindow", "EGP"))
        self.CurrencyBox.setItemText(1, _translate("MainWindow", "USD"))
        self.CurrencyBox.setItemText(2, _translate("MainWindow", "EUR"))
        self.CurrencyBox.setItemText(3, _translate("MainWindow", "SAR"))
        self.ThemeTitle.setText(_translate("MainWindow", "Theme"))
        self.LightRadioButton.setText(_translate("MainWindow", "Light Mode"))
        self.DarkRadioButton.setText(_translate("MainWindow", "Dark Mode"))
        self.EditButton.setText(_translate("MainWindow", "Edit"))
        self.DoneButton.setText(_translate("MainWindow", "Done"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.showMaximized()
    sys.exit(app.exec_())
