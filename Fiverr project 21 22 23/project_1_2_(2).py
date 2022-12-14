# -*- coding: utf-8 -*-
"""Project_1_2 (2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tp8vVS7lReF7whT35HcUl2d44sLY0Vlf
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""(i) Load the .csv file into the notebook."""

df=pd.read_csv("https://raw.githubusercontent.com/DataTensor/hdb/main/resale-flat-prices.csv")

df.sample(3)

"""(ii) Summarize the information that can be derived from the dataset, including key
features (columns), range of values, and missing / non-useful values. All the
information should be derived by necessary Python codes.
"""

df.columns

df.describe()

df.info()

df.isna().sum()# sum of missing values in each column

df.dtypes

df.shape

"""(iii) Explain TWO (2) potential insights that can be derived from the dataset."""

df.groupby("lease_commence_date").mean()["resale_price"].plot()

df.groupby("flat_model").mean()["resale_price"]

"""(i) Refer to Q1(a)(ii), remove all the data rows with missing data values."""

df.dropna(inplace=True)
df.shape

"""(ii) In Singapore, HDB flats have a 99 years’ leasehold. Compute the remaining
lease in years for each transacted flat on its transacted date.
"""

remaining_lease_in_years = 99-(2021-df["lease_commence_date"])

remaining_lease_in_years

df["remaining_lease_in_years"] = remaining_lease_in_years

"""(iii) List out the top ten of remaining lease in years (computed by Q1(b)(ii) having
the greatest number of transacted flats.
"""

df.groupby("remaining_lease_in_years").count().sort_values(by="street_name",ascending=False).head(10).index

df.to_csv("Cleaned.csv")

df.head(1)

"""(a) Design and apply a Python ORM(s) (Object Relational Mapping) to store the CSV file
obtained in Q1(c). Please specify a table class before inserting the values into the
database.
"""

from sqlalchemy import Column, Integer, Float, Date, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
#Create the database
engine = create_engine('sqlite:///csv_test.db')
Base.metadata.create_all(engine)
class Resale_Flat_Prices(Base):
    __tablename__ = 'Resale_Flat_Prices'
    #tell SQLAlchemy the name of column and its attributes:
    transaction_id = Column(Integer,primary_key=True) 
    month = Column(Date)
    town = Column(String)
    flat_type = Column(String)
    block = Column(String)
    street_name = Column(String)
    storey_range = Column(String)
    floor_area_sqm = Column(Float)
    flat_model = Column(String)
    lease_commence_date = Column(Integer)
    resale_price = Column(Float)

data = pd.read_csv("Cleaned.csv")
data = data.values.tolist()
#Create the session
session = sessionmaker(bind=engine)
s = session()
for i in data:
  record = Resale_Flat_Prices(**{"transaction_id" : i[1],
                              "month" : pd.to_datetime(i[2]), "town" : i[3], "flat_type" : i[4], "block" : i[5],
                'street_name' : i[6],"storey_range" : i[7],"floor_area_sqm" : i[8],"flat_model" : i[9],"lease_commence_date" : i[10],"resale_price" : i[11]})
  s.add(record) #Add all the records
s.commit() #Attempt to commit all the records
s.close() #Close the connection

"""(b) Compose queries on the database and answer the following questions:
(i) What is the total number of transactions for each month?
(ii) Sort the data by town and the number of resale transactions in descending order.
(iii) For resales transacted on and after Jan 2019 and storey range being level 10
and above, what are the top three towns having the greatest number of
transactions?
"""

data = s.query(Resale_Flat_Prices)

date=[]
for a in data:
  date.append(a.month)
uni = list(dict.fromkeys(date))
for a in uni:
  co=date.count(a)
  print(a,co)

data1 = s.query(Resale_Flat_Prices).order_by(Resale_Flat_Prices.town)
#for a in data1:
#  print(a.town)

data2 = s.query(Resale_Flat_Prices).order_by(Resale_Flat_Prices.resale_price)
data2 = data2[::-1]
#for a in data2:
#  print(a.resale_price)

data3 = s.query(Resale_Flat_Prices).filter(Resale_Flat_Prices.month>=pd.to_datetime("2019-01"))

data4 = []
for a in data3:
  b=a.storey_range.split(" ")
  if int(b[0])>=10:
    data4.append(a)

towns = []
for a in data4:
  towns.append(a.town)
uni = list(dict.fromkeys(towns))
town_transaction = {}
for b in uni:
  co = towns.count(b)
  town_transaction[b] = co
a=sorted(town_transaction.items(), key=lambda x: x[1], reverse=True)
a[0:3]

"""(a) Load the CSV file obtained from Q1(c) to a Pandas dataframe and derive the answers
for the same three questions in Q2(b)
"""

df=pd.read_csv("Cleaned.csv")

df.month.value_counts()

df.sort_values(by=["town","resale_price"],ascending=False)

df.month=pd.to_datetime(df.month)
df1=df[df.month>=pd.to_datetime("2019-01")]
df1

list1=[]
for a in df1.storey_range:
  b=a.split(" ")
  list1.append(int(b[0]))
df1["storey"]=list1

df2=df1[df1.storey>=10]

df2.town.value_counts()[:3]

"""(i) Design a function to find the top three towns of each month with the greatest
number of transactions.
"""

def top_three(dataframe,date):
  top_3=dataframe[dataframe.month==date].town.value_counts()
  return top_3.head(3)

for a in df.month.unique():
  print(a)
  print(top_three(df,a))

"""(ii) Draw ONE (1) figure to show the median resale price in 2020 of each town."""

data_2020=df[df.month>=pd.to_datetime("2020-01")]
data_2020.groupby('town')['resale_price'].median().plot(kind="bar",color=list("rgbmy"))

"""(iii) For the town with the greatest number of transactions in 2020, draw ONE (1)
figure to visualize the median resale price per flat type for each month.
"""

town_with_most_transactions=data_2020.town.value_counts().index[0]
df3=data_2020[data_2020.town==town_with_most_transactions]
df3.groupby(["flat_type","month"]).median()["resale_price"].plot(kind="bar",color=list("rgmbkc"))

"""we cant find out correlation between storey range and resale price,as the storey range is in string format, we can get it by splitting storey range in lower and upper storey limit and then find the correlation"""

list1=[]
list2=[]
for a in df.storey_range:
  b=a.split(" ")
  list1.append(int(b[0]))
  list2.append(int(b[-1]))
df["storey_lower_limit"]=list1
df["storey_upper_limit"]=list2
df.loc[:,["storey_lower_limit","storey_upper_limit","resale_price"]].corr().plot(kind="bar")

"""(v) Is there any correlation between the remaining lease in years and resale price?
Draw ONE (1) figure to visualize the correlation.
"""

df.loc[:,["remaining_lease_in_years","resale_price"]].corr().plot(kind="bar")

"""(vi) For Yishun, draw ONE (1) figure to visualize how was the median resale price
being changed over time per flat type?
"""

df[df.town=="YISHUN"].groupby(["flat_type","month"]).median()["resale_price"].unstack().T.plot()

"""some lines are broken because of the missing data"""

