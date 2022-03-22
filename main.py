import sqlite3
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlQuery, QSqlDatabase



app = QtWidgets.QApplication([])
dlg = uic.loadUi("test.ui")


conn=sqlite3.connect("test.db")
cursor = conn.cursor()

def loadData():
    users = select("SELECT * FROM users")
    for row_numbers, user in enumerate(users):
        dlg.tableWidget.insertRow(row_numbers)
        for column_number, data in enumerate(user):
            cell = QtWidgets.QTableWidgetItem(str(data))
            dlg.tableWidget.setItem(row_numbers, column_number, cell)


def select(query):  # SELECT
    c = cursor
    c.execute(query)
    return c.fetchall()
def edit(query):  # INSERT & UPDATE
    c = cursor
    c.execute(query)
    conn.commit()
def insert(query,inserts):  # INSERT & UPDATE
    c = cursor
    c.execute(query,inserts)
    conn.commit()

def clearData():
    while (dlg.tableWidget.rowCount()>0):
        dlg.tableWidget.removeRow(0)


def addUsers():

    name = dlg.lineEdit.text()
    comp = dlg.lineEdit_2.text()
    user = (name, comp)
    insert("INSERT INTO users(name,comp) VALUES (?,?)",user)

   
    clearData()
    loadData()

def searchUser():
    src = ''
    #srcs = dlg.lineEdit_3.text()
    loadsrc = QSqlQuery()

    loadsrc = select("SELECT * FROM users WHERE name="+src+"")
    
    for row_numbers, user in enumerate(loadsrc):
        dlg.tableWidget_2.insertRow(row_numbers)
        for column_number, data in enumerate(user):
            cell = QtWidgets.QTableWidgetItem(str(data))
            dlg.tableWidget_2.setItem(row_numbers, column_number, cell)

dlg.pushButton_2.clicked.connect(searchUser)

dlg.pushButton.clicked.connect(addUsers)
loadData()
dlg.show()
app.exec()





"""
def searchUser():
  
    srcs = dlg.lineEdit_3.text()
 
    loadsrc = select("SELECT * FROM users WHERE name="+src+"")
    for row_numbers, user in enumerate(loadsrc):
        dlg.tableWidget_2.insertRow(row_numbers)
        for column_number, data in enumerate(user):
            cell = QtWidgets.QTableWidgetItem(str(data))
            dlg.tableWidget_2.setItem(row_numbers, column_number, cell)
    print(srcs)

def viewUser():
    view = QTableWidget()
    query = QSqlQuery("SELECT * FROM users")
    view.setColumnCount(4)
    
    while query.next():
            rows = view.rowCount()
            view.setRowCount(rows + 1)
            view.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))
            view.setItem(rows, 1, QTableWidgetItem(query.value(1)))
            view.setItem(rows, 2, QTableWidgetItem(query.value(2)))
            view.setItem(rows, 3, QTableWidgetItem(query.value(3)))
   
"""


