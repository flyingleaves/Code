# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math
import xlrd   #xlrd是用来识别Excel文件的插件
from  statistics import mean,stdev,pstdev,variance,pvariance

from prettytable import PrettyTable

def getData(filename):   #获取数据，通过对Excel中数据的行、列依次读取
    
    excel = xlrd.open_workbook(filename)
    sheet = excel.sheets()[0]     #获取第一个sheet
    ncols = sheet.ncols           #列数
    nrows = sheet.nrows           #行数
    x_data = 0
    y_data = 0
    xygroups=[]
    xy={'x':[],'y':[]}

    for i in range(0,ncols,2):
        for j in range(0,nrows):
            x_data = sheet.cell_value(j,i)   #第j行i列的数
            y_data = sheet.cell_value(j ,i + 1)  #第j行i+1列的数

            xy['x'].append(float(x_data))
            xy['y'].append(float(y_data))

        xygroups.append(xy)
        xy={'x':[],'y':[]}

    return xygroups

def staData(x,y):   #所需数据形式   
    xsta={'avg':None,'stdev':None,'pstdev':None,'var':None,'pvar':None}
    ysta={'avg':None,'stdev':None,'pstdev':None,'var':None,'pvar':None}

    xsta['avg']=mean(x)
    ysta['avg']=mean(y)

    xsta['stdev']=stdev(x)
    ysta['stdev']=stdev(y)

    xsta['pstdev']=pstdev(x)
    ysta['pstdev']=pstdev(y)

    xsta['var']=variance(x)
    ysta['var']=variance(y)

    xsta['pvar']=pvariance(x)
    ysta['pvar']=pvariance(y)

    r=np.corrcoef(x,y)[0, 1]

    return  xsta,ysta,r

def table(xygroups):   #制表
    table = PrettyTable(["data set",
                         "x-avg", "x-std", "x-pstd", "x-var","x-pvar",
                         "y-avg", "y-std", "y-pstd", "y-var","y-pvar",
                         "pearson_r"])     #确定横排参数
    for i in range(len(xygroups)):
        
        xsta,ysta,r=staData(xygroups[i]['x'], xygroups[i]['y'])

        table.add_row(["file" "%.0f" % i,
                   "%.3f" % xsta['avg'],
                   "%.3f" % xsta['stdev'],"%.3f" %xsta['pstdev'],
                   "%.3f" % xsta['var'],"%.3f" % xsta['pvar'],
                   "%.3f" % ysta['avg'],
                   "%.3f" % ysta['stdev'],"%.3f" % ysta['pstdev'],
                   "%.3f" % ysta['var'],"%.3f" % ysta['pvar'],
                   "%.3f" % r])               #参数输出，保留小数点后三位
    return table

def plot(xygroups):    #绘图

    figcount=len(xygroups)    
    figcol=2
    figrow=math.ceil(figcount/figcol) 
    fig=plt.figure(figsize=(12.0,8.0))  
    fig.subplots_adjust(left=0.05,right=0.95,bottom=0.05,top=0.95)

    for i in range(0,len(xygroups)):
        m,n = np.polyfit(xygroups[i]['x'],xygroups[i]['y'],1)
        predictedY = m*np.array(xygroups[i]['x']) + n
        fig.add_subplot(figrow, figcol,i+1)     #子图
        plt.plot(xygroups[i]['x'],xygroups[i]['y'], 'bo')   #根据拟合方程y=a*x+b绘图

        plt.title("Chart "+str(i)) #图表名，x、y轴的设置
        plt.xlabel('x')
        plt.ylabel('y')

        plt.plot(xygroups[i]['x'],predictedY,
                   label = ' y = '
                   + str(round(m, 5))+'*x+'+str(round(n, 5)))  #标签，即y=a*x+b的具体数值

        plt.legend(loc = 'best')

xygroups = getData('data.xlsx')

print("the original data:")
print(table(xygroups))

plot(xygroups)

plt.show()