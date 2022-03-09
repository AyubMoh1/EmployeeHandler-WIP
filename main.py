from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

from SqliteHelper import *

app = QtWidgets.QApplication([])
dlg = uic.loadUi("test.ui")

helper = SqliteHelper("test.db")


def loadData():
    users = helper.select("SELECT * FROM users")
    for row_numbers, user in enumerate(users):
        dlg.tableWidget.insertRow(row_numbers)
        for column_number, data in enumerate(user):
            cell = QtWidgets.QTableWidgetItem(data)
            dlg.tableWidget.setItem(row_numbers, column_number, cell)


def clearData():
    while (dlg.tableWidget.rowCount()>0):
        dlg.tableWidget.removeRow(0)


def addUsers():
    name = dlg.lineEdit.text()
    comp = dlg.lineEdit.text()
    user = (name, comp)
    helper.insert("INSERT INTO users(name,comp) VALUES (?,?)",user)
    clearData()
    
    loadData()


dlg.pushButton.clicked.connect(addUsers)
loadData()
dlg.show()
app.exec()
