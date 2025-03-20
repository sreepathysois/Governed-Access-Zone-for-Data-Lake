import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFileDialog 
from PyQt5.QtWidgets import QLabel, QLineEdit, QTextBrowser, QComboBox  

from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
def getkey():
    console.clear()
    console.append('Select your Private key File')
    file , check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                               "", "All Files (*);;Python Files (*.py);;Key Files (*.key)")
    if check:
        global keypath 
        keypath = file
        print(file)
        print(keypath) 
    console.clear()
    console.append('Sucessfully Imported Key')

def describe(input_file):
    console.clear()
    console.append("Loading Data for Decryption")
    import pandas as pd
    import cryptography
    from cryptography.fernet import Fernet
    import matplotlib.pyplot as plt
    import seaborn as sns
    import os
    import json
    file = open(keypath, 'rb')
    mykey = file.read() # The key will be type bytes
#file.close()
    #input_file = 'data_encrypted.csv'
    #output_file = 'data_decrypted.csv'
    input_file = '/home/ubuntu/data/data_encrypted.csv'
    output_file = 'data_decrypted.csv'

    with open(input_file, 'rb') as f:
        data = f.read()
    
    fernet = Fernet(mykey)
    if(1):
        encrypted = fernet.decrypt(data)
        print("Key is Valid")
    else:
       print("Key is not Valid")

    with open(output_file, 'wb') as f:
        f.write(encrypted)
    #console.clear()
    console.append("Sucessfully Decrypted Data")
    console.append("Loading data for Pair-Wise Plot")
    #data = pd.read_csv("data_decrypted.csv")
    df = pd.read_csv("data_decrypted.csv")
    #df = data.drop(columns=['Date'])
    secure_fields = []
    #metafile = open("Metadata_Secure_Data.json")
    """
    metadata = json.load(metafile)
    privatefields = metadata['metadata']
    for i in privatefields:
        if i['security'] == "private":
            secure_fields.append(i['name'])
            print(i['name'])
    newdf = df.drop(secure_fields, axis =1)
    """
    sns.pairplot(df)
    plt.show()
    #console.clear()
    console.append("Pair-Wise Plot of Fileds in Dataset")
    os.remove("data_decrypted.csv")

def histogram(input_file):
    console.clear()
    console.append('Loading data for Decryption')
    import pandas as pd
    import cryptography
    from cryptography.fernet import Fernet
    import matplotlib.pyplot as plt
    import seaborn as sns
    import os
    import json
    file = open(keypath, 'rb')
    mykey = file.read() # The key will be type bytes
#file.close()
    #input_file = 'data_encrypted.csv'
    input_file = '/home/ubuntu/data/data_encrypted.csv'
    output_file = 'data_decrypted.csv'

    with open(input_file, 'rb') as f:
        data = f.read()
    
    fernet = Fernet(mykey)
    if(1):
        encrypted = fernet.decrypt(data)
        print("Key is Valid")
    else:
        print("Key is not valid")
    with open(output_file, 'wb') as f:
        f.write(encrypted)
    #console.clear()
    console.append('Sucessfully Decrypted Data')
    console.append('Loading data for Histogram Plot')
    df = pd.read_csv("data_decrypted.csv")
    """
    secure_fields = []
    metafile = open("Metadata_Secure_Data.json")
    metadata = json.load(metafile)
    privatefields = metadata['metadata']
    for i in privatefields:
        if i['security'] == "private":
            secure_fields.append(i['name'])
            print(i['name'])
    newdf = df.drop(secure_fields, axis =1)
    """
    df.hist(figsize=[7,7])
    plt.show(block=True)
    #console.clear()
    console.append('Histogram Plot')
    os.remove("data_decrypted.csv")

def correlation():
    console.clear()
    console.append('Loading data for Decryption')
    import pandas as pd
    import cryptography
    from cryptography.fernet import Fernet
    import matplotlib.pyplot as plt
    import seaborn as sns
    import os
    import json
     
    file = open(keypath, 'rb')
    mykey = file.read() # The key will be type bytes
#file.close()
    #input_file = 'data_encrypted.csv'
    input_file = '/home/ubuntu/data/data_encrypted.csv'
    output_file = 'data_decrypted.csv'

    with open(input_file, 'rb') as f:
        data = f.read()
    
    fernet = Fernet(mykey)
    if(1):
        encrypted = fernet.decrypt(data)
        print("Key is Valid")
    else:
        print("Key is not valid")
    with open(output_file, 'wb') as f:
        f.write(encrypted)

    #console.clear()
    console.append('Sucessfully Decrypted Data')
    console.append('Loading data for Correlation')
    df = pd.read_csv("data_decrypted.csv")
    """
    secure_fields = []
    metafile = open("Metadata_Secure_Data.json")
    metadata = json.load(metafile)
    privatefields = metadata['metadata']
    for i in privatefields:
        if i['security'] == "private":
            secure_fields.append(i['name'])
            print(i['name'])
    newdf = df.drop(secure_fields, axis =1)
    """
    corrMatrix = df.corr()
    sns.heatmap(corrMatrix, annot=True)
    plt.show()
    #console.clear()
    console.append('Corelation Map')
    os.remove("data_decrypted.csv")

