import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFileDialog 
from PyQt5.QtWidgets import QLabel, QLineEdit, QTextBrowser, QComboBox, QPlainTextEdit  
from PyQt5 import QtSql  
from PyQt5.QtSql import QSqlDatabase, QSqlQuery 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from datetime import datetime
import io
import os
import time


def describe():
    console.clear()
    console.append("Loading Views of PairWise Statistics from Remote database")
    import os
    import json
    import base64
    from PIL import Image
    import io 
    st = time.time() 
    query = QtSql.QSqlQuery()
    query = QSqlQuery("SELECT Plots FROM views where Id=300")
    while query.next():
         data  = query.value(0)
         #image = data[0][0]
         binary_data = base64.b64decode(data)
         image_result = Image.open(io.BytesIO(binary_data))
         image_result.show()
         et = time.time()
         elapsed_time = et - st
         console.append('Execution time:'+ str(elapsed_time) + ' ' + 'Seconds')
    #program_time = elapsed_time.toString() 
    query1 = QtSql.QSqlQuery()
    query1 = QSqlQuery("SELECT EventTime FROM views where Id=300")
    while query1.next():
         dateTime = QDateTime()
         dateTime = query1.value(0) 
         print(dateTime)
         eventtime = dateTime.toString()
    console.append("Pair-Wise Plot of Fileds in Dataset")
    console.append("Updated Batch view on :" + eventtime)

def histogram():
    console.clear()
    console.append('Loading Data views of Histogram Plots')
    import os
    import json
    import base64
    from PIL import Image
    import io 
    
    console.clear()
    console.append('Loading Data views for Coreraltion Statistics')
    st = time.time()
    query = QtSql.QSqlQuery()
    query = QSqlQuery("SELECT Plots FROM views where Id=301")
    while query.next():
         data1  = query.value(0)
         #image = data[0][0]
         binary_data1 = base64.b64decode(data1)
         image_result1 = Image.open(io.BytesIO(binary_data1))
         image_result1.show()
         et = time.time()
         elapsed_time = et - st
         console.append("Processing Time" + str(elapsed_time) + " " + "Seconds")
    query1 = QtSql.QSqlQuery()
    query1 = QSqlQuery("SELECT EventTime FROM views where Id=301")
    while query1.next():
         dateTime = QDateTime()
         dateTime = query1.value(0) 
         print(dateTime)
         eventtime = dateTime.toString()
    console.clear()
    console.append("Pair-Wise Plot of Fileds in Dataset")
    console.append('Data views of Histogram Plots')
    console.append("Updated Batch view on :" + eventtime)

def correlation():
    console.clear()
    console.append('Loading Data views for Coreraltion Statistics')
    import os
    import json
    import base64
    from PIL import Image
    import io 
    st = time.time()
    query = QtSql.QSqlQuery()
    query = QSqlQuery("SELECT Plots FROM views where Id=302")
    while query.next():
         data2  = query.value(0)
         #image = data[0][0]
         binary_data2 = base64.b64decode(data2)
         image_result2 = Image.open(io.BytesIO(binary_data2))
         image_result2.show()
         et = time.time()
         elapsed_time = et - st
         console.append("Processing Time" + str(elapsed_time) + " " + "Seconds")
    query1 = QtSql.QSqlQuery()
    query1 = QSqlQuery("SELECT EventTime FROM views where Id=302")
    while query1.next():
         dateTime = QDateTime()
         dateTime = query1.value(0) 
         print(dateTime)
         eventtime = dateTime.toString()
    console.append("Pair-Wise Plot of Fileds in Dataset")
    console.append(' Data views for Coreraltion Statistics')
    console.append("Updated Batch view on :" + eventtime)

def missing():
    console.clear()
    console.append('Loading Data Views for Missing Statistics')
    import os
    import json
    import base64
    from PIL import Image
    import io 
    st = time.time()
    query = QtSql.QSqlQuery()
    query = QSqlQuery("SELECT Plots FROM views where Id=303")
    while query.next():
       data3  = query.value(0)
         #image = data[0][0]
       binary_data3 = base64.b64decode(data3)
       image_result3 = Image.open(io.BytesIO(binary_data3))
       image_result3.show()
       et = time.time()
       elapsed_time = et - st
       console.append("Processing Time" + str(elapsed_time) + " " + "Seconds")
    query1 = QtSql.QSqlQuery()
    query1 = QSqlQuery("SELECT EventTime FROM views where Id=303")
    while query1.next():
         dateTime = QDateTime()
         dateTime = query1.value(0) 
         print(dateTime)
         eventtime = dateTime.toString()
    console.append("Pair-Wise Plot of Fileds in Dataset")
    console.append('Data Views for Missing Statistics')
    console.append("Updated Batch view on :" + eventtime)

