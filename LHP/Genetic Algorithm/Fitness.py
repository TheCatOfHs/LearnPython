import math

def calFitness(pop):
    
    for i in pop:
        #计算每个染色体的适应度
        pop[i].fitness = funcFitness(pop[i].chrom)

    return pop

def funcFitness(chrom):
    #适应度函数
    fitness = chrom[0]*chrom[1]-chrom[3]/chrom[2]/chrom[1]

    return fitness
