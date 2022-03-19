#[12345|678910]
import csv
import numpy

#Data Loading and preprocessing
with open('output2.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
row=len(data)//2
column=len(data[0])
data1=data[1:row]
data2=data[row:]


#population generation
pop=[]

for i in range(0,100,5):
    j=i
    k=0
    chromosome=[0]*10
    while(k<5):
        chromosome[k]=data1[j][0]
        chromosome[k+5]=data2[j][0]
        j+=1
        k+=1
    pop.append(chromosome)
print(pop)
print(column)