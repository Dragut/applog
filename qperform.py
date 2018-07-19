# -*- coding: utf-8 -*-
"""
Created on Mon Jul 09 11:21:36 2018

@author: s59018
"""

import exec_anaconda
exec_anaconda.exec_anaconda()
import numpy as np
from scipy.optimize import curve_fit
import splunk.Intersplunk 
def func(r,  q):
  #return a * np.exp(-b * x)c
  return  1-np.exp(-q * r) 

def queueanalyzer(percentiles):
     if len(percentiles)<10:
         exit(1)
     x=np.arange(0.1,1.1,0.1)
     x[9]=0.95
     popt, pcov=curve_fit(func, percentiles,x)
     return popt[0]
# this call populates the results variable with all the events passed into the search script:
results,dummyresults,settings = splunk.Intersplunk.getOrganizedResults()

# Iterate over all the events:

  # for each results, add a 'shape' attribute, calculated from the raw event text
for result in results:
       arr=np.arange(10,dtype=float)
       indexcount=0
       keylist=['perc10(resp)', 'perc20(resp)', 'perc30(resp)', 'perc40(resp)', 'perc50(resp)', 'perc60(resp)', 'perc70(resp)', 'perc80(resp)', 'perc90(resp)', 'perc95(resp)']
       for name in keylist:
           arr[indexcount]=result[name]
           indexcount+=1
       result["QueueSpeed"] =queueanalyzer(arr)
  # output results#list(result.values())# 
splunk.Intersplunk.outputResults(results)

