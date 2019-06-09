import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from datetime import date, timedelta
import datetime

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
matplotlib.style.use('ggplot')

G12 = pd.read_csv('C:\\Users\\NHL Goalies 2011-12.csv', sep=',', encoding= 'windows-1250')
G23 = pd.read_csv('C:\\Users\\NHL Goalies 2012-13.csv', sep=',', encoding= 'windows-1250')
G34 = pd.read_csv('C:\\Users\\NHL Goalies 2013-14.csv', sep=',', encoding= 'windows-1250')
G45 = pd.read_csv('C:\\Users\\NHL Goalies 2014-15.csv', sep=',', encoding= 'windows-1250')
G56 = pd.read_csv('C:\\Users\\NHL Goalies 2015-16.csv', sep=',', encoding= 'windows-1250')
G67 = pd.read_csv('C:\\Users\\NHL Goalies 2016-17.csv', sep=',', encoding= 'windows-1250')
G78 = pd.read_csv('C:\\Users\\NHL Goalies 2017-18.csv', sep=',', encoding= 'windows-1250')

today = date(2018,3,20)
G67['Age'] = round((today - (pd.to_datetime(G67['DOB']))) / timedelta(365.2425))
G78['Age'] = round((today - (pd.to_datetime(G78['DOB']))) / timedelta(365.2425))

# sort attributes
G1112 = G12.loc[:, ['First Name',	'Last Name', 'DOB', 'Age',	'Ctry',	'HT',	'Wt',	'C',	'Team',	'GS',	'W',	'L',	'OT',	'SA',	'SV',	'GAA',	'SV%',	'GR',	'PIM',	'MIN',	'SO',	'StGA',	'StSV',	'StMIN',	'StSV%',	'StGAA',	'QS',	'QS%',	'ReGA',	'ReSV',	'ReMIN',	'ReGAA',	'ReSV%',	'GPS',	'ESA',	'ESSV%',	'SHSA',	'SHSV%',	'PPSA',	'PPSV%',	'SOW',	'SOL',	'SSA',	'SGA',	'SOSV%', 'Status',	'Cap Hit'
]]
G1213 = G23.loc[:, ['First Name',	'Last Name', 'DOB', 'Age',	'Ctry',	'HT',	'Wt',	'C',	'Team',	'GS',	'W',	'L',	'OT',	'SA',	'SV',	'GAA',	'SV%',	'GR',	'PIM',	'MIN',	'SO',	'StGA',	'StSV',	'StMIN',	'StSV%',	'StGAA',	'QS',	'QS%',	'ReGA',	'ReSV',	'ReMIN',	'ReGAA',	'ReSV%',	'GPS',	'ESA',	'ESSV%',	'SHSA',	'SHSV%',	'PPSA',	'PPSV%',	'SOW',	'SOL',	'SSA',	'SGA',	'SOSV%', 'Status',	'Cap Hit'
]]
G1314 = G34.loc[:, ['First Name',	'Last Name', 'DOB', 'Age',	'Ctry',	'HT',	'Wt',	'C',	'Team',	'GS',	'W',	'L',	'OT',	'SA',	'SV',	'GAA',	'SV%',	'GR',	'PIM',	'MIN',	'SO',	'StGA',	'StSV',	'StMIN',	'StSV%',	'StGAA',	'QS',	'QS%',	'ReGA',	'ReSV',	'ReMIN',	'ReGAA',	'ReSV%',	'GPS',	'ESA',	'ESSV%',	'SHSA',	'SHSV%',	'PPSA',	'PPSV%',	'SOW',	'SOL',	'SSA',	'SGA',	'SOSV%', 'Status',	'Cap Hit'
]]
G1415 = G45.loc[:, ['First Name',	'Last Name', 'DOB', 'Age',	'Ctry',	'HT',	'Wt',	'C',	'Team',	'GS',	'W',	'L',	'OT',	'SA',	'SV',	'GAA',	'SV%',	'GR',	'PIM',	'MIN',	'SO',	'StGA',	'StSV',	'StMIN',	'StSV%',	'StGAA',	'QS',	'QS%',	'ReGA',	'ReSV',	'ReMIN',	'ReGAA',	'ReSV%',	'GPS',	'ESA',	'ESSV%',	'SHSA',	'SHSV%',	'PPSA',	'PPSV%',	'SOW',	'SOL',	'SSA',	'SGA',	'SOSV%', 'Status',	'Cap Hit'
]]
G1516 = G56.loc[:, ['First Name',	'Last Name', 'DOB', 'Age', 'Ctry',	'HT',	'Wt',	'C',	'Team',	'GS',	'W',	'L',	'OT',	'SA',	'SV',	'GAA',	'SV%',	'GR',	'PIM',	'MIN',	'SO',	'StGA',	'StSV',	'StMIN',	'StSV%',	'StGAA',	'QS',	'QS%',	'ReGA',	'ReSV',	'ReMIN',	'ReGAA',	'ReSV%',	'GPS',	'ESA',	'ESSV%',	'SHSA',	'SHSV%',	'PPSA',	'PPSV%',	'SOW',	'SOL',	'SSA',	'SGA',	'SOSV%', 'Status',	'Cap Hit'
]]
G1617 = G67.loc[:, ['First Name',	'Last Name', 'DOB', 'Age',	'Ctry',	'HT',	'Wt',	'C',	'Team',	'GS',	'W',	'L',	'OT',	'SA',	'SV',	'GAA',	'SV%',	'GR',	'PIM',	'MIN',	'SO',	'StGA',	'StSV',	'StMIN',	'StSV%',	'StGAA',	'QS',	'QS%',	'ReGA',	'ReSV',	'ReMIN',	'ReGAA',	'ReSV%',	'GPS',	'ESA',	'ESSV%',	'SHSA',	'SHSV%',	'PPSA',	'PPSV%',	'SOW',	'SOL',	'SSA',	'SGA',	'SOSV%', 'Status',	'Cap Hit'
]]
G1718 = G78.loc[:, ['First Name',	'Last Name', 'DOB', 'Age',	'Ctry',	'HT',	'Wt',	'C',	'Team',	'GS',	'W',	'L',	'OT',	'SA',	'SV',	'GAA',	'SV%',	'GR',	'PIM',	'MIN',	'SO',	'StGA',	'StSV',	'StMIN',	'StSV%',	'StGAA',	'QS',	'QS%',	'ReGA',	'ReSV',	'ReMIN',	'ReGAA',	'ReSV%',	'GPS',	'ESA',	'ESSV%',	'SHSA',	'SHSV%',	'PPSA',	'PPSV%',	'SOW',	'SOL',	'SSA',	'SGA',	'SOSV%', 'Status',	'Cap Hit'
]]