def missing():
    console.clear()
    console.append('Loading data for Decryption')
    import pandas as pd
    import cryptography
    from cryptography.fernet import Fernet
    import matplotlib.pyplot as plt
    import seaborn as sns
    import os
    import json
    file = open(keypath, 'rb')
    mykey = file.read() # The key will be type bytes
#file.close()
    #input_file = 'data_encrypted.csv'
    input_file = '/home/ubuntu/data/data_encrypted.csv'
    output_file = 'data_decrypted.csv'

    with open(input_file, 'rb') as f:
        data = f.read()
    
    fernet = Fernet(mykey)
    if(1):
        encrypted = fernet.decrypt(data)
        print("Key is Valid")
    else:
        print("Key is not valid")
    with open(output_file, 'wb') as f:
        f.write(encrypted)
    #console.clear()
    console.append('Sucessfully Decrypted Data')
    console.append('Loading data for Finding Missing Fields')
    df = pd.read_csv("data_decrypted.csv")
    """ 
    secure_fields = []
    metafile = open("Metadata_Secure_Data.json")
    metadata = json.load(metafile)
    privatefields = metadata['metadata']
    for i in privatefields:
        if i['security'] == "private":
            secure_fields.append(i['name'])
            print(i['name'])
    newdf = df.drop(secure_fields, axis =1)
    """ 
    sns.heatmap(df.isnull())
    plt.show()
    #console.clear()
    console.append('Missing Fields Map')
    os.remove("data_decrypted.csv")

def userquerry():
    console.clear()
    console.append('Select your Querry Method')
    import cryptography
    from cryptography.fernet import Fernet
    import pandas as pd
    from pandas import DataFrame
    import os
    import json
    console.clear()
    console.append('Loading Data for Decryption')
    file = open(keypath, 'rb')
    mykey = file.read() # The key will be type bytes
#file.close()
    #input_file = 'data_encrypted.csv'
    input_file = '/home/ubuntu/data/data_encrypted.csv'
    output_file = 'data_decrypted.csv'

    with open(input_file, 'rb') as f:
        data = f.read()
    
    fernet = Fernet(mykey)
    if(1):
        encrypted = fernet.decrypt(data)
        print("Key is Valid")
    else:
        print("Key is not valid")
    with open(output_file, 'wb') as f:
        f.write(encrypted)
    console.clear()
    console.append("Loading data for running your querry" )
    data = dropdown.currentText()
    print(data)
    method_name = getattr(DataFrame, data)
    df = pd.read_csv("data_decrypted.csv")
    """
    secure_fields = []
    metafile = open("Metadata_Secure_Data.json")
    metadata = json.load(metafile)
    privatefields = metadata['metadata']
    for i in privatefields:
        if i['security'] == "private":
            secure_fields.append(i['name'])
            print(i['name'])
    newdf = df.drop(secure_fields, axis =1)
    """
    #output = eval(data)      

    #output = datatest.to_string(index = False)
    #textbrowser.append(output.to_string())
    textbrowser.clear()
    textbrowser.append(method_name(df).to_string())
    #textinput.clear()
    console.clear()
    console.append("Result of your querry:" + data)
    os.remove("data_decrypted.csv")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QHBoxLayout')
#window.setStyleSheet("background-color: cyan;")
#window.setStyleSheet("background-image: url(white.jpg)")
window.setGeometry(200,300,700,500)
#layout = QHBoxLayout()
#layout1 = QVBoxLayout()
layout = QGridLayout()
button = QPushButton("Upload Key to Unlock Methods")
button.setGeometry(200, 150, 400, 100)
button.setFixedHeight(50)
button.setFont(QFont('Times', 20))
button.setStyleSheet("background-color : red")
button.clicked.connect(getkey)  # Connect clicked to greeting()

layout.addWidget(button,0,0,1,2)
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
textbrowser = QTextBrowser()
textbrowser.setAcceptRichText(True)
textbrowser.setOpenExternalLinks(True)
textbrowser.setFont(QFont('Times', 20))
layout.addWidget(textbrowser,6,0,1,2)

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
layout.setVerticalSpacing(30)
window.setLayout(layout)
window.show()
    
    
sys.exit(app.exec_())


