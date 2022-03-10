#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
from lxml import html
from bs4 import BeautifulSoup
import pandas as pd
import csv 
import numpy as np
import matplotlib.pyplot as plt


# In[9]:


SNHU_2010 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2010', header = 0)
SNHU_2011 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2011', header = 0)
SNHU_2012 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2012', header = 0)
SNHU_2013 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2013', header = 0)
SNHU_2014 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2014', header = 0)
SNHU_2015 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2015', header = 0)
SNHU_2016 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2016', header = 0)
SNHU_2017 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2017', header = 0)
SNHU_2018 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2018', header = 0)
SNHU_2019 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2019', header = 0)
SNHU_2020 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2020', header = 0)
SNHU_2021 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2021', header = 0)
SNHU_2022 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2022', header = 0)


# In[10]:


#Hitting Format
Pitching2010 = SNHU_2010[1]
Pitching2010 =Pitching2010.drop(['Bio Link'],axis = 1)
Pitching2010 =Pitching2010.drop(['Player'],axis = 1)
Pitching2010 = Pitching2010.dropna()
#2011
Pitching2011 = SNHU_2011[1]
Pitching2011 =Pitching2011.drop(['Bio Link'],axis = 1)
Pitching2011 =Pitching2011.drop(['Player'],axis = 1)
Pitching2011 = Pitching2011.dropna()
#2012
Pitching2012 = SNHU_2012[1]
Pitching2012 =Pitching2012.drop(['Bio Link'],axis = 1)
Pitching2012 =Pitching2012.drop(['Player'],axis = 1)
Pitching2012 = Pitching2012.dropna()
#2013
Pitching2013 = SNHU_2013[1]
Pitching2013 =Pitching2013.drop(['Bio Link'],axis = 1)
Pitching2013 =Pitching2013.drop(['Player'],axis = 1)
Pitching2013 = Pitching2013.dropna()
#2014
Pitching2014 = SNHU_2014[1]
Pitching2014 =Pitching2014.drop(['Bio Link'],axis = 1)
Pitching2014 =Pitching2014.drop(['Player'],axis = 1)
Pitching2014 = Pitching2014.dropna()
#2015
Pitching2015 = SNHU_2015[1]
Pitching2015 =Pitching2015.drop(['Bio Link'],axis = 1)
Pitching2015 =Pitching2015.drop(['Player'],axis = 1)
Pitching2015= Pitching2015.dropna()
#2016
Pitching2016 = SNHU_2016[1]
Pitching2016 =Pitching2016.drop(['Bio Link'],axis = 1)
Pitching2016 =Pitching2016.drop(['Player'],axis = 1)
Pitching2016 = Pitching2016.dropna()
#2017
Pitching2017 = SNHU_2017[1]
Pitching2017 =Pitching2017.drop(['Bio Link'],axis = 1)
Pitching2017 =Pitching2017.drop(['Player'],axis = 1)
Pitching2017 = Pitching2017.dropna()
#2018
Pitching2018 = SNHU_2018[1]
Pitching2018 =Pitching2018.drop(['Bio Link'],axis = 1)
Pitching2018 =Pitching2018.drop(['Player'],axis = 1)
Pitching2018 = Pitching2018.dropna()
#2019
Pitching2019 = SNHU_2019[1]
Pitching2019 =Pitching2019.drop(['Bio Link'],axis = 1)
Pitching2019 =Pitching2019.drop(['Player'],axis = 1)
Pitching2019 = Pitching2019.dropna()
#2020
Pitching2020= SNHU_2020[1]
Pitching2020=Pitching2020.drop(['Bio Link'],axis = 1)
Pitching2020 =Pitching2020.drop(['Player'],axis = 1)
Pitching2020 = Pitching2020.dropna()
#2021
Pitching2021 = SNHU_2021[1]
Pitching2021 =Pitching2021.drop(['Bio Link'],axis = 1)
Pitching2021 =Pitching2021.drop(['Player'],axis = 1)
Pitching2021 = Pitching2021.dropna()
#2022
Pitching2022 = SNHU_2022[1]
Pitching2022 =Pitching2022.drop(['Bio Link'],axis = 1)
Pitching2022 =Pitching2022.drop(['Player'],axis = 1)
Pitching2022 = Pitching2022.dropna()
#SPlitting Columns 
Pitching2010[['APP', 'GS']] = Pitching2010['APP-GS'].str.split('-', expand = True)
Pitching2011[['APP', 'GS']] = Pitching2011['APP-GS'].str.split('-', expand = True)
Pitching2012[['APP', 'GS']] = Pitching2012['APP-GS'].str.split('-', expand = True)
Pitching2013[['APP', 'GS']] = Pitching2013['APP-GS'].str.split('-', expand = True)
Pitching2014[['APP', 'GS']] = Pitching2014['APP-GS'].str.split('-', expand = True)
Pitching2015[['APP', 'GS']] = Pitching2015['APP-GS'].str.split('-', expand = True)
Pitching2016[['APP', 'GS']] = Pitching2016['APP-GS'].str.split('-', expand = True)
Pitching2017[['APP', 'GS']] = Pitching2017['APP-GS'].str.split('-', expand = True)
Pitching2018[['APP', 'GS']] = Pitching2018['APP-GS'].str.split('-', expand = True)
Pitching2019[['APP', 'GS']] = Pitching2019['APP-GS'].str.split('-', expand = True)
Pitching2020[['APP', 'GS']] = Pitching2020['APP-GS'].str.split('-', expand = True)
Pitching2021[['APP', 'GS']] = Pitching2021['APP-GS'].str.split('-', expand = True)
Pitching2022[['APP', 'GS']] = Pitching2022['APP-GS'].str.split('-', expand = True)


