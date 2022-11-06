#!/usr/bin/python

import requests as req

resp = req.get("https://api.open-meteo.com/v1/forecast?latitude=41.85&longitude=-87.65&hourly=temperature_2m")
data = resp.json()
dict_temp = dict(zip(data['hourly']['time'],data['hourly']['temperature_2m']))
#print(dict_temp[[k for k in dict_temp.keys() if k.endswith("11:00")][1]])
print()


# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

# Example 1:

# Input: timePoints = ["23:59","00:00"]
# Output: 1


# Example 2:

# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0

# Example 3:

# Input: timePoints = ["11:00", "10:00","20:00"]
# Output: 60

# Example 4:

# Input: timePoints = ["01:00", "19:00","23:00"]
# Output: 120


# Example 5:

# Input: timePoints = ["11:00", "01:30", "05:00"]
# Output: 210


# Constraints:

# 2 <= timePoints.length <= 2 ** 104
# timePoints[i] is in the format "HH:MM".

from pickle import FALSE
from typing import List

## max time difference can be 12 h 

class Solution:
    def morethan2(self, timePoints):
        if len(timePoints)!=len(set(timePoints)): return 0 #covered duplicates 
        res=[]
        d=dict()
        for x in range(0,1500): d[x]=9 
        #print(d) 
        for time in timePoints:
            h,m=time.split(":")
            res_h = int(h)
            #if res_h<12: res_h=res_h+24
            d[(res_h*60+int(m))]=888   
            #res.append(int(h)*60+int(m))
            #clean-up duplicates ? or i am returning 0
        #print(sorted(res))  # how to make it O(n)? - I was suffering a bit :) 
        res = [k for k,v in d.items() if v == 888]
        print(res)
        answ0=[]
        for i in range(len(res)-1):
            answ0.append(res[i+1]-res[i]) 
        #print(min(answ0))        
        return min(answ0)
    def only_two(self, timePoints):
        res=[]
        for time in timePoints:
            h,m=time.split(":")
            n_h = int(h) 
            if n_h<12: n_h+=24
            number = n_h*60+int(m)           
            res.append(number)    
        return abs(res[0]-res[1])

    def findMinDifference(self, timePoints: List[str]) -> int:
        if(len(timePoints)>2):
            return self.morethan2(timePoints)
        return self.only_two(timePoints)

timePoints = ["00:00","23:59","00:00"]#["23:59","01:00"]# - here will be buggy, the this test cases # ["11:00", "01:30", "05:00"]# => [660, 90, 300]
s = Solution()
result = s.findMinDifference(timePoints=timePoints)
print(result)