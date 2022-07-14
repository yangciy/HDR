import pandas as pd

temp = pd.Series([-20,-10,10,20],index=['Jan',"Feb","Mar","Apr"])
print(temp[0])
print(temp['Feb'])