# In[11]:


#Weighted scores for FIPer 2010
wHR10= Pitching2010['HR'] * 13
wK10 = Pitching2010['SO'] * 2
wBB10 = Pitching2010['BB'] * 3
#Scores for FIPer 2010
HR10 = Pitching2010['HR']
K10 = Pitching2010['SO']
BB10 = Pitching2010['BB']


#Weighted Scores for FIPer 2011
wHR11= Pitching2011['HR'] * 13
wK11 = Pitching2011['SO'] * 2
wBB11 = Pitching2011['BB'] * 3
#Scores for FIPer 2011
HR11 = Pitching2011['HR']
K11 = Pitching2011['SO']
BB11 = Pitching2011['BB']


#Weighted Scores for FIPer 2012
wHR12= Pitching2012['HR'] * 13
wK12 = Pitching2012['SO'] * 2
wBB12 = Pitching2012['BB'] * 3
#Scores for FIPer 2012
HR12 = Pitching2012['HR']
K12 = Pitching2012['SO']
BB12 = Pitching2012['BB']

#Weighted Scores for FIPer 2013
wHR13= Pitching2013['HR'] * 13
wK13 = Pitching2013['SO'] * 2
wBB13 = Pitching2013['BB'] * 3
#Scores for FIPer 2013
HR13 = Pitching2013['HR']
K13 = Pitching2013['SO']
BB13 = Pitching2013['BB']


#Weighted Scores for FIPer 2014
wHR14= Pitching2014['HR'] * 13
wK14 = Pitching2014['SO'] * 2
wBB14 = Pitching2014['BB'] * 3
#Scores for FIPer 2014
HR14 = Pitching2014['HR']
K14 = Pitching2014['SO']
BB14 = Pitching2014['BB']

#Weighted Scores for FIPer 2015
wHR15= Pitching2015['HR'] * 13
wK15 = Pitching2015['SO'] * 2
wBB15 = Pitching2015['BB'] * 3
#Scores for FIPer 2015
HR15 = Pitching2015['HR']
K15 = Pitching2015['SO']
BB15 = Pitching2015['BB']


#Weighted Scores for FIPer 2016
wHR16= Pitching2016['HR'] * 13
wK16 = Pitching2016['SO'] * 2
wBB16 = Pitching2016['BB'] * 3
#Scores for FIPer 2016
HR16 = Pitching2016['HR']
K16 = Pitching2016['SO']
BB16 = Pitching2016['BB']


#Weighted Scores for FIPer 2017
wHR17= Pitching2017['HR'] * 13
wK17 = Pitching2017['SO'] * 2
wBB17 = Pitching2017['BB'] * 3
#Scores for FIPer 2017
HR17 = Pitching2017['HR']
K17 = Pitching2017['SO']
BB17 = Pitching2017['BB']


#Weighted Scores for FIPer 2018
wHR18= Pitching2018['HR'] * 13
wK18 = Pitching2018['SO'] * 2
wBB18 = Pitching2018['BB'] * 3
#Scores for FIPer 2018
HR18 = Pitching2018['HR']
K18 = Pitching2018['SO']
BB18 = Pitching2018['BB']


