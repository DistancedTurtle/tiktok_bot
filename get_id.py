from pandas import *
import csv

def get_text():
    with open('used.csv', 'r') as file:
        data = list(csv.reader(file, delimiter=","))
    for (i,entry) in enumerate(data):
        if entry[2] == "False":
            data[i][2] = "True"
            with open('used.csv','w') as f:
                writer = csv.writer(f,delimiter=',')
                writer.writerows(data)
            return(entry[0])
            break