def write_file(filedata, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(filedata)
        return


def userquerry():
    console.clear()
    console.append('Select your Querry Method')
    import os
    import json
    import base64
    from PIL import Image
    import io 
    console.clear()
    console.append('Loading Data for Decryption')
    console.append("Loading data for running your querry" )
    data = dropdown.currentText()
    print(data)

    def retrievedescribe():
        import os
        st = time.time()
        query = QtSql.QSqlQuery()
        query = QSqlQuery("SELECT Plots FROM statistics where Id=100")
        while query.next():
            mydata  = query.value(0)
            mybinary_data = base64.b64decode(mydata)
            #os.remove('OverallStats/DescribePlot.pdf')
            write_file(mybinary_data,'OverallStats/DescribePlot.pdf')
            text_edit.clear()
            os.system('pdftotext -layout OverallStats/DescribePlot.pdf')
            text = open('OverallStats/DescribePlot.txt').read()
            text_edit.setPlainText(text)
            et = time.time()
            elapsed_time = et - st
            console.append("Processing Time" + str(elapsed_time) + " " + "Seconds")
        query1 = QtSql.QSqlQuery()
        query1 = QSqlQuery("SELECT EventTime FROM statistics where Id=100")
        while query1.next():
            dateTime = QDateTime()
            dateTime = query1.value(0) 
            print(dateTime)
            eventtime = dateTime.toString()
        console.append("Decribe Statistics Fileds in Dataset")
        console.append('Views for Decribe Statistics')
        console.append("Updated Batch view on :" + eventtime)
            


    def retrievecount(): 
        st = time.time()
        query = QtSql.QSqlQuery()
        query = QSqlQuery("SELECT Plots FROM statistics where Id=101")
        while query.next():
            data1  = query.value(0)
            binary_data1 = base64.b64decode(data1)
            write_file(binary_data1,'OverallStats/Count.txt')
            text = open('OverallStats/Count.txt').read()
            text_edit.setPlainText(text)
            et = time.time()
            elapsed_time = et - st
            console.append("Processing Time" + str(elapsed_time) + " " + "Seconds")
        query1 = QtSql.QSqlQuery()
        query1 = QSqlQuery("SELECT EventTime FROM statistics where Id=101")
        while query1.next():
            dateTime = QDateTime()
            dateTime = query1.value(0) 
            print(dateTime)
            eventtime = dateTime.toString()
        console.append("Count Statistics Fileds in Dataset")
        console.append('Views for Count Statistics')
        console.append("Updated Batch view on :" + eventtime)

    def retrieveinfo():  
        st = time.time()
        query = QtSql.QSqlQuery()
        query = QSqlQuery("SELECT Plots FROM statistics where Id=102")
        while query.next():
            data2  = query.value(0)
            binary_data2 = base64.b64decode(data2)
            write_file(binary_data2,'OverallStats/Info.txt')
            text_edit.clear()
            text = open('OverallStats/Info.txt').read()
            text_edit.setPlainText(text)
            et = time.time()
            elapsed_time = et - st
            console.append("Processing Time" + str(elapsed_time) + " " + "Seconds")
        query1 = QtSql.QSqlQuery()
        query1 = QSqlQuery("SELECT EventTime FROM statistics where Id=102")
        while query1.next():
            dateTime = QDateTime()
            dateTime = query1.value(0) 
            print(dateTime)
            eventtime = dateTime.toString()
        console.append("Info Statistics Fileds in Dataset")
        console.append('Views for Info Statistics')
        console.append("Updated Batch view on :" + eventtime)


    def retrievehead():  
        st = time.time()
        query = QtSql.QSqlQuery()
        query = QSqlQuery("SELECT Plots FROM statistics where Id=103")
        while query.next():
            data3  = query.value(0)
            binary_data3 = base64.b64decode(data3)
            write_file(binary_data3,'OverallStats/HeadInfo.pdf')
            import os 
            os.system('pdftotext -layout OverallStats/HeadInfo.pdf')
            text_edit.clear()
            text_edit.clear()
            text = open('OverallStats/HeadInfo.txt').read()
            text_edit.setPlainText(text)
            et = time.time()
            elapsed_time = et - st
            console.append("Processing Time" + str(elapsed_time) + " " + "Seconds")
        query1 = QtSql.QSqlQuery()
        query1 = QSqlQuery("SELECT EventTime FROM statistics where Id=103")
        while query1.next():
            dateTime = QDateTime()
            dateTime = query1.value(0) 
            print(dateTime)
            eventtime = dateTime.toString()
        console.append("Head Statistics Fileds in Dataset")
        console.append('Views for Head Statistics')
        console.append("Updated Batch view on :" + eventtime)
    
    data = dropdown.currentText()
    print(data) 
    if(data == "describe"): 
       retrievedescribe()  
    elif(data == "info"): 
      retrieveinfo()  
    elif(data == "count"): 
      retrievecount()  
    elif(data == "head"): 
       retrievehead()  
    else:
       return

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QHBoxLayout')
#window.setStyleSheet("background-color: cyan;")
#window.setStyleSheet("background-image: url(white.jpg)")
window.setGeometry(200,300,700,500)
#layout = QHBoxLayout()
#layout1 = QVBoxLayout()
layout = QGridLayout()
#button = QPushButton("Upload Key to Unlock Methods")
#button.setGeometry(200, 150, 400, 100)
#button.setFixedHeight(50)
#button.setFont(QFont('Times', 20))
#button.setStyleSheet("background-color : red")
#button.clicked.connect(getkey)  # Connect clicked to greeting()

#layout.addWidget(button,0,0,1,2)
btn = QPushButton('Describe Fields')
#btn.move(100,100)
btn.setGeometry(200, 150, 400, 100)
btn.setFont(QFont('Times', 20))
btn.setStyleSheet("background-color : orange")
btn.clicked.connect(describe)  # Connect clicked to greeting()

layout.addWidget(btn,1,0)
btn1 = QPushButton('Histogram')
btn1.setGeometry(200, 150, 100, 40)
btn1.setFont(QFont('Times', 20))
btn1.resize(100,32)
btn1.setStyleSheet("background-color : grey")
btn1.clicked.connect(histogram)  # Connect clicked to greeting()
layout.addWidget(btn1,1,1)
#msg = QLabel('')
#layout.addWidget(msg)
btn2 = QPushButton('Mutual Interaction')
btn2.setGeometry(200, 150, 100, 40)
btn2.setFont(QFont('Times', 20))
btn2.setStyleSheet("background-color : green")
btn2.clicked.connect(correlation)  # Connect clicked to greeting()
layout.addWidget(btn2,2,0)
btn3 = QPushButton('Missing Fields')
btn3.setGeometry(200, 150, 100, 40)
btn3.setFont(QFont('Times', 20))
btn3.setStyleSheet("background-color : yellow")
btn3.clicked.connect(missing)  # Connect clicked to greeting()
layout.addWidget(btn3,2,1)

textlabel = QLabel() 
textlabel.setText('Select your Dataframe Methods:')
textlabel.setFont(QFont('Times', 20))
layout.addWidget(textlabel,4,0)

#textinput = QLineEdit()
#layout.addWidget(textinput,4,1,1,1)
#textinput.setFont(QFont('Times', 20))
#inputbutton = QPushButton('Enter Methods')
#inputbutton.clicked.connect(userquerry)
#inputbutton.setGeometry(200, 150, 100, 40)
#inputbutton.setFont(QFont('Times', 20))
#inputbutton.setStyleSheet("background-color : yellow")
#layout.addWidget(inputbutton,5,1)

dropdown = QComboBox()
dropdown.setFont(QFont('Times', 20))
method_list = ["describe", "isnull", "head", "info", "count"]
dropdown.addItems(method_list) 
dropdown.currentIndexChanged.connect(userquerry)
layout.addWidget(dropdown,4,1,1,1)
'''
textbrowser = QTextBrowser()
textbrowser.setAcceptRichText(True)
textbrowser.setOpenExternalLinks(True)
textbrowser.setFont(QFont('Times', 20))
layout.addWidget(textbrowser,6,0,1,2)
'''
text_edit = QPlainTextEdit()
text_edit.setFont(QFont('Times', 17))
layout.addWidget(text_edit,6,0,1,2)
console = QTextBrowser()
console.setAcceptRichText(True)
console.setOpenExternalLinks(True)
console.setFont(QFont('Times', 20))
console.setFixedHeight(50)
layout.addWidget(console,7,0,1,2)
console.clear()
console.append('Welcome to Governed Access Zone of Data Lake')
console.append('')
console.append('')
console.append('Load your key to unlock methods')

# Set Database Connection 

db = QSqlDatabase.addDatabase("QMYSQL")
db.setHostName("172.16.51.28")
db.setDatabaseName("weather")
db.setUserName("sois")
db.setPassword("Msois@123")

# Solved qtmysql driver error by
# sudo apt install libqt5sql5-mysql

if db.open():
    print("Connection Sucessfull Db")
else:
    print("Connection Failed")

query = QSqlQuery()
query.exec("select Id, ViewName from views")
#print(results)
# displaying output of query in the table
layout.setVerticalSpacing(30)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())


