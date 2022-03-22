import csv

def Data_Loading_and_Preprocessing(path):
    with open(path, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    data=data[1:]
    row=len(data)//2
    column=len(data[0])
    data1=data[0:row]
    data2=data[row:]
    return row,data1,data2