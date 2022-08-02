# -*- coding: utf-8 -*-
"""EDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15vO609dvv35l-a6PB2Zgh4KWOFzf3-Vy
"""

import numpy as np
import pandas as pd

"""
# **Import and Combine appointments json and user json on user column**"""

df1=pd.read_csv("appointments.csv")
df2=pd.read_csv("user.csv")
df1["user"]=[a for a in range(1,len(df1)+1)]

df3=pd.merge(df2,df1,how="outer")
df3=df3.iloc[:,1:]
df3.head()

df3.tail()

"""# **Finding no of appoinntments for each user and adding this as a column to df1**"""

import yaml
def no_of_appointments(aan):
    no=[]
    for a in range(len(aan)):
        x=yaml.load(aan[a])
        dd=pd.DataFrame(x)
        no.append(len(dd))
    return no

no_of_appointments_for_each_user=no_of_appointments(df1["appointments"])

df1["no_of_appointments"]=no_of_appointments_for_each_user

df3=pd.merge(df2,df1,how="outer")
df3=df3.iloc[:,1:]
df3.head()

"""# **Flattening the json Data**"""

def list_of_lists_of_dictionaries_to_df(aan):
    no=pd.DataFrame()
    for a in range(len(aan)):
        x=yaml.load(aan[a])
        dd=pd.DataFrame(x)
        if a==0:
            no=dd
            continue
        no=pd.concat([no,dd],axis=0)
    no.index=[a for a in range(len(no))]
    return no

appointments=list_of_lists_of_dictionaries_to_df(df1["appointments"])

appointments.head()

time=pd.to_datetime(appointments["u'date'"],unit="s")

appointments["u'date'"]=time

appointments.head()

appointments["u'doctor'"].value_counts()

import matplotlib.pyplot as plt

appointments["u'doctor'"].value_counts().plot(kind="bar")

symptom=list_of_lists_of_dictionaries_to_df(df2["symptoms"])

symptom.head()

timestamp=pd.to_datetime(symptom["date"],unit="s")

timestamp

symptom["date"]=timestamp

symptom.head()

symptom_name=symptom["name"].value_counts()

symptom_name.plot(kind="bar")

symptom_strength=symptom["strength"]

symptom_strength.mean()

symptom_strength.median()

"""# **3b)**"""

constant=list_of_lists_of_dictionaries_to_df(df3["constants"])

timestamp=pd.to_datetime(constant["date"],unit="s")

constant["date"]=timestamp

constant.head()

symptom.head()

appointments.head()

t=pd.to_datetime("today")<constant["date"][0]
t
#t/np.timedelta64(1,"D")

def finding_constant_date_duration(aan):
    no=[]
    for a in range(len(aan)):
        x=yaml.load(aan[a])
        dd=pd.DataFrame(x)
        dd["date"]=pd.to_datetime(dd["date"],unit="s")
        for z in range(0,len(dd["date"])):
            date=np.nan
            if ((pd.to_datetime("today")-dd["date"][z])/np.timedelta64(1,"D")>365):
                date=dd["date"][z]
            elif z!=len(dd["date"])-1:
                continue
            else:
                date=np.nan
            if z==0:
                no.append(date)
                break
            no.append(date)
            break
  #  no.index=[a for a in range(len(no))]
    return no

def checking_more_than_1_symptoms_before_and_after_and_carrying_out_their_strength(aan,m):
    before=pd.DataFrame()
    after=pd.DataFrame()
    for a in range(len(aan)):
        x=yaml.load(aan[a])
        dd=pd.DataFrame(x)
        dd["date"]=pd.to_datetime(dd["date"],unit="s")
        try:
            ddd=dd[dd["date"]>m[a]]
            fff=dd[dd["date"]<m[a]]
        except:
            continue
        ddd=pd.DataFrame(ddd["name"].value_counts())
        fff=pd.DataFrame(fff["name"].value_counts())
        ddd=ddd[ddd>1]
        fff=fff[fff>1]
        ddd=pd.DataFrame(ddd)
        fff=pd.DataFrame(fff)
        if a==0:
            before=ddd
            after=fff
            continue
        before=pd.concat([before,ddd],axis=0)
        after=pd.concat([after,fff],axis=0)
    return before,after

