import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import mean_squared_error

#one of table
Pl = A.loc[:, ['K', 'HT',	'Wt',	'TOI',	'TOI/G',	'GP',	'G', 'G/G',	 'A', 'A/G', 	'Pts', 'Pts/G', '+/-',	'PIM',	'PIM/G', 'Shifts',	'Shifts/G', 'Sh', 'Sh/G',	'SH%',	'SOS',	'MsS',	'OPS',	'DPS',	'PS',	'Match',	'Misc',	'G Misc',	'PDO',	'Corsi',	'RelC',	'GvA',	'TkA',	'Diff', 'Diff/G', 'Blocked',	'Bl/G', 'Hits',	'Hits/G', 'FO%',	'FOW',	'FOL',	'FG',	'GWG',	'OTG',	'ENG',	'PSG', 'AdvG', 'RelG',	'SOG', 'CapHit' ]]
#players
Pl = A.loc[:, ['K', 'HT',	'Wt',	'GS',	'W',	'L',	'OT',	'SA',	'SV',	'GAA',	'SV%',	'GR',	'PIM',	'MIN',	'SO',	'StGA',	'StSV',	'StMIN',	'StSV%',	'StGAA',	'QS',	'QS%',	'ReGA',	'ReSV',	'ReMIN',	'ReGAA',	'ReSV%',	'GPS',	'ESA',	'ESSV%',	'SHSA',	'SHSV%',	'PPSA',	'PPSV%',	'SOW',	'SOL',	'SSA',	'SGA',	'SOSV%', 'CapHit']]
#goalies
Pl = Pl.fillna(0)
# replaces NA with zero
Pl[Pl<0] = 0
# replaces negative values with zero
Pl['CapHit'] = Pl['CapHit']/1000000
#Pl = Pl.sort('CapHit')
Pl['ID'] = np.arange(1,(len(Pl.index)+1),1)

Pl_array = Pl.values
X_Pl = Pl.loc[:, ['K', 'TOI/G', 'G/G', 'Pts/G', 'SH%', 'PS', 'Corsi', 'AdvG']]
#forward
X_Pl = Pl.loc[:, ['K', 'TOI/G', 'Pts/G', '+/-', 'PIM/G', 'RelC', 'Diff/G', 'Bl/G', 'Hits/G']]
#defenseman
X_Pl = Pl.loc[:, ['K', 'GS', 'W', 'GAA', 'SV%', 'QS%', 'GPS', 'MIN']]
#goalies
Y_Pl = Pl_array[:,51]#target attribute
#players
Y_Pl = Pl_array[:,40]#target attribute
#goalies
Y_Pl = Y_Pl.astype(float)

#Linear regression
lin = LinearRegression() 
lin.fit(X_Pl, Y_Pl) 

plt.scatter(Pl.ID, Y_Pl, color = 'blue') 
plt.plot(Pl.ID, lin.predict(X_Pl), color = 'green') 
plt.title('Linear Regression') 
plt.xlabel('ID') 
plt.ylabel('Cap Hit') 
plt.show() 

#Polynomial regression
poly = PolynomialFeatures(degree = 3) 
X_poly = poly.fit_transform(X_Pl) 
poly.fit(X_poly, Y_Pl) 
lin2 = LinearRegression() 
lin2.fit(X_poly, Y_Pl) 
Y_Poly = lin2.predict(X_poly)

lin2.score(X_poly,Y_Pl)
rmse = np.sqrt(mean_squared_error(Y_Pl,Y_Poly))
print(lin2.score(X_poly,Y_Pl)*100,'%')
print(rmse)

plt.plot(Pl.ID, lin2.predict(poly.fit_transform(X_Pl)), color = 'red') 
plt.scatter(Pl.ID, Y_Pl, color = 'blue')
plt.title('Polynomial Regression') 
plt.xlabel('ID') 
plt.ylabel('Cap Hit') 
plt.show() 
