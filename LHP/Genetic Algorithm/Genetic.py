
import random

#寻找最优染色体
def findBest(pop):
    best = ['1', 0.0000001]
    for i in pop:
        if best[1] < pop[i].fitness:
            best = [i, pop[i].fitness]
    return best

#寻找最劣染色体
def findWorse(pop):
    worse = ['1', 999999]
    for i in pop:
        if worse[1] > pop[i].fitness:
            worse = [i, pop[i].fitness]
    return worse

#赋初始值
def initialize(pop, chromNodes, chromRange):
    for i in pop:
        chromList = []
        for j in range(chromNodes):
            chromList.append(random.uniform(chromRange[j][0], chromRange[j][1]+1))
        pop[i].chrom = chromList.copy()
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
        if mut > random.random():
            mutNode = random.randrange(0,chromNodes)
            mutRange = random.random() * (1-pop[i].fitness/bestChrom[1])**2
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

#进行交叉
def acrChrom(pop, acr, chromNodes):
    for i in pop:
        for j in pop:
            if acr > random.random():
                acrNode = random.randrange(0, chromNodes)
                #两个染色体节点进行交换
                pop[i].chrom[acrNode], pop[j].chrom[acrNode] = pop[j].chrom[acrNode], pop[i].chrom[acrNode]
    return pop

#进行比较
def compareChrom(nowbestChrom, bestChrom):
    if bestChrom[1] > nowbestChrom[1]:
        return bestChrom
    else:
        return nowbestChrom
    

        