constant_dates_one_year_before=finding_constant_date_duration(df3["constants"])

constant_dates_one_year_before

before,after=checking_more_than_1_symptoms_before_and_after_and_carrying_out_their_strength(df3["symptoms"],constant_dates_one_year_before)

a,b=before,after

before,after=a,b

before.to_csv("Before.csv")
after.to_csv("After.csv")
before=pd.read_csv("Before.csv",usecols=[0,1])
before.columns=["Disease","Strength"]
after=pd.read_csv("After.csv",usecols=[0,1])
after.columns=["Disease","Strength"]

before=before.groupby(by="Disease")

before.sum()

after=after.groupby(by="Disease")

after.sum()

before.sum().plot(kind="bar")

after.sum().plot(kind="bar")

"""# **The 10% of users whose symptom.strength is lowest, and identify what is different about them compared to the other 90 percent (ex: do they have lower age? more activities?)**"""

def mean_strength(aan):
    df9=[]
    for a in range(len(aan)):
        x=yaml.load(aan[a])
        dd=pd.DataFrame(x)
        df9.append(dd["strength"].mean())
    return df9
n=mean_strength(df3["symptoms"])
df3["mean_strength"]=n
df3.head()

m=no_of_appointments(df3["activities"])
df3["no_of_activities"]=m

_10_percent=df3.sort_values(by="mean_strength").head(100)
_10_percent["gender"].value_counts()

var=_10_percent["age"].value_counts().sort_index()

var=pd.DataFrame(var)
vr=pd.DataFrame()
vr["age range"]=["15-30","31-50","50-80"]
vr["no_of_people"]=([var[0:13].sum()[0],var[13:28].sum()[0],var[28:].sum()[0]])

vr

per=_10_percent["no_of_activities"].value_counts().sort_index()

per=pd.DataFrame(per)
pre=pd.DataFrame()
pre["activities_range"]=["2-10","10-20","20-30"]
pre["no_of_activities"]=([per[0:9].sum()[0],per[9:19].sum()[0],per[19:].sum()[0]])

pre

"""# **users that have >3 cases of a specific symptom**"""

no_of_symptoms=no_of_appointments(df3["symptoms"])#calculating the no of symptoms to a person with the same function from which no of appoinntmennts was calculated

df3["no_of_symptoms"]=no_of_symptoms

def list_of_lists_of_dictionaries(aan):
    no=pd.DataFrame()
    for a in range(len(aan)):
        x=yaml.load(aan[a])
        dd=pd.DataFrame(x)
        dd=pd.DataFrame(dd["name"].value_counts())
        dd=dd[dd["name"]>3]
        print(dd)
        if a==0:
            no=dd
            continue
        no=pd.concat([no,dd],axis=0)
    no.index=[a for a in range(len(no))]
    return no

hello=list_of_lists_of_dictionaries(df3["symptoms"])

def mean_after_activity(aan):
    df9=[]
    for a in range(len(aan)):
        x=yaml.load(aan[a])
        dd=pd.DataFrame(x)
        df9.append(dd["after"].mean())
    return df9
n=mean_after_activity(df3["activities"])
df3["mean_activity_after"]=n
df3.head()

df3.head()

symptom["date"]=timestamp
symptom=symptom.sort_values(by="date")
symptom_strength_time_series_analysis=pd.DataFrame(symptom)

plt.plot(df3["mean_strength"])

plt.plot(df3["mean_activity_after"])

"""# **How would you find users that are similar to each other based on the data attributes they have?¶**

# *Ans :        By using unique function on dataframe.user column we can figure out which user have same data or just by applying duplicate function we can do achieve the same result*
"""