#Weighted Scores for FIPer 2019
wHR19= Pitching2019['HR'] * 13
wK19 = Pitching2019['SO'] * 2
wBB19 = Pitching2019['BB'] * 3
#Scores for FIPer 2019
HR19 = Pitching2019['HR']
K19 = Pitching2019['SO']
BB19 = Pitching2019['BB']


#Weighted Scores for FIPer 2020
wHR20= Pitching2020['HR'] * 13
wK20 = Pitching2020['SO'] * 2
wBB20 = Pitching2020['BB'] * 3
#Scores for FIPer 2020
HR20 = Pitching2010['HR']
K20 = Pitching2020['SO']
BB20 = Pitching2020['BB']


#Weighted Scores for FIPer 2021
wHR21= Pitching2021['HR'] * 13
wK21 = Pitching2021['SO'] * 2
wBB21 = Pitching2021['BB'] * 3
#Scores for FIPer 2021
HR21 = Pitching2021['HR']
K21 = Pitching2021['SO']
BB21 = Pitching2021['BB']


#Weighted Scores for FIPer 2022
wHR22= Pitching2022['HR'] * 13
wK22 = Pitching2022['SO'] * 2
wBB22 = Pitching2022['BB'] * 3 
#Scores for FIPer 2022
HR22 = Pitching2022['HR']
K22 = Pitching2022['SO']
BB22 = Pitching2022['BB']


# In[27]:


#Replacement Level
GS10 = Pitching2010['GS']
GS11 = Pitching2011['GS']
GS12 = Pitching2012['GS']
GS13 = Pitching2013['GS']
GS14 = Pitching2014['GS']
GS15 = Pitching2015['GS']
GS16 = Pitching2016['GS']
GS17 = Pitching2017['GS']
GS18 = Pitching2018['GS']
GS19 = Pitching2019['GS']
GS20 = Pitching2020['GS']
GS21 = Pitching2021['GS']
GS22 = Pitching2022['GS']

APP10 = Pitching2010['APP']
APP11 = Pitching2011['APP']
APP12 = Pitching2012['APP']
APP13 = Pitching2013['APP']
APP14 = Pitching2014['APP']
APP15 = Pitching2015['APP']
APP16 = Pitching2016['APP']
APP17 = Pitching2017['APP']
APP18 = Pitching2018['APP']
APP19 = Pitching2019['APP']
APP20 = Pitching2020['APP']
APP21 = Pitching2021['APP']
APP22 = Pitching2022['APP']


# In[ ]:


Pitching2010["Replacement Level"] = 0.03*(1-GS10/APP10)+ 0.12*(GS10/APP10)
Pitching2011["Replacement Level"] = 0.03*(1-GS11/APP11)+ 0.12*(GS11/APP11)
Pitching2012["Replacement Level"] = 0.03*(1-GS12/APP12)+ 0.12*(GS12/APP12)
Pitching2013["Replacement Level"] = 0.03*(1-GS13/APP13)+ 0.12*(GS13/APP13)
Pitching2014["Replacement Level"] = 0.03*(1-GS14/APP14)+ 0.12*(GS14/APP14)
Pitching2015["Replacement Level"] = 0.03*(1-GS15/APP15)+ 0.12*(GS15/APP15)
Pitching2016["Replacement Level"] = 0.03*(1-GS16/APP16)+ 0.12*(GS16/APP16)
Pitching2017["Replacement Level"] = 0.03*(1-GS17/APP17)+ 0.12*(GS17/APP17)
Pitching2018["Replacement Level"] = 0.03*(1-GS18/APP18)+ 0.12*(GS18/APP18)
Pitching2019["Replacement Level"] = 0.03*(1-GS19/APP19)+ 0.12*(GS19/APP19)
Pitching2020["Replacement Level"] = 0.03*(1-GS20/APP20)+ 0.12*(GS20/APP20)
Pitching2021["Replacement Level"] = 0.03*(1-GS21/APP21)+ 0.12*(GS21/APP21)
Pitching2022["Replacement Level"] = 0.03*(1-GS22/APP22)+ 0.12*(GS22/APP22)


# In[25]:


#Scatter Plot Model
MeanEra10 = Pitching2010['ERA'].mean()
MeanEra11 = Pitching2011['ERA'].mean()
MeanEra12 = Pitching2012['ERA'].mean()
MeanEra13 = Pitching2013['ERA'].mean()
MeanEra14 = Pitching2014['ERA'].mean()
MeanEra15 = Pitching2015['ERA'].mean()
MeanEra16 = Pitching2016['ERA'].mean()
MeanEra17 = Pitching2017['ERA'].mean()
MeanEra18 = Pitching2018['ERA'].mean()
MeanEra19 = Pitching2019['ERA'].mean()
MeanEra20 = Pitching2020['ERA'].mean()
MeanEra21 = Pitching2021['ERA'].mean()
MeanEra22 = Pitching2022['ERA'].mean()

