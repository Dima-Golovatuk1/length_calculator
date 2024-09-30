from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        translate = QtCore.QCoreApplication.translate
        font = QtGui.QFont()
        font.setPointSize(13)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setWindowTitle(translate("length calculator", "length calculator"))

        self.btn_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calculate.setGeometry(QtCore.QRect(110, 100, 250, 100))
        self.btn_calculate.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.btn_calculate.setObjectName("btn_calculate")
        self.btn_calculate.setText(translate("MainWindow", "Вирахувати"))



        self.distance_value = QtWidgets.QComboBox(self.centralwidget)
        self.distance_value.setGeometry(QtCore.QRect(10, 20, 80, 31))
        self.distance_value.setFont(font)
        self.distance_value.setModelColumn(0)
        self.distance_value.setObjectName("distance_value")
        self.distance_value.addItems(["Фут", "Дюйм", "Ярд", "Миль"])


        self.distance_result = QtWidgets.QComboBox(self.centralwidget)
        self.distance_result.setGeometry(QtCore.QRect(360, 20, 80, 31))
        self.distance_result.setFont(font)
        self.distance_result.setModelColumn(0)
        self.distance_result.setObjectName("distance_result")
        self.distance_result.addItems(["Фут", "Дюйм", "Ярд", "Миль"])

        self.result = QtWidgets.QTextEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(250, 20, 104, 31))
        self.result.setFont(font)
        self.result.setReadOnly(True)
        self.result.setObjectName("result")


        self.value = QtWidgets.QTextEdit(self.centralwidget)
        self.value.setGeometry(QtCore.QRect(100, 20, 104, 31))
        self.value.setFont(font)
        self.value.setObjectName("value")

        font = QtGui.QFont()
        font.setPointSize(30)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 10, 21, 41))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText(translate("MainWindow", "="))
        MainWindow.setCentralWidget(self.centralwidget)

        self.btn_calculate.clicked.connect(self.calculate)

    def calculate(self):
        selected_value = self.distance_value.currentText()
        selected_result = self.distance_result.currentText()
        selected_value_num = int(self.value.toPlainText())
        if selected_value == "Фут":
            if selected_result == "Фут":
                num = selected_value_num
                num2 = 1
                result = num * num2
                self.result.setText(str(result))
            elif selected_result == "Дюйм":
                num = selected_value_num
                num2 = 12
                result = num * num2
                self.result.setText(str(result))
            elif selected_result == "Ярд":
                num = selected_value_num
                num2 = 0.333333
                result = num * num2
                self.result.setText(str(result))
            elif selected_result == "Миль":
                num = selected_value_num
                num2 = 0.000189393939
                result = num * num2
                self.result.setText(str(result))
        elif selected_value == "Дюйм":
            if selected_result == "Фут":
                num = selected_value_num
                num2 = 0.0833333
                result = num * num2
                self.result.setText(str(result))
            elif selected_result == "Дюйм":
                num = selected_value_num
                num2 = 1
                result = num * num2
                self.result.setText(str(result))
            elif selected_result == "Ярд":
                num = selected_value_num
                num2 = 0.0277777666667
                result = num * num2
                self.result.setText(str(result))
            elif selected_result == "Миль":
                num = selected_value_num
                num2 = 1.5783*10**-5
                result = num * num2
                self.result.setText(str(result))
            print(selected_value)
            print(selected_result)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

