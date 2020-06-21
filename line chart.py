from numpy import random
import numpy as np
from scipy import stats
X = random.normal(size=5)


print(X)
mean = np. mean(X)
medium = np. median(X)
mode = stats. mode(X)
print('Mean is ', mean)
print('Median is ', medium)