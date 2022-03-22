import random


#selection strategy
def Selection_strategy(inner_pop,scores):
    tournament=[]
    best_chromosomes=set()
    for i in range(0,1000):
        curr_tour=[i]
        for j in range(0,3):
            curr_tour.append(random.randint(0,(len(inner_pop)-1)))
        min1=curr_tour[1]
        for k in range(1,4):
            if scores[curr_tour[k]]<scores[min1]:
                min1=curr_tour[k]
        best_chromosomes.add((scores[min1],min1))
        curr_tour.append(min1)
        tournament.append(curr_tour)
    # print(tournament)
    
    best_chromosomes=sorted(best_chromosomes,key=take_first)
    selected=[best_chromosomes[0],best_chromosomes[1]]

    return tournament,selected

def take_first(ele):
        return ele[0]