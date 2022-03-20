#[12345|678910]
from itertools import count,permutations
import random
import numpy
import pprint
#Data Loading and preprocessing
with open('./Datasets/output2.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
data=data[1:]
row=len(data)//2
column=len(data[0])
data1=data[0:row]
data2=data[row:]

#inner pop permutaion function
def perm(a):
    return list(permutations(a))


#population generation
pop=[]
count=0

for i in range(0,row,4):
    # print(i)
    j=i
    k=0
    chromosome=[0]*8
    while(k<4):
        chromosome[k]=data1[j][0]
        chromosome[k+4]=data2[j][0]
        j+=1
        k+=1
    # count+=1
    
    pop.append(chromosome)



#inner pop
inner_pop=perm(pop[0])

#fitness function
scores=[]
pos_asgn=[0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55]

for x in range(0,len(inner_pop)):
    Total_bt=0
    for i in range(0,8):

        if int(inner_pop[x][i]) <= 639:
            curr_bt=int(data1[int(inner_pop[x][i])][5])
        else:
            curr_bt=int(data2[(int(inner_pop[x][i]))-641][5])  
        Total_bt+=(pos_asgn[i]*curr_bt)+curr_bt
    scores.append(Total_bt)
print(len(scores))


#selection strategy
tournament=[]
best_chromosomes=set()
for i in range(0,1000):
    curr_tour=[i]
    for j in range(0,3):
        curr_tour.append(random.randint(0,len(inner_pop)))
    min1=curr_tour[1]
    for k in range(1,4):
        if scores[curr_tour[k]]<scores[min1]:
            min1=curr_tour[k]
    best_chromosomes.add((scores[min1],min1))
    curr_tour.append(min1)
    tournament.append(curr_tour)
# print(tournament)
def take_first(ele):
    return ele[0]
best_chromosomes=sorted(best_chromosomes,key=take_first)
selected=[best_chromosomes[0],best_chromosomes[1]]
print(selected)

#crossover strategy
children=[]
children.append(inner_pop[selected[0][1]][0:4]+inner_pop[selected[1][1]][4:])
children.append(inner_pop[selected[1][1]][0:4]+inner_pop[selected[0][1]][4:])
print(children)

     

