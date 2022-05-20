# -*- coding: utf-8 -*-
"""
Created on Thu May 19 18:30:52 2022

@author: oluchukwuadonu
"""

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import operator
df_1 = pd.read_csv(r"C:/buy-clicks.csv")
df_1.groupby('buyId').size()
Price_id =df_1.groupby('buyId').sum()
print(Price_id)
import matplotlib.pyplot as plt
import numpy as np
 
# Creating dataset
products = ['0', '1', '2',
        '3', '4', '5']
 
data = Price_id["price"]
 
 
# Creating explode data
explode = (0.1, 0.0, 0 , 0.2, 0.0, 0.2)
 
# Creating color parameters
colors = ( "orange", "indigo", "brown",
          "grey", "cyan", "beige")
 
# Wedge properties
wp = { 'linewidth' : 1, 'edgecolor' : "green" }
 
# Creating autocpt arguments
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d})".format(pct, absolute)
 
# Creating plot
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(data,
                                  autopct = lambda pct: func(pct, data),
                                  explode = explode,
                                  labels = products,
                                  shadow = True,
                                  colors = colors,
                                  startangle = 90,
                                  wedgeprops = wp,
                                  textprops = dict(color ="magenta"))
 
# Adding legend
ax.legend(wedges, products,
          title ="Buy Id",
          loc ="center left",
          bbox_to_anchor =(1, 0, 0.5, 1))
 
plt.setp(autotexts, size = 8, weight ="bold")
ax.set_title("Customizing pie chart")
 
# show plot
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import operator
df_3 = pd.read_csv(r"C:/game-clicks.csv")
New_column = 1 
df_3["New_column"] = New_column
df_3["timestamp"] = pd.to_datetime(df_3["timestamp"])
df_3["Time"] = df_3["timestamp"].dt.time
Daily = df_3.groupby([pd.Grouper(key='timestamp',freq='1D'),df_3.New_column]).size().reset_index(name='count')
Daily= Daily.drop([0 , 21])
import matplotlib.pyplot as plt

Days = Daily["timestamp"]
Counts = Daily["count"]
  
plt.plot(Days, Counts, color='red')
plt.title('Daily clicks count', fontsize=14)
plt.xlabel('Days', fontsize=14)
plt.ylabel('Number of clicks', fontsize=14)
plt.grid(True)
plt.xticks(rotation=90)
plt.show()