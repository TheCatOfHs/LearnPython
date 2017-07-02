
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
    aveFitness = sumFitness / N
    return aveFitness

#进行突变
def mutChrom(pop, mut, chromNodes, bestChrom, chromRange):
    for i in pop:
        #如果随机数小于变异概率（即可以变异)
        if mut > random.uniform(0,2):
            mutNode = random.randrange(0,chromNodes)
            mutRange = random.uniform(0, 2) * (1-pop[i].fitness/bestChrom[1])**2
            pop[i].chrom[mutNode] = pop[i].chrom[mutNode] * (1+mutRange)
            #判断变异后的范围是否在要求范围内
            pop[i].chrom[mutNode] = inRange(pop[i].chrom[mutNode], chromRange[mutNode])
    return pop

#检验便宜范围是否在要求范围内
def inRange(mutNode, chromRange):
    if chromRange[0] < mutNode < chromRange[1]:
        return mutNode
    elif mutNode-chromRange[0] > mutNode-chromRange[1]:
        return chromRange[1]
        else:
            return chromRange[0]


    

        