import numpy as np

list1 = ["A","B","C","D","E"]
list2=["a","b","c"]

probabilities1 = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
probabilities2 = [0.05]





arr = np.random.choice(list1, size=5, p=probabilities1)

print(arr)
