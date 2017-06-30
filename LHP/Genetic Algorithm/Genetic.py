
import random

#寻找最优染色体
def findBest(pop):
    best = ['1', 0]
    for i in pop:
        if best[1] < pop[i].fitness:
            best = [i, pop[i].fitness]
    return best

#赋初始值
def initialize(pop, chromNodes, chromRange):
    for i in pop:
        for j in range(chromNodes):
            pop[i].chrom.append(random.uniform(chromRange[j][0], chromRange[j][1]+1))
    
    return pop

#计算平均适应度
def calAveFitness(pop, N):
    sumFitness = 0
    for i in pop:
        sumFitness = sumFitness + pop[i].fitness
    aveFitness = summFitness / N
    return aveFitness
    

    

        