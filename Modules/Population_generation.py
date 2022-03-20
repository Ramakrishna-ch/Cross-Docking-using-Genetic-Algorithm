from itertools import count,permutations

#inner pop permutaion function
def perm(a):
    return list(permutations(a))

def Population_gen(row,data1,data2):
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
    return pop

    


def Inner_pop_gen(pop,data1,data2):
    #inner pop
    inner_pop=perm(pop)

    return inner_pop