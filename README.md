# python-vector-genetics
Python class that implements genetic machine learning approach to select the fittest vector. 

```python
from vectorgenetics import VectorEvolution

def error_function(vector):
  return error

ve = VectorEvolution(error_function, vector_shape)
ve.evolve() 
```

Also example usage on Erdos problem. 
Aim is to find such set of points on plane that there are as much as possible distances of length 1 between them.
Result i got on set of 200 points after 300 generations. ( Computation was intense )
![result_200_points](https://github.com/trikota/python-vector-genetics/raw/master/figure_200.png)

You can find more description at
http://allmachineslearn.blogspot.com/2016/12/trying-to-solve-erdos-problem-with.html
