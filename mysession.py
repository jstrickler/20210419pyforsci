# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('DATA/airport_boardings.csv', thousands=',')
df.columns
df['2001 Total'].plot()
plt.show()
with open('DATA/mary.txt') as mary_in:
    print(mary_in.read())
    
get_ipython().run_line_magic('lsmagic', '')
get_ipython().run_line_magic('pinfo', 'save')
