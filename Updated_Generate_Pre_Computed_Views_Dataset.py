# Import the required modules
#!/usr/bin/python3
import mysql.connector
import base64
from PIL import Image
import io
import pandas as pd
import cryptography
from cryptography.fernet import Fernet
import matplotlib.pyplot as plt
import seaborn as sns
#import os
import json
import os, sys, time
import pdfkit

#{1627723549.0876832}
# For security reasons, never expose your password
#password = open('/home/sois/pilot_encrypt_decrypt_method/','r').readline()

# Create a connection
mydb = mysql.connector.connect(
	host="172.16.51.28",
	user="sois",
	password="Msois@123",
        #database=sys.argv[3]
	database="healthcareviews" # Name of the database
)
"""
def DecryptData(): 
    file = open('rainfallkey.key', 'rb')
    rainfallkey = file.read() # The key will be type bytes
    input_file = 'rainfall_flood_encrypted.csv'
    output_file = 'rainfall_flood_decrypted.csv'

    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(rainfallkey)
    if(1):
        encrypted = fernet.decrypt(data)
        print("Key is Valid")
    else:
        print("Key is not Valid")

    with open(output_file, 'wb') as f:
        f.write(encrypted)
"""
"""
def PrepareData():
    global df
    df = pd.read_csv("dataset/rainfall_flood.csv")
    #df = data.drop(columns=['Date'])
    global secure_fields 
    secure_fields = []
    metafile = open("Metadata_Secure_Data.json")
    metadata = json.load(metafile)
    privatefields = metadata['metadata']
    for i in privatefields:
        if i['security'] == "private":
            secure_fields.append(i['name'])
            print(i['name'])
    global newdf   
    newdf = df.drop(secure_fields, axis =1)
"""
def DescribePlots():
    datapath = sys.argv[1]
    df = pd.read_csv(datapath)
    #df = pd.read_csv("dataset/rainfall_flood.csv")
    #df = data.drop(columns=['Date'])
    #global secure_fields 
    #secure_fields = []
    #metafile = open("Metadata_Secure_Data.json")
    #metadata = json.load(metafile)
    #privatefields = metadata['metadata']
    #for i in privatefields:
    #    if i['security'] == "private":
    #        secure_fields.append(i['name'])
    #        print(i['name'])
       
    #newdf = df.drop(secure_fields, axis =1)
    plt.figure()
    sns_plot = sns.pairplot(df)
    #fig = sns_plot.get_figure()
    stat_store_path = sys.argv[2]
    plot_name = "Pairplot.png"
    path = stat_store_path + '/' + plot_name
    sns_plot.savefig(path)
    #sns_plot.savefig("WeatherPlots/Weather_Pairplot.png")

    #hist_fig = plt.hist(newdf)
    #plt.show(block=True)
def HistogramPlots():
    
    #df = pd.read_csv("dataset/rainfall_flood.csv")
    datapath = sys.argv[1]
    df = pd.read_csv(datapath)
    #df = data.drop(columns=['Date'])
    fig=plt.figure()
    df.hist(figsize=[7,7])
    #fig = plt.figure()
    stat_store_path = sys.argv[2]
    plot_name = "Histogram.png"
    path = stat_store_path + '/' + plot_name
    fig.savefig(path)
    #fig.savefig("WeatherPlots/Weather_Histogram.png")
    

def CorrelationPlots():

    #df = pd.read_csv("dataset/rainfall_flood.csv")
    datapath = sys.argv[1]
    df = pd.read_csv(datapath)
    #df = data.drop(columns=['Date'])
    plt.figure()
    corrMatrix = df.corr()
    svm = sns.heatmap(corrMatrix, annot=True)
    #plt.show()
    stat_store_path = sys.argv[2]
    plot_name = "Correlation.png"
    path = stat_store_path + '/' + plot_name
    svm.get_figure().savefig(path)
    #svm.get_figure().savefig("WeatherPlots/Weather_Correlation.png")

def MissingPlots():

    #df = pd.read_csv("dataset/rainfall_flood.csv")
    datapath = sys.argv[1]
    df = pd.read_csv(datapath)
    #df = data.drop(columns=['Date'])
    plt.figure()
    sms = sns.heatmap(df.isnull())
    #plt.show()
    stat_store_path = sys.argv[2]
    plot_name = "Missing.png"
    path = stat_store_path + '/' + plot_name
    sms.get_figure().savefig(path)
    #sms.get_figure().savefig("WeatherPlots/Weather_Missing.png")

def OverallStat():
    import io  
    datapath = sys.argv[1]
    df = pd.read_csv(datapath)
    #df = pd.read_csv("dataset/rainfall_flood.csv")
    #df = data.drop(columns=['Date'])
    desc = df.describe()
    count = df.count() 
    head = df.head(5)
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    stat_store_path = sys.argv[2]
    stat_name = "Info.txt"
    path = stat_store_path + '/' + stat_name
    with open(path, "w", encoding="utf-8") as f:
    #with open("WeatherPlots/Info.txt", "w", encoding="utf-8") as f:
        f.write(s)
    stat_store_path = sys.argv[2]
    head_name = "HeadPlot.html"
    new_head_name = "HeadPlot.pdf"
    source_path = stat_store_path + '/' + head_name
    dest_path = stat_store_path + '/' + new_head_name
    head.to_html(source_path)
    #head.to_html("WeatherPlots/HeadPlot.html")
    pdfkit.from_url(source_path, dest_path)
    #pdfkit.from_url("WeatherPlots/HeadPlot.html","WeatherPlots/HeadPlot.pdf")
    stat_store_path = sys.argv[2]
    desc_name = "DescribePlot.html"
    new_desc_name = "DescribePlot.pdf"
    headpath = stat_store_path + '/' + desc_name
    destpath = stat_store_path + '/' + new_desc_name
    desc.to_html(headpath)
    #desc.to_html("WeatherPlots/DescribePlot.html")
    #pdfkit.from_url("WeatherPlots/DescribePlot.html","WeatherPlots/DescribePlot.pdf")
    pdfkit.from_url(headpath,destpath)
    stat_store_path = sys.argv[2]
    count_name = "CountInfo.txt"
    countpath = stat_store_path + "/" + count_name
    count.to_csv(countpath, sep=',', index=True)



