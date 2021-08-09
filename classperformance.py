import pandas as pd
import csv 
import plotly.graph_objects as go 

df=pd.read_csv("D:/python/class107/data.csv")
print(df.groupby("level")["attempt"].mean())
#output:
#level
#Level 1    0.751445
#Level 2    0.863281
#Level 3    0.698113
#Level 4    0.734694
#Name: attempt, dtype: float64

#student  did perform well in level 3

fig= go.Figure(go.Bar(
    y=df.groupby("level")["attempt"].mean(),
    x=['Level 1','Level 2','Level 3','Level 4'],
    orientation='v'
    #if orientation='h' change y to x and x to y 
    )) 

fig.show()    