G1112['Season'] = '11/12'
G1213['Season'] = '12/13'
G1314['Season'] = '13/14'
G1415['Season'] = '14/15'
G1516['Season'] = '15/16'
G1617['Season'] = '16/17'
G1718['Season'] = '17/18'

# join table
frames = [G1112, G1213, G1314, G1415, G1516, G1617, G1718]
Goalies = pd.concat(frames)
Goalies.rename(columns={'Cap Hit': 'CapHit'}, inplace=True)

Goalies["SV%"] = Goalies["SV%"].convert_objects(convert_numeric=True)
Goalies["QS%"] = Goalies["QS%"].convert_objects(convert_numeric=True)
Goalies["SOSV%"] = Goalies["SOSV%"].convert_objects(convert_numeric=True)

H12 = pd.read_csv('C:\\Users\\NHL 2011-12.csv', sep=',', encoding= 'windows-1250')
H23 = pd.read_csv('C:\\Users\\NHL 2012-13.csv', sep=',', encoding= 'windows-1250')
H34 = pd.read_csv('C:\\Users\\NHL 2013-14.csv', sep=',', encoding= 'windows-1250')
H45 = pd.read_csv('C:\\Users\\NHL 2014-15.csv', sep=',', encoding= 'windows-1250')
H56 = pd.read_csv('C:\\Users\\NHL 2015-16.csv', sep=',', encoding= 'windows-1250')
H67 = pd.read_csv('C:\\Users\\NHL 2016-17.csv', sep=',', encoding= 'windows-1250', header = 2)
H78 = pd.read_csv('C:\\Users\\NHL 2017-18.csv', sep=',', encoding= 'windows-1250', header = 2)

today = date(2018,3,20)
H67['Age'] = round((today - (pd.to_datetime(H67['DOB']))) / timedelta(365.2425))
H78['Age'] = round((today - (pd.to_datetime(H78['DOB']))) / timedelta(365.2425))

