# length_calculator

### length_calculator - це калькулятор довжин, який переводить між собою такі одиниці виміру, як: Фути, Дюйми, Ярди, Милі.

`class Ui_MainWindow(object):` слугує шаблоном для головного вікна інтерфейсу.

`def setupUi(self, MainWindow):` — це функція, в якій прописані всі головні налаштування інтерфейсу.

---

Тут прописані стилі та налаштування до вікна програми:

```python~~
MainWindow.setObjectName("MainWindow")
MainWindow.resize(450, 320)
self.centralwidget = QtWidgets.QWidget(MainWindow)
self.centralwidget.setEnabled(True)
self.centralwidget.setObjectName("centralwidget")
MainWindow.setWindowTitle(translate("length calculator", "length calculator"))
```

Це стилі та налаштування прописані для кнопки:
```python~~
        self.btn_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calculate.setGeometry(QtCore.QRect(110, 100, 250, 100))
        self.btn_calculate.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.btn_calculate.setObjectName("btn_calculate")
        self.btn_calculate.setText(translate("MainWindow", "Вирахувати"))
```

Стилі та налаштування прописані для фігнюшки де ти вибираєш один із 4 варіантів:
```python~~
        self.distance_value = QtWidgets.QComboBox(self.centralwidget)
        self.distance_value.setGeometry(QtCore.QRect(10, 20, 80, 31))
        self.distance_value.setFont(font)
        self.distance_value.setModelColumn(0)
        self.distance_value.setObjectName("distance_value")
        self.distance_value.addItems(["Фут", "Дюйм", "Ярд", "Миль"])
```

Те саме що і зверху але тут вибирається на що перетворити
```python~~
        self.distance_result = QtWidgets.QComboBox(self.centralwidget)
        self.distance_result.setGeometry(QtCore.QRect(360, 20, 80, 31))
        self.distance_result.setFont(font)
        self.distance_result.setModelColumn(0)
        self.distance_result.setObjectName("distance_result")
        self.distance_result.addItems(["Фут", "Дюйм", "Ярд", "Миль"])
```

На цьому моменті мені набридло розбирати код тому все що йде з 10 рядка по 61 це стилі та налаштування віджетів

А далі це просто моє бачення калькулятора довжин я більш чим впевнений що його можна було зробити більш компктним але...