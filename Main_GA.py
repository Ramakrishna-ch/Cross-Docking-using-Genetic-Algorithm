import pprint
from numpy import inner
from type import Interface
from Modules import Data_Load_and_Preprocess,Population_generation,Fitness_function,Selection_strategy,Crossover


#Data loading & Preprocessing
path='./Datasets/output2.csv'
Data1=[]
Data2=[]
rows=0
rows,Data1,Data2=Data_Load_and_Preprocess.Data_Loading_and_Preprocessing(path)

Interface.call_intf()

Interface.call_ac()
#Population generation
pop=[]

pop=Population_generation.Population_gen(rows,Data1,Data2)

All_orders=[]

for curr_pop in pop:
    # print(curr_pop)
    inner_pop=[]
    scores=[]
    inner_pop=Population_generation.Inner_pop_gen(curr_pop,Data1,Data2)


    scores=Fitness_function.Fitness_function(inner_pop,Data1,Data2)


    Tournaments=[]
    Selected_parents=[]

    Tournaments,Selected_parents=Selection_strategy.Selection_strategy(inner_pop,scores)


    children=Crossover.Cross_Over(inner_pop,Selected_parents)

    new_scores=Fitness_function.Fitness_function(children,Data1,Data2)

    final_check={}
    final_check[1]=[inner_pop[Selected_parents[0][1]],Selected_parents[0][0]]
    final_check[2]=[inner_pop[Selected_parents[1][1]],Selected_parents[1][0]]
    final_check[3]=[children[0],new_scores[0]]
    final_check[4]=[children[1],new_scores[1]]

    min=final_check[1]
    for i in final_check:
        if final_check[i][1]<min[1]:
            min=final_check[i]
    All_orders.append(min)

pprint.pprint(len(All_orders))



