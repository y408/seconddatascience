import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
edu = pd.read_csv(r'C:\Users\OMOTOSHO\Documents\data scientist\introduction-datascience-python-book\files\ch07/educ_figdp_1_Data.csv',
                  na_values= ':',
                  usecols=[ "TIME","GEO","Value"])
print(edu)
# print(edu.tail(8))
# print(edu.describe())
# print(edu['GEO'])
# print(edu[10:20])
# print(edu.loc[90:94, ['TIME','GEO']])
# # # print(edu[edu['Value'] > 6.5].tail())
# print(edu[edu['Value'].isnull()].head())
# print("pandas max fuction", end=":")
# print(edu['Value'].max())
# print()
# print("pandas max fuction")
# s = edu['Value']/100
# print(s.head())
# e =edu['Value']. apply(np.sqrt)
# print(e)
# z = edu['Value']. apply(lambda d: d**4/4)
# print(z.head())
# edu ['Valuenorm'] = edu['Value']/(edu['Value'].max())
# print(edu.head())
# print(edu.tail(8 ))
# edu ['Valuenorm'] = edu['Value']/(edu['Value'].max())
# edu.drop('Value',axis = 1 ,inplace=False)
# print(edu.tail())
# edu = edu.append({'TIME' : 2000 , 'GEO' : 'africa', 'Value':19},
#                  ignore_index = True)
# print(edu.tail())
# edu.drop(max(edu.index), axis = 0, inplace = True)
# print(edu.head())
#
# eduDrop = edu.dropna(how = 'any', subset = ["Value"])
# print(eduDrop. head())
# edufiiledna = edu.fillna(value = {"Value": 1.4})
# print(edufiiledna.tail(9))
# edu.sort_index( by = 'Value', ascending=False, inplace=True)
# print(edu.head())
# edu.sort_index( axis = 1, ascending = False , inplace = True)
# print(edu.tail())
filtered_data = edu[edu["TIME"] > 2005]
pivedu = pd. pivot_table( filtered_data , values = 'Value',
                          index = ['GEO'] ,
                          columns = ['TIME'])
# pivedu.loc[['Japan ','Belgium '],[2006,2002]]
# s=(pivedu.loc[[ 'Belgium','Switzerland'], [2006,2011]])
# print(s)
# pivedu= pivedu.dropna()
# print(pivedu)
# t= pivedu.rank(ascending=False, method='first')
# print(t)
# gt=pivedu.sum(axis=1)
# lp=gt.rank(ascending=False,method='dense').sort_values()
# print(lp)
# totalSum = pivedu.sum(axis = 1).sort_values(ascending = False)
# print(totalSum)
# fe = totalSum. plot(kind = 'bar', style = 'g', alpha = 0.1,title = "Total Values for Country")
# my_colors = ['b', 'r', 'g', 'y', 'm', 'c']
# ax = pivedu. plot(kind = 'barh',
#                          stacked = True ,
#                          color = my_colors)
# ax.legend(loc = 'center left', bbox_to_anchor = (1, .4))
# plt.show(ax)


