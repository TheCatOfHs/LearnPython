# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 23:45:36 2017

@author: vento
"""

import Genetic
import Fitness
import matplotlib.pyplot as plt
import numpy as np
import datetime

startTime = datetime.datetime.now()

#染色体的类
class Chrom:
    chrom = []
    fitness = 0
    def showChrom(self):
        print(self.chrom)
    def showFitness(self):
        print(self.fitness)
        

#基础参数
N = 200  #种群内个体数目
mut = 0.3  #突变概率
acr = 0.2  #交叉概率

pop = {}  #存储染色体的字典
for i in range(N):
    pop['chrom'+str(i)] = Chrom()
chromNodes = 4  #染色体节点数（变量个数）
iterNum = 10000  #迭代次数
chromRange = [[0, 10], [0, 10], [0, 10], [0, 10]]  #染色体范围
aveFitnessList = []  #平均适应度
bestFitnessList = []  #最优适应度


#初始染色体
pop = Genetic.initialize(pop, chromNodes, chromRange)
pop = Fitness.calFitness(pop)  #计算适应度
bestChrom = Genetic.findBest(pop)  #寻找最优染色体
bestFitnessList.append(bestChrom[1])  #将当前最优适应度压入列表中
aveFitnessList.append(Genetic.calAveFitness(pop, N))  #计算并存储平均适应度


 
#开始迭代
for t in range(iterNum):
    
    #print(bestChrom)
    #染色体突变
    pop = Genetic.mutChrom(pop, mut, chromNodes, bestChrom, chromRange)
    #染色体交换
    pop = Genetic.acrChrom(pop, acr, chromNodes)
    #寻找最优
    nowBestChrom = Genetic.findBest(pop)
    #比较前一个时间的最优和现在的最优
    bestChrom = Genetic.compareChrom(nowBestChrom, bestChrom)
    #寻找与替换最劣
    worseChrom = Genetic.findWorse(pop)
    pop[worseChrom[0]].chrom = pop[bestChrom[0]].chrom.copy()
    pop[worseChrom[0]].fitness = pop[bestChrom[0]].fitness
    #存储最优与平均
    bestFitnessList.append(bestChrom[1])
    aveFitnessList.append(Genetic.calAveFitness(pop, N))
    
x = list(range(iterNum+1))

plt.figure(1)
plt.plot(x, aveFitnessList)
plt.plot(x, bestFitnessList)

print(bestChrom[1])

endTime = datetime.datetime.now()

print((endTime-startTime).seconds)


