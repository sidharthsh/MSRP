import os
import math
import random
import matplotlib.pyplot as plt
import csv

def get_power_set(s):
  power_set=[[]]
  for elem in s:
    for sub_set in power_set:
      power_set=power_set+[list(sub_set)+[elem]]
  return power_set

base = 3
possibleforbidden = [1, 2]
possiblelimits = [1000, 10000, 100000]
while (base < 10):
    allforbidden = get_power_set(possibleforbidden)
    for forbidden in allforbidden:
        if (forbidden == []):
            continue
        for limit in possiblelimits:
            x = []
            filename = "b" + str(base) + "_" + str(forbidden) + "_till_" + str(limit) + ".txt"
            picname = "GRAPH_b" + str(base) + "_" + str(forbidden) + "_till_" + str(limit) + ".png" 
            with open(filename,'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=',')
                for row in plots:
                     x.append(int(row[0]))  
            
                plt.plot(x)
                plt.xlabel('nth quotient set number')
                plt.savefig("GRAPH_" + picname)
                plt.close()


    base = base + 1
    possibleforbidden.append(base - 1)
