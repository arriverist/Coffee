import sys
import sqlite3
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                                                    'описание вкуса', 'цена', 'объем упаковки'])
        con = sqlite3.connect('coffee.sql')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM 'MAIN'""").fetchall()
        self.tableWidget.setRowCount(len(result))
        for i in range(len(result)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(result[i][0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(result[i][1])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(result[i][2])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(result[i][3])))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(result[i][4])))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(result[i][5])))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(str(result[i][6])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())