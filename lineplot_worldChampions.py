# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 16:11:34 2021

@author: Alessio
"""
import pandas as pd
#from siuba import _, mutate, summarize, filter, group_by, select, inner_join
from plotnine import *
import numpy as np

risultati = ('results.csv')
risultati = pd.read_csv(risultati)

gare = ('races.csv')
gare = pd.read_csv(gare)

piloti = ('drivers.csv')
piloti = pd.read_csv(piloti)

currPointSystem = ('currPointSystem.csv')
currPointSystem = pd.read_csv(currPointSystem)

# 1 hamilton, 30 schumacher, 579 fangio, 117 prost, 20 vettel, 101 brahabam, 
# 328 stewart, 182 lauda, 137 piquet, 102 senna, 647 ascari, 373 clarke
# 289 graham hill, 224 emerson fittipaldi, 57 hakkinen, 4 alonso, 642 farina, 
# 578 hawthorn, 403 phill hill, 341 surtees, 304 hulme, 358 rindt, 231 hunt, 
# 207 mario andretti, 222 schecktr, 178 alan jones, 177 keke rosberg
# 3 nico rosberg, 71 damon hill, 95 nigel mansell, 35 jacques villeneuve, 
# 8 raikkonen, 18 button, 830 max verstappen


'''
top = (
       risultati
       >> select(_.driverId == 1, _.driverId == 30)
       )

_.driverId == 579, 
          _.driverId == 117, _.driverId == 20, _.driverId == 101,
          _.driverId == 328, _.driverId == 182, _.driverId == 137, 
          _.driverId == 102, _.driverId == 647, _.driverId == 373,
          _.driverId == 289, _.driverId == 224, _.driverId == 57, 
          _.driverId == 4, _.driverId == 642, _.driverId == 578,
          _.driverId == 403, _.driverId == 341, _.driverId == 304, 
          _.driverId == 358, _.driverId == 231, _.driverId == 207,
          _.driverId == 222, _.driverId == 178, _.driverId == 177, 
          _.driverId == 3, _.driverId == 71, _.driverId == 95,
          _.driverId == 35, _.driverId == 8, _.driverId == 18, 
          _.driverId == 830
'''


dataPilota1 = risultati[risultati['driverId'] == 1]
dataPilota30 = risultati[risultati['driverId'] == 30]
dataPilota579 = risultati[risultati['driverId'] == 579]
dataPilota117 = risultati[risultati['driverId'] == 117]
dataPilota20 = risultati[risultati['driverId'] == 20]
dataPilota101 = risultati[risultati['driverId'] == 101]
dataPilota328 = risultati[risultati['driverId'] == 328]
dataPilota182 = risultati[risultati['driverId'] == 182]
dataPilota137 = risultati[risultati['driverId'] == 37]
dataPilota102 = risultati[risultati['driverId'] == 102]
dataPilota647 = risultati[risultati['driverId'] == 647]
dataPilota373 = risultati[risultati['driverId'] == 373]
dataPilota289 = risultati[risultati['driverId'] == 289]
dataPilota224 = risultati[risultati['driverId'] == 224]
dataPilota57 = risultati[risultati['driverId'] == 57]
dataPilota4 = risultati[risultati['driverId'] == 4]
dataPilota642 = risultati[risultati['driverId'] == 642]
dataPilota578 = risultati[risultati['driverId'] == 578]
dataPilot403 = risultati[risultati['driverId'] == 403]
dataPilota341 = risultati[risultati['driverId'] == 341]
dataPilota304 = risultati[risultati['driverId'] == 304]
dataPilota358 = risultati[risultati['driverId'] == 358]
dataPilota231 = risultati[risultati['driverId'] == 231]
dataPilota207 = risultati[risultati['driverId'] == 207]
dataPilota222 = risultati[risultati['driverId'] == 222]
dataPilota178 = risultati[risultati['driverId'] == 178]
dataPilota177 = risultati[risultati['driverId'] == 177]
dataPilota3 = risultati[risultati['driverId'] == 3]
dataPilota71 = risultati[risultati['driverId'] == 71]
dataPilota95 = risultati[risultati['driverId'] == 95]
dataPilota35 = risultati[risultati['driverId'] == 35]
dataPilota8 = risultati[risultati['driverId'] == 8]
dataPilota18 = risultati[risultati['driverId'] == 18]
dataPilota830 = risultati[risultati['driverId'] == 830]

framesPilota = [dataPilota1, dataPilota30, dataPilota579, dataPilota117, 
                 dataPilota20, dataPilota101, dataPilota328, dataPilota182,
                 dataPilota137, dataPilota102, dataPilota647, dataPilota373, 
                 dataPilota289, dataPilota224, dataPilota57, dataPilota4, 
                 dataPilota642, dataPilota578, dataPilot403, dataPilota341, 
                 dataPilota304, dataPilota358, dataPilota231, dataPilota207,
                 dataPilota222, dataPilota178, dataPilota177, dataPilota3, 
                 dataPilota71, dataPilota95, dataPilota35, dataPilota8, 
                 dataPilota18, dataPilota830]
resultPilota = pd.concat(framesPilota)


idPil_gara = resultPilota.join(gare.set_index('raceId'), on = 'raceId', lsuffix = 'caller', rsuffix = 'other')

idPil_gara_nomePil = idPil_gara.join(piloti.set_index('driverId'), on = 'driverId', lsuffix = 'caller', rsuffix = 'other')

idPil_gara_nomePil['forename'] = idPil_gara_nomePil['forename'] + " " + idPil_gara_nomePil['surname']
idPil_gara_nomePil = idPil_gara_nomePil.drop(columns = ['surname'], axis = 1)


idPil_gara_nomePil['dob'] = pd.to_datetime(idPil_gara_nomePil['dob'], format = '%Y-%m-%d')
idPil_gara_nomePil['date'] = pd.to_datetime(idPil_gara_nomePil['date'], format = '%Y-%m-%d')
idPil_gara_nomePil['anni_gara'] = ((idPil_gara_nomePil['date'] - idPil_gara_nomePil['dob']).dt.days)/365.25


#cambiati punti mettendo sistema di punti attuale
currPointSystem['positionOrder'] = currPointSystem['positionOrder'].astype('str')
idPil_gara_nomePil = idPil_gara_nomePil.join(currPointSystem.set_index('positionOrder'), on = 'position', lsuffix = 'caller', rsuffix = 'other')

idPil_gara_nomePil=idPil_gara_nomePil.drop(columns = ['raceId','constructorId','driverId','name','numbercaller', 'pointscaller', 'grid', 'position', 'positionText', 'positionOrder', 'laps', 'timecaller','milliseconds', 'fastestLap', 'rank', 'fastestLapTime', 'fastestLapSpeed', 'statusId', 'year', 'round','circuitId','date','timeother','urlcaller','driverRef', 'numberother','code','dob','nationality', 'urlother'], axis = 1)

#per far apparire le linee dei 6 piloti sopra alle altre li mettiamo come ultimi
idPil_gara_nomePil = idPil_gara_nomePil.reset_index(drop = True)

idPil_gara_nomePil.loc[0:287, ['forename']] = 'ZZZLewis Hamilton'
idPil_gara_nomePil.loc[288:595, ['forename']] = 'ZZZMichael Schumacher'
idPil_gara_nomePil.loc[596:653, ['forename']] = 'ZZZJuan Fangio'
idPil_gara_nomePil.loc[654:855, ['forename']] = 'ZZZAlain Prost'
idPil_gara_nomePil.loc[856:1135, ['forename']] = 'ZZZSebastian Vettel'
idPil_gara_nomePil.loc[1547:1708, ['forename']] = 'ZZZAyrton Senna'


idPil_gara_nomePil = idPil_gara_nomePil.sort_values(['anni_gara'], ascending = True)

idPil_gara_nomePil['pointsother'] = idPil_gara_nomePil['pointsother'].replace(np.nan, 0)

idPil_gara_nomePil['cumsum'] = idPil_gara_nomePil.groupby('forename')['pointsother'].cumsum()







#hamilton(22), schumacher(25), vettel(34), senna(4), prost(1), fangio(19) 

fig1 = (ggplot(idPil_gara_nomePil, aes(x = 'anni_gara', y = 'cumsum')) +
       scale_x_continuous(labels = ['20 anni', '30 anni', '40 anni', '50 anni']) +
       geom_line(aes(group = 'forename', color = 'forename', size = 'forename')) +
       scale_color_manual(values = ['grey', 'grey', 'grey', 'grey', 'grey', 'grey',
                                      'grey', 'grey', 'grey', 'grey', 'grey', 'grey',
                                      'grey', 'grey', 'grey', 'grey', 'grey', 'grey',
                                      'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 
                                      'grey', 'grey', 'grey', 'grey', 'darkorange', 'orchid',
                                      'limegreen', 'turquoise', 'red', 'mediumblue']) + 
       scale_size_manual(values = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
                                   0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2]) +
       theme(legend_position=('none')) +
       theme(figure_size = (17, 12))
       )

ggsave(fig1, filename = 'LineChart.svg', dpi = 1200, format = 'svg', path = 'C:/Users/Alessio/Documents/GitHub/DataVizProject-F1/data')
#fig1.savefig(f'LineChart.svg', format='svg', dpi=1200, facecolor='w', bbox_inches='tight', pad_inches=0)


#ALLUVIAL PLOT
#ALLUVIAL PLOT

stato = ('status.csv')
stato = pd.read_csv(stato)

idStatus_gara = stato.join(risultati.set_index('statusId'), on = 'statusId', lsuffix = 'caller', rsuffix = 'other')
idStatus_gara = idStatus_gara.drop(columns = ['resultId', 'raceId', 'constructorId',
                                              'number', 'grid', 'position', 'positionText', 
                                              'positionOrder', 'points', 'laps', 'time', 
                                              'milliseconds', 'fastestLap', 'rank', 'fastestLapTime',
                                              'fastestLapSpeed'])

idStatus_gara = idStatus_gara.join(piloti.set_index('driverId'), on = 'driverId', lsuffix = 'caller', rsuffix = 'other')
idStatus_gara = idStatus_gara.drop(columns = ['driverRef', 'number', 'code', 'dob', 'nationality', 'url'])
idStatus_gara['forename'] = idStatus_gara['forename'] + " " + idStatus_gara['surname']
idStatus_gara = idStatus_gara.drop(columns = ['surname'])


# DOPPIATO 11a19+45+50+53+55+58+88+111a120+122a125+127+128+133+134
# INCIDENTE 3+4+20+33+41+65+70+78+85+89+104+130+137+138
# MECCANICA 5+6+7+8+21+22+23+24+26+30+37+38+43+49+56+76+79+80+83+86+87+90+91+102+105+
# + 109+121+126+129+135
# RUOTE 27+29+36+46+59+61+63+67
# GUASTI TECNICI 9+10+25+32+34+35+39+40+42+44+47+48+51+60+66+69+71+72+74+75+84+94+
# + 95+98+99+101+103+106+108+110+131+132
# PROBLEMI PILOTA 28+64+68+73+82+92+93+100+107+136+139
# NON CLASSIFICATI 31+54+62+77+81+90+96+97
#mancanti 57

idStatus_gara1 = idStatus_gara[idStatus_gara['statusId'] == 1]
idStatus_gara2 = idStatus_gara[idStatus_gara['statusId'] == 2]
idStatus_gara3 = idStatus_gara[idStatus_gara['statusId'] == 3]
idStatus_gara4 = idStatus_gara[idStatus_gara['statusId'] == 4]
idStatus_gara5 = idStatus_gara[idStatus_gara['statusId'] == 5]
idStatus_gara6 = idStatus_gara[idStatus_gara['statusId'] == 6]
idStatus_gara7 = idStatus_gara[idStatus_gara['statusId'] == 7]
idStatus_gara8 = idStatus_gara[idStatus_gara['statusId'] == 8]
idStatus_gara9 = idStatus_gara[idStatus_gara['statusId'] == 9]
idStatus_gara10 = idStatus_gara[idStatus_gara['statusId'] == 10]
idStatus_gara11 = idStatus_gara[idStatus_gara['statusId'] == 11]
idStatus_gara12 = idStatus_gara[idStatus_gara['statusId'] == 12]
idStatus_gara13 = idStatus_gara[idStatus_gara['statusId'] == 13]
idStatus_gara14 = idStatus_gara[idStatus_gara['statusId'] == 14]
idStatus_gara15 = idStatus_gara[idStatus_gara['statusId'] == 15]
idStatus_gara16 = idStatus_gara[idStatus_gara['statusId'] == 16]
idStatus_gara17 = idStatus_gara[idStatus_gara['statusId'] == 17]
idStatus_gara18 = idStatus_gara[idStatus_gara['statusId'] == 18]
idStatus_gara19 = idStatus_gara[idStatus_gara['statusId'] == 19]
idStatus_gara20 = idStatus_gara[idStatus_gara['statusId'] == 20]
idStatus_gara21 = idStatus_gara[idStatus_gara['statusId'] == 21]
idStatus_gara22 = idStatus_gara[idStatus_gara['statusId'] == 22]
idStatus_gara23 = idStatus_gara[idStatus_gara['statusId'] == 23]
idStatus_gara24 = idStatus_gara[idStatus_gara['statusId'] == 24]
idStatus_gara25 = idStatus_gara[idStatus_gara['statusId'] == 25]
idStatus_gara26 = idStatus_gara[idStatus_gara['statusId'] == 26]
idStatus_gara27 = idStatus_gara[idStatus_gara['statusId'] == 27]
idStatus_gara28 = idStatus_gara[idStatus_gara['statusId'] == 28]
idStatus_gara29 = idStatus_gara[idStatus_gara['statusId'] == 29]
idStatus_gara30 = idStatus_gara[idStatus_gara['statusId'] == 30]
idStatus_gara31 = idStatus_gara[idStatus_gara['statusId'] == 31]
idStatus_gara32 = idStatus_gara[idStatus_gara['statusId'] == 32]
idStatus_gara33 = idStatus_gara[idStatus_gara['statusId'] == 33]
idStatus_gara34 = idStatus_gara[idStatus_gara['statusId'] == 34]
idStatus_gara35 = idStatus_gara[idStatus_gara['statusId'] == 35]
idStatus_gara36 = idStatus_gara[idStatus_gara['statusId'] == 36]
idStatus_gara37 = idStatus_gara[idStatus_gara['statusId'] == 37]
idStatus_gara38 = idStatus_gara[idStatus_gara['statusId'] == 38]
idStatus_gara39 = idStatus_gara[idStatus_gara['statusId'] == 39]
idStatus_gara40 = idStatus_gara[idStatus_gara['statusId'] == 40]
idStatus_gara41 = idStatus_gara[idStatus_gara['statusId'] == 41]
idStatus_gara42 = idStatus_gara[idStatus_gara['statusId'] == 42]
idStatus_gara43 = idStatus_gara[idStatus_gara['statusId'] == 43]
idStatus_gara44 = idStatus_gara[idStatus_gara['statusId'] == 44]
idStatus_gara45 = idStatus_gara[idStatus_gara['statusId'] == 45]
idStatus_gara46 = idStatus_gara[idStatus_gara['statusId'] == 46]
idStatus_gara47 = idStatus_gara[idStatus_gara['statusId'] == 47]
idStatus_gara48 = idStatus_gara[idStatus_gara['statusId'] == 48]
idStatus_gara49 = idStatus_gara[idStatus_gara['statusId'] == 49]
idStatus_gara50 = idStatus_gara[idStatus_gara['statusId'] == 50]
idStatus_gara51 = idStatus_gara[idStatus_gara['statusId'] == 51]
idStatus_gara52 = idStatus_gara[idStatus_gara['statusId'] == 52]
idStatus_gara53 = idStatus_gara[idStatus_gara['statusId'] == 53]
idStatus_gara54 = idStatus_gara[idStatus_gara['statusId'] == 54]
idStatus_gara55 = idStatus_gara[idStatus_gara['statusId'] == 55]
idStatus_gara56 = idStatus_gara[idStatus_gara['statusId'] == 56]
idStatus_gara58 = idStatus_gara[idStatus_gara['statusId'] == 58]
idStatus_gara59 = idStatus_gara[idStatus_gara['statusId'] == 59]
idStatus_gara60 = idStatus_gara[idStatus_gara['statusId'] == 60]
idStatus_gara61 = idStatus_gara[idStatus_gara['statusId'] == 61]
idStatus_gara62 = idStatus_gara[idStatus_gara['statusId'] == 62]
idStatus_gara63 = idStatus_gara[idStatus_gara['statusId'] == 63]
idStatus_gara64 = idStatus_gara[idStatus_gara['statusId'] == 64]
idStatus_gara65 = idStatus_gara[idStatus_gara['statusId'] == 65]
idStatus_gara66 = idStatus_gara[idStatus_gara['statusId'] == 66]
idStatus_gara67 = idStatus_gara[idStatus_gara['statusId'] == 67]
idStatus_gara68 = idStatus_gara[idStatus_gara['statusId'] == 68]
idStatus_gara69 = idStatus_gara[idStatus_gara['statusId'] == 69]
idStatus_gara70 = idStatus_gara[idStatus_gara['statusId'] == 70]
idStatus_gara71 = idStatus_gara[idStatus_gara['statusId'] == 71]
idStatus_gara72 = idStatus_gara[idStatus_gara['statusId'] == 72]
idStatus_gara73 = idStatus_gara[idStatus_gara['statusId'] == 73]
idStatus_gara74 = idStatus_gara[idStatus_gara['statusId'] == 74]
idStatus_gara75 = idStatus_gara[idStatus_gara['statusId'] == 75]
idStatus_gara76 = idStatus_gara[idStatus_gara['statusId'] == 76]
idStatus_gara77 = idStatus_gara[idStatus_gara['statusId'] == 77]
idStatus_gara78 = idStatus_gara[idStatus_gara['statusId'] == 78]
idStatus_gara79 = idStatus_gara[idStatus_gara['statusId'] == 79]
idStatus_gara80 = idStatus_gara[idStatus_gara['statusId'] == 80]
idStatus_gara81 = idStatus_gara[idStatus_gara['statusId'] == 81]
idStatus_gara82 = idStatus_gara[idStatus_gara['statusId'] == 82]
idStatus_gara83 = idStatus_gara[idStatus_gara['statusId'] == 83]
idStatus_gara84 = idStatus_gara[idStatus_gara['statusId'] == 84]
idStatus_gara85 = idStatus_gara[idStatus_gara['statusId'] == 85]
idStatus_gara86 = idStatus_gara[idStatus_gara['statusId'] == 86]
idStatus_gara87 = idStatus_gara[idStatus_gara['statusId'] == 87]
idStatus_gara88 = idStatus_gara[idStatus_gara['statusId'] == 88]
idStatus_gara89 = idStatus_gara[idStatus_gara['statusId'] == 89]
idStatus_gara90 = idStatus_gara[idStatus_gara['statusId'] == 90]
idStatus_gara91 = idStatus_gara[idStatus_gara['statusId'] == 91]
idStatus_gara92 = idStatus_gara[idStatus_gara['statusId'] == 92]
idStatus_gara93 = idStatus_gara[idStatus_gara['statusId'] == 93]
idStatus_gara94 = idStatus_gara[idStatus_gara['statusId'] == 94]
idStatus_gara95 = idStatus_gara[idStatus_gara['statusId'] == 95]
idStatus_gara96 = idStatus_gara[idStatus_gara['statusId'] == 96]
idStatus_gara97 = idStatus_gara[idStatus_gara['statusId'] == 97]
idStatus_gara98 = idStatus_gara[idStatus_gara['statusId'] == 98]
idStatus_gara99 = idStatus_gara[idStatus_gara['statusId'] == 99]
idStatus_gara100 = idStatus_gara[idStatus_gara['statusId'] == 100]
idStatus_gara101 = idStatus_gara[idStatus_gara['statusId'] == 101]
idStatus_gara102 = idStatus_gara[idStatus_gara['statusId'] == 102]
idStatus_gara103 = idStatus_gara[idStatus_gara['statusId'] == 103]
idStatus_gara104 = idStatus_gara[idStatus_gara['statusId'] == 104]
idStatus_gara105 = idStatus_gara[idStatus_gara['statusId'] == 105]
idStatus_gara106 = idStatus_gara[idStatus_gara['statusId'] == 106]
idStatus_gara107 = idStatus_gara[idStatus_gara['statusId'] == 107]
idStatus_gara108 = idStatus_gara[idStatus_gara['statusId'] == 108]
idStatus_gara109 = idStatus_gara[idStatus_gara['statusId'] == 109]
idStatus_gara110 = idStatus_gara[idStatus_gara['statusId'] == 110]
idStatus_gara111 = idStatus_gara[idStatus_gara['statusId'] == 111]
idStatus_gara112 = idStatus_gara[idStatus_gara['statusId'] == 112]
idStatus_gara113 = idStatus_gara[idStatus_gara['statusId'] == 113]
idStatus_gara114 = idStatus_gara[idStatus_gara['statusId'] == 114]
idStatus_gara115 = idStatus_gara[idStatus_gara['statusId'] == 115]
idStatus_gara116 = idStatus_gara[idStatus_gara['statusId'] == 116]
idStatus_gara117 = idStatus_gara[idStatus_gara['statusId'] == 117]
idStatus_gara118 = idStatus_gara[idStatus_gara['statusId'] == 118]
idStatus_gara119 = idStatus_gara[idStatus_gara['statusId'] == 119]
idStatus_gara120 = idStatus_gara[idStatus_gara['statusId'] == 120]
idStatus_gara121 = idStatus_gara[idStatus_gara['statusId'] == 121]
idStatus_gara122 = idStatus_gara[idStatus_gara['statusId'] == 122]
idStatus_gara123 = idStatus_gara[idStatus_gara['statusId'] == 123]
idStatus_gara124 = idStatus_gara[idStatus_gara['statusId'] == 124]
idStatus_gara125 = idStatus_gara[idStatus_gara['statusId'] == 125]
idStatus_gara126 = idStatus_gara[idStatus_gara['statusId'] == 126]
idStatus_gara127 = idStatus_gara[idStatus_gara['statusId'] == 127]
idStatus_gara128 = idStatus_gara[idStatus_gara['statusId'] == 128]
idStatus_gara129 = idStatus_gara[idStatus_gara['statusId'] == 129]
idStatus_gara130 = idStatus_gara[idStatus_gara['statusId'] == 130]
idStatus_gara131 = idStatus_gara[idStatus_gara['statusId'] == 131]
idStatus_gara132 = idStatus_gara[idStatus_gara['statusId'] == 132]
idStatus_gara133 = idStatus_gara[idStatus_gara['statusId'] == 133]
idStatus_gara134 = idStatus_gara[idStatus_gara['statusId'] == 134]
idStatus_gara135 = idStatus_gara[idStatus_gara['statusId'] == 135]
idStatus_gara136 = idStatus_gara[idStatus_gara['statusId'] == 136]
idStatus_gara137 = idStatus_gara[idStatus_gara['statusId'] == 137]
idStatus_gara138 = idStatus_gara[idStatus_gara['statusId'] == 138]
idStatus_gara139 = idStatus_gara[idStatus_gara['statusId'] == 139]


resultGaraFinita = idStatus_gara1

framesDoppiato = [idStatus_gara11, idStatus_gara12, idStatus_gara13, idStatus_gara14, 
                  idStatus_gara15, idStatus_gara16, idStatus_gara17, idStatus_gara18, 
                  idStatus_gara19, idStatus_gara50, idStatus_gara53, idStatus_gara55, 
                  idStatus_gara58, idStatus_gara88, idStatus_gara111, idStatus_gara112, 
                  idStatus_gara113, idStatus_gara114, idStatus_gara115, idStatus_gara116, 
                  idStatus_gara117, idStatus_gara118, idStatus_gara119, idStatus_gara120, 
                  idStatus_gara122, idStatus_gara123, idStatus_gara124, idStatus_gara125,
                  idStatus_gara127, idStatus_gara128, idStatus_gara133, idStatus_gara134]
resultDoppiato = pd.concat(framesDoppiato)

framesIncidente = [idStatus_gara3, idStatus_gara4, idStatus_gara20, idStatus_gara33, 
                   idStatus_gara41, idStatus_gara65, idStatus_gara70, idStatus_gara78, 
                   idStatus_gara85, idStatus_gara89, idStatus_gara104, idStatus_gara130, 
                   idStatus_gara137, idStatus_gara138]
resultIncidente = pd.concat(framesIncidente)

framesMeccanica = [idStatus_gara5, idStatus_gara6, idStatus_gara7, idStatus_gara8, 
                   idStatus_gara21, idStatus_gara22, idStatus_gara23, idStatus_gara24, 
                   idStatus_gara26, idStatus_gara30, idStatus_gara37, idStatus_gara38, 
                   idStatus_gara43, idStatus_gara49, idStatus_gara56, idStatus_gara64,
                   idStatus_gara76, idStatus_gara79, idStatus_gara80, idStatus_gara83, 
                   idStatus_gara86, idStatus_gara87, idStatus_gara90, idStatus_gara91, 
                   idStatus_gara102, idStatus_gara105, idStatus_gara109, idStatus_gara121, 
                   idStatus_gara126, idStatus_gara129, idStatus_gara135]
resultMeccanica = pd.concat(framesMeccanica)


framesProbRuote = [idStatus_gara27, idStatus_gara29, idStatus_gara36, idStatus_gara46,
                 idStatus_gara59, idStatus_gara61, idStatus_gara63, idStatus_gara67]
resultProbRuote = pd.concat(framesProbRuote)


framesProbTecn = [idStatus_gara9, idStatus_gara10, idStatus_gara25, idStatus_gara32,
                 idStatus_gara34, idStatus_gara35, idStatus_gara39, idStatus_gara40,
                 idStatus_gara42, idStatus_gara44, idStatus_gara47, idStatus_gara48, 
                 idStatus_gara51, idStatus_gara60, idStatus_gara66, idStatus_gara69,
                 idStatus_gara71, idStatus_gara72, idStatus_gara74, idStatus_gara75,
                 idStatus_gara84, idStatus_gara94, idStatus_gara95, idStatus_gara98,
                 idStatus_gara99, idStatus_gara101, idStatus_gara103, idStatus_gara106,
                 idStatus_gara108, idStatus_gara110, idStatus_gara131, idStatus_gara132]
resultProbTecn = pd.concat(framesProbTecn)

framesProbPilota = [idStatus_gara28, idStatus_gara68, idStatus_gara73,
                 idStatus_gara82, idStatus_gara92, idStatus_gara93, idStatus_gara100,
                 idStatus_gara107, idStatus_gara136, idStatus_gara139]
resultProbPilota = pd.concat(framesProbPilota)

framesNonClass = [idStatus_gara31, idStatus_gara54, idStatus_gara62, idStatus_gara77,
                 idStatus_gara81, idStatus_gara90, idStatus_gara96, idStatus_gara97]
resultNonClass = pd.concat(framesNonClass)


resultGaraFinita1 = resultGaraFinita[resultGaraFinita['forename'] == "Alain Prost"]
resultGaraFinita2 = resultGaraFinita[resultGaraFinita['forename'] == "Ayrton Senna"]
resultGaraFinita3 = resultGaraFinita[resultGaraFinita['forename'] == "Juan Fangio"]
resultGaraFinita4 = resultGaraFinita[resultGaraFinita['forename'] == "Lewis Hamilton"]
resultGaraFinita5 = resultGaraFinita[resultGaraFinita['forename'] == "Michael Schumacher"]
resultGaraFinita6 = resultGaraFinita[resultGaraFinita['forename'] == "Sebastian Vettel"]
framesGaraFinitaTop = [resultGaraFinita1, resultGaraFinita2, resultGaraFinita3,
                     resultGaraFinita4, resultGaraFinita5, resultGaraFinita6]
resultGaraFinitaTop = pd.concat(framesGaraFinitaTop)

resultDoppiato1 = resultDoppiato[resultDoppiato['forename'] == "Alain Prost"]
resultDoppiato2 = resultDoppiato[resultDoppiato['forename'] == "Ayrton Senna"]
resultDoppiato3 = resultDoppiato[resultDoppiato['forename'] == "Juan Fangio"]
resultDoppiato4 = resultDoppiato[resultDoppiato['forename'] == "Lewis Hamilton"]
resultDoppiato5 = resultDoppiato[resultDoppiato['forename'] == "Michael Schumacher"]
resultDoppiato6 = resultDoppiato[resultDoppiato['forename'] == "Sebastian Vettel"]
framesDoppiatoTop = [resultDoppiato1, resultDoppiato2, resultDoppiato3, resultDoppiato4, resultDoppiato5, resultDoppiato6]
resultDoppiatoTop = pd.concat(framesDoppiatoTop)


resultIncidente1 = resultIncidente[resultIncidente['forename'] == "Alain Prost"]
resultIncidente2 = resultIncidente[resultIncidente['forename'] == "Ayrton Senna"]
resultIncidente3 = resultIncidente[resultIncidente['forename'] == "Juan Fangio"]
resultIncidente4 = resultIncidente[resultIncidente['forename'] == "Lewis Hamilton"]
resultIncidente5 = resultIncidente[resultIncidente['forename'] == "Michael Schumacher"]
resultIncidente6 = resultIncidente[resultIncidente['forename'] == "Sebastian Vettel"]
framesIncidenteTop = [resultIncidente1, resultIncidente2, resultIncidente3, resultIncidente4, resultIncidente5, resultIncidente6]
resultIncidenteTop = pd.concat(framesIncidenteTop)


resultMeccanica1 = resultMeccanica[resultMeccanica['forename'] == "Alain Prost"]
resultMeccanica2 = resultMeccanica[resultMeccanica['forename'] == "Ayrton Senna"]
resultMeccanica3 = resultMeccanica[resultMeccanica['forename'] == "Juan Fangio"]
resultMeccanica4 = resultMeccanica[resultMeccanica['forename'] == "Lewis Hamilton"]
resultMeccanica5 = resultMeccanica[resultMeccanica['forename'] == "Michael Schumacher"]
resultMeccanica6 = resultMeccanica[resultMeccanica['forename'] == "Sebastian Vettel"]
framesMeccanicaTop = [resultMeccanica1, resultMeccanica2, resultMeccanica3, resultMeccanica4, resultMeccanica5, resultMeccanica6]
resultMeccanicaTop = pd.concat(framesMeccanicaTop)


resultProbRuote1 = resultProbRuote[resultProbRuote['forename'] == 'Alain Prost']
resultProbRuote2 = resultProbRuote[resultProbRuote['forename'] == 'Ayrton Senna']
resultProbRuote3 = resultProbRuote[resultProbRuote['forename'] == 'Juan Fangio']
resultProbRuote4 = resultProbRuote[resultProbRuote['forename'] == 'Lewis Hamilton']
resultProbRuote5 = resultProbRuote[resultProbRuote['forename'] == 'Michael Schumacher']
resultProbRuote6 = resultProbRuote[resultProbRuote['forename'] == 'Sebastian Vettel']
framesProbRuoteTop = [resultProbRuote1, resultProbRuote2, resultProbRuote3,
                      resultProbRuote4, resultProbRuote5, resultProbRuote6]
resultProbRuoteTop = pd.concat(framesProbRuoteTop)


resultProbTecn1 = resultProbTecn[resultProbTecn['forename'] == 'Alain Prost']
resultProbTecn2 = resultProbTecn[resultProbTecn['forename'] == 'Ayrton Senna']
resultProbTecn3 = resultProbTecn[resultProbTecn['forename'] == 'Juan Fangio']
resultProbTecn4 = resultProbTecn[resultProbTecn['forename'] == 'Lewis Hamilton']
resultProbTecn5 = resultProbTecn[resultProbTecn['forename'] == 'Michael Schumacher']
resultProbTecn6 = resultProbTecn[resultProbTecn['forename'] == 'Sebastian Vettel']
framesProbTecnTop = [resultProbTecn1, resultProbTecn2, resultProbTecn3,
                      resultProbTecn4, resultProbTecn5, resultProbTecn6]
resultProbTecnTop = pd.concat(framesProbTecnTop)


resultProbPilota1 = resultProbPilota[resultProbPilota['forename'] == 'Alain Prost']
resultProbPilota2 = resultProbPilota[resultProbPilota['forename'] == 'Ayrton Senna']
resultProbPilota3 = resultProbPilota[resultProbPilota['forename'] == 'Juan Fangio']
resultProbPilota4 = resultProbPilota[resultProbPilota['forename'] == 'Lewis Hamilton']
resultProbPilota5 = resultProbPilota[resultProbPilota['forename'] == 'Michael Schumacher']
resultProbPilota6 = resultProbPilota[resultProbPilota['forename'] == 'Sebastian Vettel']
framesProbPilotaTop = [resultProbPilota1, resultProbPilota2, resultProbPilota3,
                      resultProbPilota4, resultProbPilota5, resultProbPilota6]
resultProbPilotaTop = pd.concat(framesProbPilotaTop)



resultNonClass1 = resultNonClass[resultNonClass['forename'] == 'Alain Prost']
resultNonClass2 = resultNonClass[resultNonClass['forename'] == 'Ayrton Senna']
resultNonClass3 = resultNonClass[resultNonClass['forename'] == 'Juan Fangio']
resultNonClass4 = resultNonClass[resultNonClass['forename'] == 'Lewis Hamilton']
resultNonClass5 = resultNonClass[resultNonClass['forename'] == 'Michael Schumacher']
resultNonClass6 = resultNonClass[resultNonClass['forename'] == 'Sebastian Vettel']
framesNonClassTop = [resultNonClass1, resultNonClass2, resultNonClass3,
                      resultNonClass4, resultNonClass5, resultNonClass6]
resultNonClassTop = pd.concat(framesNonClassTop)


import plotly.graph_objects as go


#sankey schumacher e hamilton

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 2),
      label = ["Lewis Hamilton", "Michael Schumacher",
               "Gara finita", "Gara non finita", "Doppiato",
               "Incidente", "Problema meccanico", "Problema ruote", "Problema tecnico/elettronico", "Non classificato"],
      color = "white",
      #fissate posizioni
      x = [0, 0, 0.5, 0.5, 0.5, 0.9, 0.9, 0.9, 0.9, 0.9],
      y = [0.2, 0.6, 0.35, 0.9, 0.75, 0.2, 0.4, 0.6, 0.8, 0.9]
    ),
    link = dict(
      source = [0, 1, 0, 1, 0, 1,    3, 3, 3, 3, 3, 3, 3, 3, 3, 3], # indices correspond to labels
      target = [2, 2, 3, 3, 4, 4,    5 ,6, 7, 8, 9, 5, 6, 7, 8, 9],
      value = [251, 219, 26, 68, 9, 18,     13, 8, 2, 2, 1, 33, 22, 5, 6, 2],
      color = ['turquoise', 'red', 'turquoise', 'red', 'turquoise', 'red', 
               'turquoise', 'turquoise', 'turquoise', 'turquoise', 'turquoise', 'red', 'red', 'red', 'red', 'red']
  ),)],
    layout = dict(
        title = dict(
        text = '<b>' + "Come si sono concluse le gare dei due migliori piloti?" + '</b>' + 
         '<br>' + "Attraverso l’analisi dei risultati di ogni gara disputata da ognuno dei piloti considerati, è stato realizzato un alluvial diagram per rappresentare la quantità di gare concluse, <br>concluse ma dopo essere stati doppiati o non concluse (con le varie motivazioni)."
         '<br>' '<br>' + '<i>' + "Fonte: ergast.com/mrd/" + '</i>' + "<br>", 
        font = dict(size = 17, family = 'Georgia'),
        x=0,
        y=0.98
        ),
    )
    )

#fig.update_layout(title_text="Sankey Diagram Piloti & gare (non) finite <br> Context Context Context Context Context Context Context Context Context Context", 
                  #font_size=15)
#fig.text(s='This is my 1st main title', x=0, y=0.9, fontsize=18, ha='center', va='center')

fig.add_annotation(x=0.45, y=0.99,
            text='<b>' + "Hamilton" + '</b>' + " è il pilota che ha concluso più gare",
            showarrow=True,
            arrowhead=1, 
            font = dict(size = 13, family = 'Georgia'))

fig.add_annotation(x=0.65, y=0.8,
            text= '<b>' + "Schumacher" + '</b>' + " ha avuto più problemi tecnici " '<br>'
            "e meccanici di Hamilton, " '<br>' "dovuto alla" + '<b>' + " minore affidabilità" + '</b>' + " delle " '<br>'
            "vetture di quel periodo rispetto a quelle attuali",
            showarrow=False, 
            yshift = 10,
            font = dict(size = 13, family = 'Georgia'))

fig.add_annotation(x=0.888, y=0.84,
            text='<b>' + "Schumacher" + '</b>' + " ha registrato un maggior"'<br>'
            "numero di incidenti rispetto ad Hamilton",
            showarrow=True,
            arrowhead=1, 
            font = dict(size = 13, family = 'Georgia'))

fig.add_annotation(x=0.45, y=-0.06,
            text= '<b>' + "Schumacher" + '</b>' + " è il pilota che ha" '<br>'
            + '<b>' + "più gare non finite" + '</b>',
            showarrow=False,
            font = dict(size = 13, family = 'Georgia'))

fig.add_annotation(x=0.45, y=0,
            showarrow=True,
            arrowhead = 1)

fig.show()
fig.write_html("C:/Users/Alessio/Desktop/index.html")
#fig.write_html("C:/Users/gemelli/Desktop/index.html")


#sankey sui 6 piloti tutto colorato

fig2 = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 2),
      label = ["Alain Prost", "Ayrton Senna", "Juan Manuel Fangio", "Lewis Hamilton", "Michael Schumacher", "Sebastian Vettel",
               "Gara finita", "Gara non finita", "Doppiato",
               "Incidente", "Problema meccanico", "Problema ruote", "Problema tecnico/elettronico", "Non classificato"],
      color = "white",
      #fissate posizioni
      x = [0, 0, 0, 0, 0, 0, 0.5, 0.5, 0.5, 0.9, 0.9, 0.9, 0.9, 0.9],
      y = [0, 0.2, 0.4, 0.6, 0.8, 1, 0.3, 0.9, 0.7, 0.2, 0.4, 0.6, 0.8, 1]
    ),
    link = dict(
      source = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5,    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7], # indices correspond to labels
      target = [6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8,    9, 10, 11, 12, 13, 9, 10, 11, 12, 13, 9, 10, 11, 12, 13, 9, 10, 11, 12, 13, 9, 10, 11, 12, 13, 9, 10, 11, 12, 13],
      value = [119, 85, 37, 251, 219, 213, 63, 62, 14, 26, 68, 42, 18, 12, 7, 9, 18, 24,     20, 27, 0, 13, 3, 22, 22, 3, 14, 1, 1, 11, 0, 2, 0, 13, 8, 2, 2, 1, 33, 22, 5, 6, 2, 17, 15, 4, 5, 1],
      color = ['darkorange', 'orchid', 'limegreen', 'turquoise', 'red', 'mediumblue', 'darkorange', 'orchid', 'limegreen', 'turquoise', 'red', 'mediumblue', 'darkorange', 'orchid', 'limegreen', 'turquoise', 'red', 'mediumblue',
               'darkorange', 'darkorange', 'darkorange', 'darkorange', 'darkorange', 'orchid', 'orchid', 'orchid', 'orchid', 'orchid', 
               'limegreen', 'limegreen', 'limegreen', 'limegreen', 'limegreen', 'turquoise', 'turquoise', 'turquoise', 'turquoise', 'turquoise', 
               'red', 'red', 'red', 'red', 'red', 'mediumblue', 'mediumblue', 'mediumblue', 'mediumblue', 'mediumblue']
  ),)],
    layout = dict(
        title = dict(
        text = '<b>' + "COME SI SONO CONCLUSE LE GARE DEI MIGLIORI 6 PILOTI?" + '</b>' + 
         '<br>' + "Attraverso l’analisi dei risultati di ogni gara disputata da ognuno dei piloti considerati, è stato realizzato un alluvial diagram per rappresentare la quantità di gare concluse, <br>concluse ma dopo essere stati doppiati o non concluse (con le varie motivazioni)."
         '<br>' '<br>' + '<i>' + "Fonte: ergast.com/mrd/" + '</i>' + "<br>", 
        font = dict(size = 17, family = 'Georgia'),
        x=0,
        y=0.98
        ),
    )
    )

fig2.write_html("C:/Users/Alessio/Desktop/Sankey_6Pil.html")

resultGaraFinitaTop['forename'].value_counts() #Prost 119, Senna 85, Fangio 37, Hamilton 251, Schumacher 219, Vettel 213
resultDoppiatoTop['forename'].value_counts() #Prost 18, Senna 12, Fangio 7, Hamilton 9, Schumacher 18, Vettel 24
resultIncidenteTop['forename'].value_counts() #Prost 20, Senna 22, Fangio 1, Hamilton 13, Schumacher 33, Vettel 17
resultMeccanicaTop['forename'].value_counts() #Prost 26, Senna 22, Fangio 11, Hamilton 8, Schumacher 22, Vettel 15
resultProbRuoteTop['forename'].value_counts() #Prost 0, Senna 3, Fangio 0, Hamilton 2, Schumacher 5, Vettel 4
resultProbTecnTop['forename'].value_counts() #Prost 13, Senna 14, Fangio 2, Hamilton 2, Schumacher 6, Vettel 5
resultProbPilotaTop['forename'].value_counts() #Prost 1, Senna 0, Fangio 0, Hamilton 0, Schumacher 0, Vettel 0
resultNonClassTop['forename'].value_counts() #Prost 3, Senna 1, Fangio 0, Hamilton 1, Schumacher 2, Vettel 1

                       # gara non finita      Prost 63, Senna 62, Fangio 14, Hamilton 26, Schumacher 68, Vettel 42
                       
                       
                       
#altro sankey sch vs ham                       
                       
fig3 = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 2),
      label = ["Lewis Hamilton", "Michael Schumacher",
               "Gara finita", "Gara non finita", "Doppiato", "Gara finita", "Gara non finita", "Doppiato",
               "Incidente", "Problema meccanico", "Problema ruote", "Problema tecnico/elettronico", "Non classificato",
               "Incidente", "Problema meccanico", "Problema ruote", "Problema tecnico/elettronico", "Non classificato"],
      color = ["turquoise", "red", "turquoise", "turquoise", "turquoise", "red", "red", "red", "turquoise", "turquoise", "turquoise", "turquoise", "turquoise", "red", "red", "red", "red", "red"],
      #fissate posizioni
      x = [0, 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9],
      y = [0.2, 0.6, 0.1, 0.5, 0.35, 0.6, 0.9, 0.75, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    ),
    link = dict(
      source = [0, 1, 0, 1, 0, 1,    3, 3, 3, 3, 3, 6, 6, 6, 6, 6], # indices correspond to labels
      target = [2, 5, 3, 6, 4, 7,    8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
      value = [251, 219, 26, 68, 9, 18,     13, 8, 2, 2, 1, 33, 22, 5, 6, 2],
      #color = ['turquoise', 'red', 'turquoise', 'red', 'turquoise', 'red', 
        #       'turquoise', 'turquoise', 'turquoise', 'turquoise', 'turquoise', 'red', 'red', 'red', 'red', 'red']
  ),)],
    layout = dict(
        title = dict(
        text = '<b>' + "Come si sono concluse le gare dei due migliori piloti?" + '</b>' + 
         '<br>' + "Attraverso l’analisi dei risultati di ogni gara disputata da ognuno dei piloti considerati, è stato realizzato un alluvial diagram per rappresentare la quantità di gare concluse, <br>concluse ma dopo essere stati doppiati o non concluse (con le varie motivazioni)."
         '<br>' '<br>' + '<i>' + "Fonte: ergast.com/mrd/" + '</i>' + "<br>", 
        font = dict(size = 17, family = 'Georgia'),
        x=0,
        y=0.98
        ),
    )
    )
                      

fig3.write_html("C:/Users/Alessio/Desktop/Sankey_boh.html")                
                       
                       
