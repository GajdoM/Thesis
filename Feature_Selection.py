import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

#one of table
Pl = Players.loc[:, ['HT',	'Wt',	'TOI',	'TOI/G',	'GP',	'G', 'G/G',	 'A', 'A/G', 	'Pts', 'Pts/G', '+/-',	'PIM',	'PIM/G', 'Shifts',	
'Shifts/G', 'Sh', 'Sh/G',	'SH%',	'SOS',	'MsS',	'OPS',	'DPS',	'PS',	'Match',	'Misc',	'G Misc',	'PDO',	'Corsi',	'RelC',	'GvA',	
'TkA',	'Diff', 'Diff/G', 'Blocked',	'Bl/G', 'Hits',	'Hits/G', 'FO%',	'FOW',	'FOL',	'FG',	'GWG',	'OTG',	'ENG',	'PSG', 'AdvG', 
'RelG',	'SOG', 'CapHit' ]]
# replaces negative values with zero
Pl[Pl<0] = 0
Pl = Pl.fillna(0)
array = Pl.values
X = array[:,0:48]
Y = array[:,49]

###MODEL1 - Univariate Selection
# k = 2 -> numer of best attributes
test = SelectKBest(score_func=chi2, k=5)
fit = test.fit(X, Y)

# precision = numer of decimal points
np.set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(X)
print(features[0:5,:])
# detects the strongest relationship with the output variable

###MODEL - Recursive Feature Elimination
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
rfe = RFE(model, 2)
fit = rfe.fit(X, Y)

print("Num Features: %d") % fit.n_features_
print("Selected Features: %s") % fit.support_
print("Feature Ranking: %s") % fit.ranking_
#The Recursive Feature Elimination (or RFE) works by recursively removing attributes 
#and building a model on those attributes that remain.
#It uses the model accuracy to identify which attributes (and combination of attributes) 
#contribute the most to predicting the target attribute.

###MODEL - Principal Component Analysis
from sklearn.decomposition import PCA

pca = PCA(n_components=10)
fit = pca.fit(X)

print("Explained Variance: %s"), fit.explained_variance_ratio_
print(fit.components_)
#The property of PCA is that you can choose the number of dimensions or principal component in the transformed result

##MODEL - Feature Importance
from sklearn.ensemble import ExtraTreesClassifier

model = ExtraTreesClassifier()
model.fit(X_, Yl)
print(model.feature_importances_, Goalies_names)
a = model.feature_importances_
print(np.around(a,3))
#how important are the individual attributes
