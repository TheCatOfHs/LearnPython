# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 23:45:36 2017

@author: vento
"""

import Genetic
import Fitness

#染色体的类
class Chrom:
    chrom = []
    fitness = 0
    
    def showChrom(self):
        print(self.chrom)
    
    def showFitness(self):
        print(self.chrom)
        

#基础参数
N = 20  #种群内个体数目
pop = {}  #存储染色体的字典
for i in range(20):
    pop['chrom'+str(i)] = Chrom()
chromNodes = 4  #染色体节点数（变量个数）
iterNum = 100  #迭代次数
chromRange = [[0, 10], [0, 10], [0, 10], [0, 10]]  #染色体范围
aveFitnessList = []  #平均适应度
bestFitnessList = []  #最优适应度


#初始染色体
pop = Genetic.initialize(pop, chromNodes, chromRange)
pop = Fitness.calFitness(pop)  #计算适应度
bestChrom = Genetic.findBest(pop)  #寻找最优染色体
bestFitnessList.append(bestChrom[chromNodes])  #将当前最优适应度压入列表中
aveFitnessList.apped(Genetic.calAveFitness(pop, N))  #计算平均适应度




