#========================================
"""
mydata = [10,50,20,88,90]

def data_analysis(values):
  m = 0
  sd = 0
  sum = 0
  n = len(mydata)
  for i in range(n):
    sum += values[i]
  m = sum/n

  ss = 0
  for i in range(n):
    ss+= (i-m)**2
  sd = (ss / (n-1))**0.5

  return (m,sd)

mean, std = data_analysis(mydata)
print(mean,std)
"""
#========================================
"""
import numpy as np

mydata = [10,50,20,88,90]

def np_analysis(values):
  mean = np.mean(values)
  std = np.std(values)
  return (mean, std)

mean, std = np_analysis(mydata)
print(mean,std)
"""

