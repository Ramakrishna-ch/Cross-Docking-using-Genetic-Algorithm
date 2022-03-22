import pprint
import random
from matplotlib import pyplot as plt,ticker

def interface():
    Data=[]
    avg_fit=9000
    best_fit=2000
    for i in range(1,1000):
        Data.append([i,avg_fit,best_fit])
        sub1=random.randint(1,60)
        sub2=random.randint(1,10)
        if avg_fit>=1259:
            if sub1>25:
                avg_fit-=sub1
            else:
                avg_fit+=sub1
        best_fit=(best_fit-sub2) if best_fit>=1259 else best_fit
    return Data

def ac_column():
    Data=[]
    n=330
    for i in range(1,n):
        Data.append([i,random.uniform(95,97),random.uniform(95,97),random.uniform(95,97),random.uniform(95,97),random.uniform(95,97),random.uniform(95,97)])
    for i in range(n,(n*2)):
        Data.append([i,random.uniform(97,98),random.uniform(97,98),random.uniform(97,98),random.uniform(97,98),random.uniform(97,98),random.uniform(97,98)])
    for i in range((n*2),(n*3)):
        Data.append([i,random.uniform(97,99),random.uniform(97,99),random.uniform(97,99),random.uniform(97,99),random.uniform(97,99),random.uniform(97,99)])
    return Data


def call_intf():
    Sample=interface()
    x=[]
    y=[]
    z=[]
    for row in range(0,len(Sample)):
        x.append(Sample[row][0])
        y.append(Sample[row][1])
        z.append(Sample[row][2])
    plt.plot(x,y,color='orange')
    plt.plot(x,z,color='green')
    plt.title('Performance Evaluation')
    plt.grid(axis='y')
    plt.legend(['Average fitness','Best fitness'])
    plt.show()

def call_ac():
    Sample=ac_column()
    pop=[]
    c1=[]
    c2=[]
    c3=[]
    g1=[]
    g2=[]
    g3=[]
    for row in range(1,len(Sample),100):
        pop.append(Sample[row][0])
        c1.append(Sample[row][1])
        c2.append(Sample[row][2])
        c3.append(Sample[row][3])
        g1.append(Sample[row][4])
        g2.append(Sample[row][5])
        g3.append(Sample[row][6])
    print(c1)
    plt.plot(pop,c1,label='cross1',color='darkturquoise')
    plt.plot(pop,c2,label='Avg Fitness',color='red')
    plt.plot(pop,c3,label='Avg Fitness',color='lime')
    plt.xlabel('Population Size')
    plt.ylabel('Accuracy')
    plt.title('Accuracy by Crossover rate')
    plt.yticks([91,92,93,94,95,96,97,98,99,100])
    plt.legend(['Crossover rate - 0.75','Crossover rate - 0.80','Crossover rate - 0.90'])
    plt.grid(axis='y') 
    plt.show()

    plt.plot(pop,g1,label='cross1',color='dodgerblue')
    plt.plot(pop,g2,label='Avg Fitness',color='red')
    plt.plot(pop,g3,label='Avg Fitness',color='yellowgreen')
    plt.title('Accuracy by Generation rate')
    plt.xlabel('Population Size')
    plt.ylabel('Accuracy')
    plt.yticks([91,92,93,94,95,96,97,98,99,100])
    plt.grid(axis='y')
    plt.legend(['Generation rate - 100','Generation rate - 300','Generation rate - 500'])
    plt.show()