H1112 = H12.loc[:, ['First Name',	'Last Name',	'DOB', 'Age',	'Ctry',	'Team',	'Pos',	'S',	'HT',	'Wt',	'TOI',	'TOI/G',	'GP',	'G',	'A',	'Pts',	'+/-',	'PIM',	'Shifts',	'Sh',	'SH%',	'SOS',	'MsS',	'OPS',	'DPS',	'PS',	'Match',	'Misc',	'G Misc',	'PDO',	'Corsi',	'RelC',	'GvA',	'TkA',	'Blocked',	'Hits',	'FO%',	'FOW',	'FOL',	'1G',	'GWG',	'OTG',	'ENG',	'PSG',	'SOG',	'Status',	'Cap Hit'
]]
H1213 = H23.loc[:, ['First Name',	'Last Name',	'DOB', 'Age',	'Ctry',	'Team',	'Pos',	'S',	'HT',	'Wt',	'TOI',	'TOI/G',	'GP',	'G',	'A',	'Pts',	'+/-',	'PIM',	'Shifts',	'Sh',	'SH%',	'SOS',	'MsS',	'OPS',	'DPS',	'PS',	'Match',	'Misc',	'G Misc',	'PDO',	'Corsi',	'RelC',	'GvA',	'TkA',	'Blocked',	'Hits',	'FO%',	'FOW',	'FOL',	'1G',	'GWG',	'OTG',	'ENG',	'PSG',	'SOG',	'Status',	'Cap Hit'
]]
H1314 = H34.loc[:, ['First Name',	'Last Name',	'DOB', 'Age',	'Ctry',	'Team',	'Pos',	'S',	'HT',	'Wt',	'TOI',	'TOI/G',	'GP',	'G',	'A',	'Pts',	'+/-',	'PIM',	'Shifts',	'Sh',	'SH%',	'SOS',	'MsS',	'OPS',	'DPS',	'PS',	'Match',	'Misc',	'G Misc',	'PDO',	'Corsi',	'RelC',	'GvA',	'TkA',	'Blocked',	'Hits',	'FO%',	'FOW',	'FOL',	'1G',	'GWG',	'OTG',	'ENG',	'PSG',	'SOG',	'Status',	'Cap Hit'
]]
H1415 = H45.loc[:, ['First Name',	'Last Name',	'DOB', 'Age',	'Ctry',	'Team',	'Pos',	'S',	'HT',	'Wt',	'TOI',	'TOI/G',	'GP',	'G',	'A',	'Pts',	'+/-',	'PIM',	'Shifts',	'Sh',	'SH%',	'SOS',	'MsS',	'OPS',	'DPS',	'PS',	'Match',	'Misc',	'G Misc',	'PDO',	'Corsi',	'RelC',	'GvA',	'TkA',	'Blocked',	'Hits',	'FO%',	'FOW',	'FOL',	'1G',	'GWG',	'OTG',	'ENG',	'PSG',	'SOG',	'Status',	'Cap Hit'
]]
H1516 = H56.loc[:, ['First Name',	'Last Name',	'DOB', 'Age',	'Ctry',	'Team',	'Pos',	'S',	'HT',	'Wt',	'TOI',	'TOI/G',	'GP',	'G',	'A',	'Pts',	'+/-',	'PIM',	'Shifts',	'Sh',	'SH%',	'SOS',	'MsS',	'OPS',	'DPS',	'PS',	'Match',	'Misc',	'G Misc',	'PDO',	'Corsi',	'RelC',	'GvA',	'TkA',	'Blocked',	'Hits',	'FO%',	'FOW',	'FOL',	'1G',	'GWG',	'OTG',	'ENG',	'PSG',	'SOG',	'Status',	'Cap Hit'
]]
H1617 = H67.loc[:, ['First Name',	'Last Name',	'DOB', 'Age',	'Ctry',	'Team',	'Pos',	'S',	'HT',	'Wt',	'TOI',	'TOI/G',	'GP',	'G',	'A',	'Pts',	'+/-',	'PIM',	'Shifts',	'Sh',	'SH%',	'SOS',	'MsS',	'OPS',	'DPS',	'PS',	'Match',	'Misc',	'G Misc',	'PDO',	'Corsi',	'RelC',	'GvA',	'TkA',	'Blocked',	'Hits',	'FO%',	'FOW',	'FOL',	'1G',	'GWG',	'OTG',	'ENG',	'PSG',	'SOG',	'Status',	'Cap Hit'
]]
H1718 = H78.loc[:, ['First Name',	'Last Name',	'DOB', 'Age',	'Ctry',	'Team',	'Pos',	'S',	'HT',	'Wt',	'TOI',	'TOI/G',	'GP',	'G',	'A',	'Pts',	'+/-',	'PIM',	'Shifts',	'Sh',	'SH%',	'SOS',	'MsS',	'OPS',	'DPS',	'PS',	'Match',	'Misc',	'G Misc',	'PDO',	'Corsi',	'RelC',	'GvA',	'TkA',	'Blocked',	'Hits',	'FO%',	'FOW',	'FOL',	'1G',	'GWG',	'OTG',	'ENG',	'PSG',	'SOG',	'Status',	'Cap Hit'
]]

