import sys
import sqlite3
import io
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>576</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>581</width>
      <height>511</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>510</y>
      <width>461</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>460</x>
      <y>510</y>
      <width>111</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>PushButton</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>576</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
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
        self.pushButton.clicked.connect(self.add)

    def add(self):
        con = sqlite3.connect('coffee.sql')
        cur = con.cursor()
        a = self.lineEdit.text().split()
        ins = "INSERT INTO MAIN VALUES "
        ins += ("(" + a[0] + ", " + "'" + a[1] + "', " +
                a[2] + ", " + a[3] + ", " +
                "'" + a[4] + "', " +
                a[5] + ", " + a[6] + ")")
        result = cur.execute(ins).fetchall()
        con.commit()
        self.tableWidget.clear()
        con = sqlite3.connect('coffee.sql')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM 'MAIN'""").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                                                    'описание вкуса', 'цена', 'объем упаковки'])
        self.tableWidget.setRowCount(len(result))
        for i in range(len(result)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(result[i][0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(result[i][1])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(result[i][2])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(result[i][3])))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(result[i][4])))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(result[i][5])))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(str(result[i][6])))
        self.pushButton.clicked.connect(self.add)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())