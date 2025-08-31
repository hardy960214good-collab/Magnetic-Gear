#%% 匯入模組
from vpython import *
import time
import sympy as smp
import math
import numpy as np
import matplotlib.pyplot as plt

#%% 匯入數值解
path = r"C:\Users\hardy\Desktop\Datas\英物\10. Magnetic Gear\Numerical Solution.txt" #檔案位置
data = [] #拿來接收的陣列

with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip() #拆解匯入的檔案
        if line:
            data.append(eval(line)) #逐格添入數值解[時間,角度1,角度2,角速度1,角速度2]
f.close()

#%% 設定變數

d = data[0][0] #指尖陀螺距離
r = data[0][1] #指尖寬度
l = data[0][2] #指尖長度
dt = data[0][3] #時間間隔
data.remove(data[0]) #刪除陣列中暫存變數那項

#%% 動畫物件

#背景
scene = canvas(title="Magnetic Gear", width=1100, height=600, x=0, y=0, background=color.white)

#指尖陀螺1
color1 = color.red #指尖陀螺1的顏色
g11 = cylinder(pos=vec(-d/2,0,0),axis=vec(l,0,0),color=color1,radius=r/2)
g12 = cylinder(pos=vec(-d/2,0,0),axis=vec(l,0,0),color=color1,radius=r/2)
g13 = cylinder(pos=vec(-d/2,0,0),axis=vec(l,0,0),color=color1,radius=r/2)

#指尖陀螺2
color2 = color.blue #指尖陀螺2的顏色
g21 = cylinder(pos=vec(d/2,0,0),axis=vec(l,0,0),color=color2,radius=r/2)
g22 = cylinder(pos=vec(d/2,0,0),axis=vec(l,0,0),color=color2,radius=r/2)
g23 = cylinder(pos=vec(d/2,0,0),axis=vec(l,0,0),color=color2,radius=r/2)

#%% 跑動畫
for n in data:
    the1 = n[1]
    the2 = n[2]
    
    #指尖陀螺1的角度
    g11.axis=vec(l*np.cos(the1),0,l*np.sin(the1))
    g12.axis=vec(l*np.cos(the1+np.radians(120)),0,l*np.sin(the1+np.radians(120)))
    g13.axis=vec(l*np.cos(the1-np.radians(120)),0,l*np.sin(the1-np.radians(120)))
    
    #指尖陀螺2的角度
    g21.axis=vec(l*np.cos(the2),0,l*np.sin(the2))
    g22.axis=vec(l*np.cos(the2+np.radians(120)),0,l*np.sin(the2+np.radians(120)))
    g23.axis=vec(l*np.cos(the2-np.radians(120)),0,l*np.sin(the2-np.radians(120)))
    
    #停頓dt
    time.sleep(dt*0.75)

#%% 匯出變數(複製貼到Excel繪圖)
t = 0
plot_time  = []  #時間
plot_the1 = []   #角度1
plot_the2 = []   #角度2
plot_the1_d = [] #角速度1
plot_the2_d = [] #角速度2

#匯入資料
for n in data:
    plot_the1.append(n[1])
    plot_the2.append(n[2])
    plot_the1_d.append(n[3])
    plot_the2_d.append(n[4])
    plot_time.append(t)
    t+=dt

#繪圖: (x軸,y軸,顏色="?!")
plt.plot(plot_time,plot_the1,color='pink')
plt.plot(plot_time,plot_the2,color='palevioletred')
plt.plot(plot_time,plot_the1_d,color='mediumvioletred')
plt.plot(plot_time,plot_the2_d,color='darkmagenta')

plt.xlabel("Time (s)")     #x軸標題
plt.ylabel("rad & rad/s") #y軸標題
plt.show() #秀出圖表

#%%