ERAavgs = [MeanEra10,MeanEra11,MeanEra12,MeanEra13,MeanEra14,MeanEra15,MeanEra16,
          MeanEra17,MeanEra18,MeanEra19,MeanEra20,MeanEra21,MeanEra22]



#Frequency model
Pitching2010['Frequency']= Pitching2010['IP']/Pitching2010['IP'].sum()
Pitching2011['Frequency']= Pitching2011['IP']/Pitching2011['IP'].sum()
Pitching2012['Frequency']= Pitching2012['IP']/Pitching2012['IP'].sum()
Pitching2013['Frequency']= Pitching2013['IP']/Pitching2013['IP'].sum()
Pitching2014['Frequency']= Pitching2014['IP']/Pitching2014['IP'].sum()
Pitching2015['Frequency']= Pitching2015['IP']/Pitching2015['IP'].sum()
Pitching2016['Frequency']= Pitching2016['IP']/Pitching2016['IP'].sum()
Pitching2017['Frequency']= Pitching2017['IP']/Pitching2017['IP'].sum()
Pitching2018['Frequency']= Pitching2018['IP']/Pitching2018['IP'].sum()
Pitching2019['Frequency']= Pitching2019['IP']/Pitching2019['IP'].sum()
Pitching2020['Frequency']= Pitching2020['IP']/Pitching2020['IP'].sum()
Pitching2021['Frequency']= Pitching2021['IP']/Pitching2021['IP'].sum()
Pitching2022['Frequency']= Pitching2022['IP']/Pitching2022['IP'].sum()


Pitching2010['wERA']=Pitching2010['Frequency']* Pitching2010['ERA']
Pitching2011['wERA']=Pitching2011['Frequency']* Pitching2011['ERA']
Pitching2012['wERA']=Pitching2012['Frequency']* Pitching2012['ERA']
Pitching2013['wERA']=Pitching2013['Frequency']* Pitching2013['ERA']
Pitching2014['wERA']=Pitching2014['Frequency']* Pitching2014['ERA']
Pitching2015['wERA']=Pitching2015['Frequency']* Pitching2015['ERA']
Pitching2016['wERA']=Pitching2016['Frequency']* Pitching2016['ERA']
Pitching2017['wERA']=Pitching2017['Frequency']* Pitching2017['ERA']
Pitching2018['wERA']=Pitching2018['Frequency']* Pitching2018['ERA']
Pitching2019['wERA']=Pitching2019['Frequency']* Pitching2019['ERA']
Pitching2020['wERA']=Pitching2020['Frequency']* Pitching2020['ERA']
Pitching2021['wERA']=Pitching2021['Frequency']* Pitching2021['ERA']
Pitching2022['wERA']=Pitching2022['Frequency']* Pitching2022['ERA']

wMeanEra10 = Pitching2010['wERA'].mean()
wMeanEra11 = Pitching2011['wERA'].mean()
wMeanEra12 = Pitching2012['wERA'].mean()
wMeanEra13 = Pitching2013['wERA'].mean()
wMeanEra14 = Pitching2014['wERA'].mean()
wMeanEra15 = Pitching2015['wERA'].mean()
wMeanEra16 = Pitching2016['wERA'].mean()
wMeanEra17 = Pitching2017['wERA'].mean()
wMeanEra18 = Pitching2018['wERA'].mean()
wMeanEra19 = Pitching2019['wERA'].mean()
wMeanEra20 = Pitching2020['wERA'].mean()
wMeanEra21 = Pitching2021['wERA'].mean()
wMeanEra22 = Pitching2022['wERA'].mean()

AVG_Data1= [['2010' ,wMeanEra10],
        ['2011' ,wMeanEra11],
        ['2012' ,wMeanEra12],
        ['2013' ,wMeanEra13],
        ['2014', wMeanEra14],
        ['2015', wMeanEra15],
        ['2016' , wMeanEra16],
        ['2017' ,wMeanEra17],
        ['2018' ,wMeanEra18],
        ['2019' , wMeanEra19],
        ['2020', wMeanEra20],
        ['2021', wMeanEra21],
        ['2022', wMeanEra22]]



# In[31]:


#Pitchers K Rate
Pitching2010['K%'] = Pitching2010['SO']/Pitching2010['AB']
Pitching2011['K%'] = Pitching2011['SO']/Pitching2011['AB']
Pitching2012['K%'] = Pitching2012['SO']/Pitching2012['AB']
Pitching2013['K%'] = Pitching2013['SO']/Pitching2013['AB']
Pitching2014['K%'] = Pitching2014['SO']/Pitching2014['AB']
Pitching2015['K%'] = Pitching2015['SO']/Pitching2015['AB']
Pitching2016['K%'] = Pitching2016['SO']/Pitching2016['AB']
Pitching2017['K%'] = Pitching2017['SO']/Pitching2017['AB']
Pitching2018['K%'] = Pitching2018['SO']/Pitching2018['AB']
Pitching2019['K%'] = Pitching2019['SO']/Pitching2019['AB']
Pitching2020['K%'] = Pitching2020['SO']/Pitching2020['AB']
Pitching2021['K%'] = Pitching2021['SO']/Pitching2021['AB']
Pitching2022['K%'] = Pitching2022['SO']/Pitching2022['AB']


# In[32]:


#K to walk ratio
Pitching2010['K/BB'] = Pitching2010['SO']/Pitching2010['BB']
Pitching2011['K/BB'] = Pitching2011['SO']/Pitching2011['BB']
Pitching2012['K/BB'] = Pitching2012['SO']/Pitching2012['BB']
Pitching2013['K/BB'] = Pitching2013['SO']/Pitching2013['BB']
Pitching2014['K/BB'] = Pitching2014['SO']/Pitching2014['BB']
Pitching2015['K/BB'] = Pitching2015['SO']/Pitching2015['BB']
Pitching2016['K/BB'] = Pitching2016['SO']/Pitching2016['BB']
Pitching2017['K/BB'] = Pitching2017['SO']/Pitching2017['BB']
Pitching2018['K/BB'] = Pitching2018['SO']/Pitching2018['BB']
Pitching2019['K/BB'] = Pitching2019['SO']/Pitching2019['BB']
Pitching2020['K/BB'] = Pitching2020['SO']/Pitching2020['BB']
Pitching2021['K/BB'] = Pitching2021['SO']/Pitching2021['BB']
Pitching2022['K/BB'] = Pitching2022['SO']/Pitching2022['BB']


# In[ ]:


#Strikeout Rate


# In[22]:


# Create the pandas DataFrame
wERA_All = pd.DataFrame(AVG_Data1, columns = ['Year', 'wERA'])
 
# print dataframe.
AVG_Data['wERA'].plot()
plt.show()


# In[26]:


# initialize list of lists
data = [['2010' ,MeanEra10],
       ['2011' ,MeanEra11],
       ['2012' ,MeanEra12],
       ['2013' ,MeanEra13],
       ['2014', MeanEra14],
       ['2015', MeanEra15],
       ['2016' , MeanEra16],
       ['2017' ,MeanEra17],
       ['2018' ,MeanEra18],
       ['2019' , MeanEra19],
       ['2020', MeanEra20],
       ['2021', MeanEra21],
       ['2022', MeanEra22]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns = ['Year', 'ERA'])

# print dataframe.
df


# In[55]:


#FIP
LeagueFIP = 3.20

Pitching2010['FIP'] = ((wHR10+wBB10)-wK10)/(HR10 + BB10 +K10+ LeagueFIP )
Pitching2011['FIP'] = ((wHR11+wBB11)-wK11)/(HR11 + BB11 +K11+ LeagueFIP )
Pitching2012['FIP'] = ((wHR12+wBB12)-wK12)/(HR12 + BB12 +K12+ LeagueFIP )
Pitching2013['FIP'] = ((wHR13+wBB13)-wK13)/(HR13 + BB13 +K13+ LeagueFIP )
Pitching2014['FIP'] = ((wHR14+wBB14)-wK14)/(HR14 + BB14 +K14+ LeagueFIP )
Pitching2015['FIP'] = ((wHR15+wBB15)-wK15)/(HR15 + BB15 +K15+ LeagueFIP )
Pitching2016['FIP'] = ((wHR16+wBB16)-wK16)/(HR16 + BB16 +K16+ LeagueFIP )
Pitching2017['FIP'] = ((wHR17+wBB17)-wK17)/(HR17 + BB17 +K17+ LeagueFIP )
Pitching2018['FIP'] = ((wHR18+wBB18)-wK18)/(HR18 + BB18 +K18+ LeagueFIP )
Pitching2019['FIP'] = ((wHR19+wBB19)-wK19)/(HR19 + BB19 +K19+ LeagueFIP )
Pitching2020['FIP'] = ((wHR20+wBB20)-wK20)/(HR20 + BB20 +K20+ LeagueFIP )
Pitching2021['FIP'] = ((wHR21+wBB21)-wK21)/(HR21 + BB21 +K21+ LeagueFIP )
Pitching2022['FIP'] = ((wHR22+wBB22)-wK21)/(HR22 + BB22 +K22+ LeagueFIP )


