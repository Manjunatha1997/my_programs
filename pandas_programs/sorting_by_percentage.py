import pandas as pd 

data = pd.read_csv("/home/manju/python_programs/sel/results1_fifth_sem.csv") 


sort = data.sort_values(by='GSGPA',ascending=False)

print(sort.head(5))
