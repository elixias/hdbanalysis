#cd C:\Users\elixander_tan\AppData\Local\Programs\Python\Python36\

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("C:\\Users\\elixander_tan\\Desktop\\hdb\\data\\hdbData_22072019.csv", header=0)
dataset = pd.read_csv("C:\\Users\\elixander_tan\\Desktop\\hdb\\data\\hdbData_22072019.tsv", sep='\t', header=0)

#format currency
pd.set_option('display.float_format', lambda x: '%.3f' % x)

#total number of transactions
dataset['Town'].value_counts().plot.bar().figure.show();

dataset.describe()
       # AreaSQM  PricePSF       Price
# count 1538.000  1538.000    1538.000
# mean    95.637  4478.277  425277.245
# std      7.264  1346.407  120898.158
# min     75.000  2303.000  240000.000
# 25%     91.000  3584.000  345000.000
# 50%     93.000  4123.000  394000.000
# 75%    103.000  4876.000  458866.000
# max    121.000 11076.000 1038000.000

#Select minimum PricePSF grouped by Town
dataset.groupby('Town', as_index=False)['PricePSF'].min().sort_values('PricePSF')
df.groupby('Town', as_index=False, group_keys=True)['PricePSF'].min().sort_values('PricePSF').plot.bar(x='Town').figure.show()
#Select min, mean and max PricePSF grouped by Town
df.groupby('Town', as_index=False, group_keys=True)['PricePSF'].agg({'Low Value':'min','High Value':'max','Mean':'mean'})
df.groupby('Town', as_index=False, group_keys=True)['PricePSF'].agg({'Low Value':'min','High Value':'max','Mean':'mean'}).sort_values('Mean').plot.bar(x='Town').figure.show()

#sort by lowest PricePSF in AMK
df.loc[df['Town']=="Yishun"].sort_values('PricePSF')
df.loc[df['Town']=="Yishun"]['PricePSF'].plot.hist(bins=100).figure.show()

#histogram (general)
df['PricePSF'].plot.hist(bins=100).figure.show()

#relationship between PricePSF and Price
df.plot.scatter(x='PricePSF',y='Price').figure.show()

fig, axarr = plt.subplots(2, 1, figsize=(12, 8))
df.groupby('Town', as_index=False, group_keys=True)['PricePSF'].min().sort_values('PricePSF').plot.bar(x='Town',ax=axarr[1])
df['PricePSF'].plot.hist(bins=100,ax=axarr[0])
axarr[1].set_title('Minimum PricePSF')
axarr[0].set_title('Histogram of PricePSF (All Towns)')
plt.show()
plt.clf()


towns = df['Town'].unique()
min = df['PricePSF'].min()
max = df['PricePSF'].max()
slots = np.floor(len(towns)**(1/2)).astype(int)
fig, axarr = plt.subplots(slots+1, slots, figsize=(2, 2))
for i in range(0,len(towns)):
  rem=i%slots.astype(int)
  row=np.floor(i/slots).astype(int)
  df.loc[df['Town']==towns[i]]['PricePSF'].plot.hist(bins=100,ax=axarr[row,rem],title=towns[i],range=(min,max))

plt.tight_layout()
plt.show()