

def Fitness_function(inner_pop,data1,data2):
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
    
    return scores