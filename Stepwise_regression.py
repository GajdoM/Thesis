from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#####Players

#one of table
Pl = Players.loc[:, ['TOI',	'TOI/G',	'GP',	'G', 'G/G',	 'A', 'A/G', 	'Pts', 'Pts/G', '+/-',	'PIM',	'PIM/G', 'Shifts',	
'Shifts/G', 'Sh', 'Sh/G',	'SH%',	'SOS',	'MsS',	'OPS',	'DPS',	'PS',	'Match',	'Misc',	'G Misc',	'PDO',	'Corsi',	'RelC',	'GvA',	
'TkA',	'Diff', 'Diff/G', 'Blocked',	'Bl/G', 'Hits',	'Hits/G', 'FO%',	'FOW',	'FOL',	'FG',	'GWG',	'OTG',	'ENG',	'PSG', 'AdvG', 
'RelG',	'SOG', 'CapHit' ]]
Pl = Pl.fillna(0)
# replaces NA with zero
Pl[Pl<0] = 0
# replaces negative values with zero

Pl_array = Pl.values
X_Pl = Pl.loc[:, ['TOI',	'TOI/G',	'GP',	'G', 'G/G',	 'A', 'A/G', 	'Pts', 'Pts/G', '+/-',	'PIM',	'PIM/G', 'Shifts',	
'Shifts/G', 'Sh', 'Sh/G',	'SH%',	'SOS',	'MsS',	'OPS',	'DPS',	'PS',	'Match',	'Misc',	'G Misc',	'PDO',	'Corsi',	'RelC',	'GvA',	
'TkA',	'Diff', 'Diff/G', 'Blocked',	'Bl/G', 'Hits',	'Hits/G', 'FO%',	'FOW',	'FOL',	'FG',	'GWG',	'OTG',	'ENG',	'PSG', 'AdvG', 
'RelG',	'SOG' ]]
Y_Pl = Pl_array[:,49] #target attribute
Y_Pl = Y_Pl.astype(int)

knn = KNeighborsClassifier(n_neighbors=2)
lr = LinearRegression()
# number of neighbors = 2

Players_names = ['TOI',	'TOI/G',	'GP',	'G', 'G/G',	 'A', 'A/G', 	'Pts', 'Pts/G', '+/-',	'PIM',	'PIM/G', 'Shifts',	
'Shifts/G', 'Sh', 'Sh/G',	'SH%',	'SOS',	'MsS',	'OPS',	'DPS',	'PS',	'Match',	'Misc',	'G Misc',	'PDO',	'Corsi',	'RelC',	'GvA',	
'TkA',	'Diff', 'Diff/G', 'Blocked',	'Bl/G', 'Hits',	'Hits/G', 'FO%',	'FOW',	'FOL',	'FG',	'GWG',	'OTG',	'ENG',	'PSG', 'AdvG', 
'RelG',	'SOG' ]
sfs1 = SFS(knn, 
           k_features=(1,49), 
           forward=True, 
           floating=False, 
           verbose=2,
           scoring='balanced_accuracy',
           cv=0)
#looking best combinations from 0 to 49 attributes

sfsPl = sfs1.fit(X_Pl, Y_Pl, custom_feature_names=Players_names)

sfsPl.subsets_
sfsPl.k_feature_idx_
sfsPl.k_feature_names_
sfsPl.k_score_

plot_sfs(sfsPl.get_metric_dict(), kind='std_err');
print('all subsets:\n', sfsPl.subsets_)
print('best combination (ACC: %.5f): %s\n' % (sfsPl.k_score_, sfsPl.k_feature_names_))

#####Goalies

#one of table
Gl = Goalies.loc[:, ['GS',	'W',	'L',	'OT',	'SA',	'SV',	'GAA',	'SV%',	'GR',	'PIM',	'MIN',	'SO',	'StGA',	'StSV',	
'StMIN',	'StSV%',	'StGAA',	'QS',	'QS%',	'ReGA',	'ReSV',	'ReMIN',	'ReGAA',	'ReSV%',	'GPS',	'ESA',	'ESSV%',	'SHSA',	'SHSV%',	
'PPSA',	'PPSV%',	'SOW',	'SOL',	'SSA',	'SGA',	'SOSV%',	'CapHit']]
Gl.astype(float)
Gl = Gl.fillna(0)
# replaces NA with zero
Gl[Gl<0] = 0
# replaces negative values with zero

Gl_array = Gl.values
X_Gl = Gl.loc[:, ['GS',	'W',	'L',	'OT',	'SA',	'SV',	'GAA',	'SV%',	'GR',	'PIM',	'MIN',	'SO',	'StGA',	'StSV',	'StMIN',	
'StSV%',	'StGAA',	'QS',	'QS%',	'ReGA',	'ReSV',	'ReMIN',	'ReGAA',	'ReSV%',	'GPS',	'ESA',	'ESSV%',	'SHSA',	'SHSV%',	'PPSA',
'PPSV%',	'SOW',	'SOL',	'SSA',	'SGA',	'SOSV%']]
Y_Gl = Gl_array[:,38]
Y_Gl = Y_Gl.astype(int)

knn = KNeighborsClassifier(n_neighbors=2)
lr = LinearRegression()
# number of neighbors = 2
Goalies_names = ['GS',	'W',	'L',	'OT',	'SA',	'SV',	'GAA',	'SV%',	'GR',	'PIM',	'MIN',	'SO',	'StGA',	'StSV',	'StMIN',	
'StSV%',	'StGAA',	'QS',	'QS%',	'ReGA',	'ReSV',	'ReMIN',	'ReGAA',	'ReSV%',	'GPS',	'ESA',	'ESSV%',	'SHSA',	'SHSV%',	'PPSA',	
'PPSV%',	'SOW',	'SOL',	'SSA',	'SGA',	'SOSV%']

sfs2 = SFS(knn, 
           k_features=(1,38), 
           forward=True, 
           floating=False, 
           verbose=2,
           scoring='balanced_accuracy',
           cv=0)
# looking best combinations from 0 to 38 attributes

sfsGl = sfs2.fit(X_Gl, Y_Gl, custom_feature_names = Goalies_names)

sfsGl.subsets_
sfsGl.k_feature_idx_
sfsGl.k_feature_names_
sfsGl.k_score_

plot_sfs(sfsGl.get_metric_dict(), kind='std_err');
print('all subsets:\n', sfsGl.subsets_)
print('best combination (ACC: %.5f): %s\n' % (sfsGl.k_score_, sfsGl.k_feature_names_))
