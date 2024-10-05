# length_calculator

### length_calculator - це калькулятор довжин, який переводить між собою такі одиниці виміру, як: Фути, Дюйми, Ярди, Милі.

`class Ui_MainWindow(object):` слугує шаблоном для головного вікна інтерфейсу.

`def setupUi(self, MainWindow):` — це функція, в якій прописані всі головні налаштування інтерфейсу.

---

Тут прописані стилі та налаштування до вікна програмитакі такі як розмір:

```python~~
MainWindow.setObjectName("MainWindow") #задаємо ім'я обєкту MainWindow
MainWindow.resize(450, 320) #задаємо розмір самого вікна програми
self.centralwidget = QtWidgets.QWidget(MainWindow) #створення такого якби вікна на якому буду зозміщатися всі елементи
self.centralwidget.setEnabled(True) #вмикаємо це вікно (хоча вона вімкнено автоматично, тому це не обов'язково)
self.centralwidget.setObjectName("centralwidget") #даємо ім'я елементу
MainWindow.setWindowTitle(translate("length calculator", "length calculator")) #ставимо заголовок на нашу програму
```

Це стилі та налаштування прописані для кнопки:
```python~~
        self.btn_calculate = QtWidgets.QPushButton(self.centralwidget) #Створюємо елемент в нашому випадку кнопку
            і вказуємо дн ми його створюємо в нашому випадка на елемента centralwidget
        self.btn_calculate.setGeometry(QtCore.QRect(110, 100, 250, 100)) #Встановлюємо положення та розмір
        self.btn_calculate.setStyleSheet("background-color: rgb(170, 170, 170);") #тут задаємо колір кнопки-елементу
        self.btn_calculate.setObjectName("btn_calculate") #ім'я кнопки-елементу
        self.btn_calculate.setText(translate("MainWindow", "Вирахувати")) #Текст в смому елементі
```

Стилі та налаштування прописані для фігнюшки де ти вибираєш один із 4 варіантів:
```python~~
        #тут майже все аналогічно що і з кнопкою але
        self.distance_value = QtWidgets.QComboBox(self.centralwidget) #створення
        self.distance_value.setGeometry(QtCore.QRect(10, 20, 80, 31)) #розміщення та розмір
        self.distance_value.setFont(font) #в даному рядку вказуємо зовнішній вигляд шрифта
        self.distance_value.setObjectName("distance_value") #ім'я
        self.distance_value.addItems(["Фут", "Дюйм", "Ярд", "Миль"]) #тут вказуємо які варіанти користувач зможе вибрати
```

Те саме що і зверху але тут вибирається на що перетворити
```python~~
        # Все те саме змынивося лише ім'я та кординати
        self.distance_result = QtWidgets.QComboBox(self.centralwidget)
        self.distance_result.setGeometry(QtCore.QRect(360, 20, 80, 31))
        self.distance_result.setFont(font)
        self.distance_result.setModelColumn(0)
        self.distance_result.setObjectName("distance_result")
        self.distance_result.addItems(["Фут", "Дюйм", "Ярд", "Миль"])
```

По факту це один і той самий елемент, проте мені сподобалося що в QTextEdit коли ти виходиш за рамки
то тебе переносити на 2 рядок і в тебе є можливість скролити. Тому замість обичного тексту
де повинен виводитися результат я вирішив що зроблю отакий якби input але ```self.result.setReadOnly(True)``` поставлю
його тільки на читання без змоги редагувати
```python~~
        self.result = QtWidgets.QTextEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(250, 20, 104, 31))
        self.result.setFont(font)
        self.result.setReadOnly(True)
        self.result.setObjectName("result")


        self.value = QtWidgets.QTextEdit(self.centralwidget)
        self.value.setGeometry(QtCore.QRect(100, 20, 104, 31))
        self.value.setFont(font)
        self.value.setObjectName("value")
```

Ну а це просто я так зробив знак =
```python~~
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 10, 21, 41))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText(translate("MainWindow", "="))
        MainWindow.setCentralWidget(self.centralwidget)
```

Тут я мазав метод що при натиску на кнопку ```self.btn_calculate.clicked.connect(self.calculate)```
визивається функція калькулятора

### Калькулятор
Я думаю тут потрібно пояснити тільки цю частину коду
```python~~
    def calculate(self):
        selected_value = self.distance_value.currentText() #тут я дізнаюсь який варіант вибраний в елементі під назвою distance_value
        selected_result = self.distance_result.currentText() #аналогічно
        selected_value_num = float(self.value.toPlainText()) #тут вже не варіант а число яке було ведене в елемент під назвою value
```

### Запуск
Ну і звісно ту як запускається дана програма
```python~~
if __name__ == "__main__": #перевірка чи програма зупущена вручну а не завдяки імпорту
    app = QtWidgets.QApplication(sys.argv) #відповідає за управління подіями (там натиск миші чи кнопки на клавіатурі)
    MainWindow = QtWidgets.QMainWindow() #Створюємо головне вікно програми
    ui = Ui_MainWindow() #ui використовуватиметься для налаштування вікна
    ui.setupUi(MainWindow) #буде використовуватися щоб налаштувати інтерфейс
    MainWindow.show() #відображає вікно на екрані
    sys.exit(app.exec_()) #запускає програму
```



### Відповідь на питання:
1) Чому не tkinter? Оскільки я роблю перший раз такого роду програми а не знав про існування бібліотеки tkinter 
і мені довелося шукати якусь інформацію на якій бібліотеці можна зробити такий інтерфейс перше що занайшов в ютубі
це відео уроки по PyQt5 тому і почав робити по нбому коли дізнався про tkinter уже більша частина програми була завершина
тому вирішив вже доробити на PyQt5
2) Вручну я прописував все це чи користувався Qt Designer? я прописував це вручну проте код я брав з відео