# Create a cursor object
def StoreViewsDatabase():
    from datetime import datetime


    cursor = mydb.cursor()

# Open a file in binary mode
    stat_store_path = sys.argv[2]
    pair_name = "Pairplot.png"
    pair_path = stat_store_path + "/" + pair_name
    hist_name = "Histogram.png"
    hist_path = stat_store_path + "/" + hist_name
    corr_name = "Correlation.png"
    core_path = stat_store_path + "/" + corr_name
    miss_name = "Missing.png"
    miss_path = stat_store_path + "/" + miss_name
    desc_name = "DescribePlot.pdf"
    desc_path = stat_store_path + "/" + desc_name
    count_name = "CountInfo.txt"
    count_path = stat_store_path + "/" + count_name
    info_name = "Info.txt"
    info_path = stat_store_path + "/" + info_name
    head_name = "HeadPlot.pdf"
    head_path = stat_store_path + "/" + head_name
    file1 = open(pair_path,'rb').read()
    file2 = open(hist_path,'rb').read()
    file3 = open(corr_path,'rb').read()
    file4 = open(miss_path,'rb').read()
    file5 = open(desc_path,'rb').read()
    file6 = open(count_path,'rb').read()
    file7 = open(info_path,'rb').read()
    file8 = open(head_path,'rb').read()

# We must encode the file to get base64 string
    file1 = base64.b64encode(file1)
    file2 = base64.b64encode(file2)
    file3 = base64.b64encode(file3)
    file4 = base64.b64encode(file4)
    file5 = base64.b64encode(file5)
    file6 = base64.b64encode(file6)
    file7 = base64.b64encode(file7)
    file8 = base64.b64encode(file8)

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# Sample data to be inserted
    args1 = ('PairPlot', file1,timestamp,'300')
    args2 = ('Histogram', file2,timestamp,'301')
    args3 = ('Corelation', file3,timestamp,'302')
    args4 = ('Missing', file4,timestamp,'303')
    args5 = ('DescribStat', file5,timestamp,'100')
    args6 = ('CountStat', file6,timestamp,'101')
    args7 = ('InfoStat', file7,timestamp,'102')
    args8 = ('HeadStat', file8,timestamp,'103')
    #args1 = (file1)
    #args2 = (file2)
    #args3 = (file3)
    #args4 = (file4)

# Prepare a query
    #query = ' INSERT INTO views VALUES(%s, %s, %s)'
    query = "UPDATE  views SET ViewName=%s, Plots=%s , EventTime=%s WHERE Id=%s" 
    query1 = "UPDATE  statistics SET ViewName=%s, Plots=%s , EventTime=%s WHERE Id=%s" 
    #query2 = 'UPDATE  views SET Plots = %s WHERE ViewName = Weather_Histogram' 
    #query3 = 'UPDATE  views SET Plots = %s WHERE ViewName = Weather_Corelation'  
    #query4 = 'UPDATE  views SET Plots = %s WHERE ViewName = Weather_Missing' 

# Execute the query and commit the database.
    cursor.execute(query,args1)
    cursor.execute(query,args2)
    cursor.execute(query,args3)
    cursor.execute(query,args4)
    cursor.execute(query1,args5)
    cursor.execute(query1,args6)
    cursor.execute(query1,args7)
    cursor.execute(query1,args8)
    mydb.commit()


def files_to_timestamp(path):
    files = [os.path.join(path, f) for f in os.listdir(path)]
    return dict ([(f, os.path.getmtime(f)) for f in files])


def main():
    #DecryptData()
    #PrepareData()
    DescribePlots()
    HistogramPlots()
    CorrelationPlots()
    MissingPlots()
    OverallStat() 
    StoreViewsDatabase()
    """ 
    path_to_watch = '/home/sois/pilot_encrpyt_decrypt_method/dataset' 
    print('Watching {}..'.format(path_to_watch))
    before = {}

    #before = {'/home/sois/pilot_encrpyt_decrypt_method/dataset/rainfall_flood.csv': 1627723020.0110664} 
    before = files_to_timestamp(path_to_watch)

    while 1: 
        time.sleep(5) 
        after = files_to_timestamp(path_to_watch)

        added = [f for f in after.keys() if not f in before.keys()]
        removed = [f for f in before.keys() if not f in after.keys()]
        modified = []

        for f in before.keys():
            if not f in removed:
                if os.path.getmtime(f) != before.get(f):
                    modified.append(f)
        if added:
            print('Added: {}'.format(', '.join(added)))
            return main()
        if modified: 
            print('Removed: {}'.format(', '.join(removed)))
            return main()
        if removed:
             print('Modified: {}'.format(', '.join(modified))) 
             return main()
    
    '''
    file_size_stored = 34442 

    while True:
            file_size_current = os.stat('daatset/rainfall_flood.csv').st_size
            if file_size_stored != file_size_current:
                restart_program()
    except: 
      pass
    ''' 
    """

if __name__ == "__main__":
    main()
