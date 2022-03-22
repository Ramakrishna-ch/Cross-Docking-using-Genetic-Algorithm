

def Cross_Over(inner_pop,selected):
    children=[]
    children.append(inner_pop[selected[0][1]][0:4]+inner_pop[selected[1][1]][4:])
    children.append(inner_pop[selected[1][1]][0:4]+inner_pop[selected[0][1]][4:])
    # print(children)

    return children