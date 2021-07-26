import csv
import ploty.figure_factory as ff
import pandas as pd

df=pd.read_csv("data.csv")
fig=ff.create_distplot([df["Mobile Brand"].tolist],["Height"],show_heist=False)
fig.show()