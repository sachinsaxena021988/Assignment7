#import numpy module
import numpy as np

#define array to for input value
x=np.array([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150])

#define k as number of column 
k=3

#define mean array to add the mean
meanarray =[]

#define range to loop through numpy array
for i in range(len(x)-k+1):
    
    #internal sum of all kth value
    internalSum =0.0
    
    for j in range(i,i+k):
        internalSum =internalSum+x[j]
        
    meanarray.append(internalSum/k)
    
#print mean array
print(meanarray)

        
        
        
        
        
        
   