H1112['Season'] = '11/12'
H1213['Season'] = '12/13'
H1314['Season'] = '13/14'
H1415['Season'] = '14/15'
H1516['Season'] = '15/16'
H1617['Season'] = '16/17'
H1718['Season'] = '17/18'

frames = [H1112, H1213, H1314, H1415, H1516, H1617, H1718]
Players = pd.concat(frames)
Players.rename(columns={'1G': 'FG'}, inplace=True)

#convert types
Players["SH%"] = Players["SH%"].convert_objects(convert_numeric=True)
Players["PDO"] = Players["PDO"].convert_objects(convert_numeric=True)
Players["Corsi"] = Players["Corsi"].convert_objects(convert_numeric=True)
Players["RelC"] = Players["RelC"].convert_objects(convert_numeric=True)

#create new attributes
Players['G/G'] = Players.G/Players.GP
Players['A/G'] = Players.A/Players.GP
Players['Pts/G'] = Players.Pts/Players.GP
Players['PIM/G'] = Players.PIM/Players.GP
Players['Shifts/G'] = Players.Shifts/Players.GP
Players['Sh/G'] = Players.Sh/Players.GP
Players['Diff'] = Players.TkA-Players.GvA
Players['Diff/G'] = Players.Diff/Players.GP
Players['Hits/G'] = Players.Hits/Players.GP
Players['Bl/G'] = Players.Blocked/Players.GP
Players['AdvG'] = Players.FG+Players.GWG+Players.OTG
Players['RelG'] = Players.G-Players.ENG-Players.PSG

#sort attributes 2
Players = Players.loc[:, ['First Name',	'Last Name',	'DOB', 'Age',	'Ctry',	'Team',	'Pos',	'S',	'HT',	'Wt',	'TOI',	'TOI/G',	'GP',	'G', 'G/G',	 'A', 'A/G', 	'Pts', 'Pts/G', '+/-',	'PIM',	'PIM/G', 'Shifts',	'Shifts/G', 'Sh', 'Sh/G',	'SH%',	'SOS',	'MsS',	'OPS',	'DPS',	'PS',	'Match',	'Misc',	'G Misc',	'PDO',	'Corsi',	'RelC',	'GvA',	'TkA',	'Diff', 'Diff/G', 'Blocked',	'Bl/G', 'Hits',	'Hits/G', 'FO%',	'FOW',	'FOL',	'FG',	'GWG',	'OTG',	'ENG',	'PSG', 'AdvG', 'RelG',	'SOG',	'Status',	'Cap Hit', 'Season'
]]
Players.rename(columns={'Cap Hit': 'CapHit'}, inplace=True)

#create subtables
Goalies1 = Goalies.loc[Goalies.GS>9,:]
Goalies2 = Goalies1.loc[Goalies1.CapHit>=1000000,:]
GoaliesN = Goalies1.loc[Goalies1.CapHit<1000000,:]
GoaliesU = Goalies2.loc[Goalies2.Status=='UFA',:]
GoaliesR = Goalies2.loc[Goalies2.Status=='RFA',:]
Players1 = Players.loc[Players.GP>9,:]
Defenseman = Players1.loc[Players1.Pos=='D',:]
Defenseman1 = Defenseman.loc[Defenseman.CapHit>=1000000,:]
DefensemanN = Defenseman.loc[Defenseman.CapHit<1000000,:]
DefensemanU = Defenseman1.loc[Defenseman1.Status=='UFA',:]
DefensemanR = Defenseman1.loc[Defenseman1.Status=='RFA',:]
Forward = Players1.loc[Players1.Pos!='D',:]
Forward1 = Forward.loc[Forward.CapHit>=1000000,:]
ForwardN = Forward.loc[Forward.CapHit<1000000,:]
ForwardU = Forward1.loc[Forward1.Status=='UFA',:]
ForwardR = Forward1.loc[Forward1.Status=='RFA',:]