# In[57]:


#Data set with keys containing 2010-2022
All_years = pd.concat([Pitching2010,Pitching2011,Pitching2012,Pitching2013,Pitching2014,Pitching2015,Pitching2016,
                    Pitching2017, Pitching2018, Pitching2019,Pitching2020, Pitching2021, Pitching2022],
                       keys = ['Pitching2010','Pitching2011','Pitching2012','Pitching2013','Pitching2014','Pitching2015','Pitching2016',
                    'Pitching2017', 'Pitching2018', 'Pitching2019','Pitching2020', 'Pitching2021', 'Pitching2022'],
                      axis = 0)

All_No_Keys = pd.concat([Pitching2010,Pitching2011,Pitching2012,Pitching2013,Pitching2014,Pitching2015,Pitching2016,
                    Pitching2017, Pitching2018, Pitching2019,Pitching2020, Pitching2021, Pitching2022],
                      axis = 0)


# In[58]:


#BoxPlot Plus 20 at-bats
Plus20IP_10 = Pitching2010[Pitching2010['IP'] > 20]
Plus20IP_11 = Pitching2011[Pitching2011['IP'] > 20]
Plus20IP_12 = Pitching2012[Pitching2012['IP'] > 20]
Plus20IP_13 = Pitching2013[Pitching2013['IP'] > 20]
Plus20IP_14 = Pitching2014[Pitching2014['IP'] > 20]
Plus20IP_15 = Pitching2015[Pitching2015['IP'] > 20]
Plus20IP_16 = Pitching2016[Pitching2016['IP'] > 20]
Plus20IP_17 = Pitching2017[Pitching2017['IP'] > 20]
Plus20IP_18 = Pitching2018[Pitching2018['IP'] > 20]
Plus20IP_19 = Pitching2019[Pitching2019['IP'] > 20]
Plus20IP_20 = Pitching2020[Pitching2020['IP'] > 20]
Plus20IP_21 = Pitching2021[Pitching2021['IP'] > 20]
Plus20IP_22 = Pitching2022[Pitching2022['IP'] > 20]
Plus20IP_All = All_No_Keys[All_No_Keys['AB'] > 20]


# In[108]:


#Open dataframe for boxplot values of FIP
FIP_BoxPlot = pd.DataFrame()


# In[109]:


FIP_BoxPlot['All'] = Plus20IP_All['FIP']


# In[110]:


#Adding columns to a dataframe for FIP Boxplot
FIP_BoxPlot['2010'] = Plus20IP_10['FIP']
FIP_BoxPlot['2011'] = Plus20IP_11['FIP']
FIP_BoxPlot['2012'] = Plus20IP_12['FIP']
FIP_BoxPlot['2013'] = Plus20IP_13['FIP']
FIP_BoxPlot['2014'] = Plus20IP_14['FIP']
FIP_BoxPlot['2015'] = Plus20IP_15['FIP']
FIP_BoxPlot['2016'] = Plus20IP_16['FIP']
FIP_BoxPlot['2017'] = Plus20IP_17['FIP']
FIP_BoxPlot['2018'] = Plus20IP_18['FIP']
FIP_BoxPlot['2019'] = Plus20IP_19['FIP']
FIP_BoxPlot['2020'] = Plus20IP_20['FIP']
FIP_BoxPlot['2021'] = Plus20IP_21['FIP']
FIP_BoxPlot['2022'] = Plus20IP_22['FIP']


# In[119]:


FIP_BoxPlot[FIP_BoxPlot['All']> 0.95]


# In[70]:


FIP_BoxPlot.plot(kind = "box", figsize = (16,6))
plt.title("2010 - 2022 FIP")
plt.style.use("fivethirtyeight")


# In[73]:


#Feature Engineering for outlier detection 
Q1 = FIP_BoxPlot['2010-2022'].height.quantile(0.25)
Q3 = FIP_BoxPlot['2010-2022'].height.quantile(0.75)
Q1, Q3


# In[ ]:




