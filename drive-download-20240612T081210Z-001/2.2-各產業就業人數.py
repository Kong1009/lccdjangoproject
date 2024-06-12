# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:04:24 2024

@author: user
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.font_manager import fontManager
from matplotlib.font_manager import FontProperties as font

data = pd.read_csv('各產業就業人口.csv', index_col=0, encoding='Big5')

plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

fig = plt.figure()

fig, ax = plt.subplots(3,3)


x = data['製造業 ']
ax[0,0].set_title('製造業 ', size = 10, color = "maroon")
ax[0,0].plot(x)

y = data['批發及零售業 ']
ax[0,1].set_title('批發及零售業 ', size = 10, color = "maroon")
ax[0,1].plot(y)

b = data['農、林、漁、牧業 ']
ax[0,2].set_title('農、林、漁、牧業 ', size = 10, color = "maroon")
ax[0,2].plot(b)

z = data['營造業 ']
ax[1,0].set_title('營造業 ', size = 10, color = "maroon")
ax[1,0].plot(z)

a = data['住宿及餐飲業 ']
ax[1,1].set_title('住宿及餐飲業 ', size = 10)
ax[1,1].plot(a)

c = data['教育服務業 ']
ax[1,2].set_title('教育服務業 ', size = 10)
ax[1,2].plot(c)

d = data['運輸及倉儲業 ']
ax[2,0].set_title('運輸及倉儲業 ', size = 10)
ax[2,0].plot(d)

e = data['醫療保健及社會工作服務業 ']
ax[2,1].set_title('醫療保健及社會工作服務業 ', size = 10)
ax[2,1].plot(e)

x = data['其他服務業 ']
ax[2,2].set_title('其他服務業 ', size = 10)
ax[2,2].plot(x)


plt.tight_layout()


plt.savefig('2.2-各產業就業人數.png')






