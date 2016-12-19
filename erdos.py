
from math import sqrt
from vectorgenetics import VectorEvolution
    
#target error function   
def evaluator(x):
    error = 0
    #2 for-loops iterating over every pair of points
    for i in range(x.shape[0]-1):
        x1 = x[i][0]
        y1 = x[i][1]
        for j in range(i+1, x.shape[0]):
            x2 = x[j][0]
            y2 = x[j][1]
            #distance between points
            d = sqrt((x2-x1)**2+(y2-y1)**2)
            #ideally d=1 for all pairs. then error=0. 
            #(though in 2d this can only be possible for less than 3 points)
            error += (1-d)**2
    return error    
    

POINTS_COUNT = 10 #10 2d points   
    
ve = VectorEvolution(evaluator, (POINTS_COUNT,2,))
ve.evolve() 
