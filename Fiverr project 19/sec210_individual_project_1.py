# -*- coding: utf-8 -*-
"""SEC210 Individual Project 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11UZj5aEwG5Ms9UiX_yoK_9eH2uOm6QQ1

# Individual Project 1

<table align="left">
    <tr>
        <td style="text-align:left"><b>Course Name:</b></td>
        <td style="text-align:left">Systems & Technologies</td>
        <td style="text-align:left"><b>Course Code:</b></td>
        <td style="text-align:left">SEC210</td>
    </tr>
    <tr>
        <td style="text-align:left"><b>Release Date:</b></td>
        <td style="text-align:left">Sunday, February 7th, 2021</td>
        <td style="text-align:left"><b>Release Time:</b></td>
        <td style="text-align:left">08:00</td>
    </tr>
    <tr>
        <td style="text-align:left"><b>Submission Date:</b></td>
        <td style="text-align:left">Sunday, February 21st, 2021</td>
        <td style="text-align:left"><b>Submission Time:</b></td>
        <td style="text-align:left">08:00<td>
    </tr>
    <tr>
        <td style="text-align:left"><b>Submission Note:</b></td>
        <td style="text-align:left" colspan="3">Submission will be completed using the assignment link on Week 6 in Moodle<td>
    </tr>
    <tr>
        <td style="text-align:left"><b>Course Learning Outcome:</b></td>
        <td style="text-align:left"> 2 (20%) and 5 (80%)</td>
        <td style="text-align:left"><b>% of Final Grade:</b></td>
        <td style="text-align:left">20%</td>
    </tr>
</table>

### Instructions
<b>Starting the project</b>
- Please download and put the <code>SEC210 Individual Project 1</code> notebook and <code>covid_data.txt</code> in the same folder on your lapptop
- Open Navigator and launch Juypter Notebook
- Go to the folder above and open <code>SEC210 Individual Project 1</code>
- Run the cell <code>Step 1 - Importing the Covid 19 Data</code>

---

Please update the information in the markdown cell below. You will need to put in your ID number, Student Name and Program of Study.

<b>Student ID#:</b> Please enter your ID here

<b>Student Name:</b> Please enter your full name here

<b>Program of Study:</b> Please enter your Program of Study (for example Homeland Security)

---

## Project 1 Description

During the first four weeks of the Spring 2021 semester we have looked at the basics of Python. 

We focused on
- integers <code>int</code>
- floating point numbers <code>float</code>
- strings <code>str</code>
- lists <code>list</code>

You will be working with <b>Covid-19</b> data from January 30th, 2021.

---

## <font color="blue">Step 1 - Importing the Covid 19 Data</font>
<b>Please do not touch the code below.</b> 

Just run the cell to load the data. Please make sure you have the <code>covid_data.txt</code> file saved in the same folder as this Juypter Notebook</b> 

All of the data will be stored in a new <code>list</code> called <code>covid_data</code>. This covid_data list can be used for the rest of the indivudal project
"""

import csv

covid_data = []

with open('covid_data.txt', newline = '') as covid:      
    
    txt_reader = csv.reader(covid, delimiter='\t')
    for row in txt_reader:
        covid_data.append(row)

"""---

## <font color="green">Student Task 1  (CLO 5):- <u>(Marks: 5)</u></font>
How many items are in the <code>covid_data</code> list?
"""

#<--Student code for task 1 goes below-->

print("There are ",len(covid_data)," items in covid_data_list.")

"""---

## <font color="orange">Student Task 2 (CLO 5):- <u>(Marks: 10)</u></font>

Using the <code>type</code> function that we used in Week 2 please determine the type of each item in <code>covid_data</code> list. You might use a <code>for</code> loop to go through each item in the list. We covered this in class in Week 4
"""

#<--Student code for task 2 goes below-->

for a in covid_data:
  print(type(a))

"""---

## <font color="blue">Student Task 3 (CLO 5):- <u>(Marks: 30)</u></font>
- Create a new list called <code>asia_countries</code>. Using a <code>for</code> loop along with an <code>if</code> statement go through the <code>covid_data</code> list and store all the countries from Asia in this new <code>asia_countries</code>.
- At the end please print out the number of countries in the <code>asia_countries</code> list.
"""

#<--Student code for task 3 goes below-->
asia_countries=[]
for a in covid_data:
  if a[1]=="Asia":
    asia_countries.append(a[2])

len(asia_countries)

"""---

## <font color="red">Student Task 4A (CLO 5):- <u>(Marks: 15)</u></font>
- Create a new list called <code>highest_ten_deaths</code>
- Store the countries that are in the highest 10 deaths per million from the <code>covid_data</code>
"""

#<--Student code for task 4A goes below-->
highest_ten_deaths_1=[]
all_countries={}
for a in covid_data[1:]:
  all_countries[a[2]]=a[-2]
for a in all_countries.keys():
  if all_countries[a]=="":
    all_countries[a]=0
  else:
    all_countries[a]=float(all_countries[a])
all=sorted(all_countries.items(), key=lambda x: x[1],reverse=True)
highest_ten_deaths_1=all[0:10]

highest_ten_deaths=[]
for a in highest_ten_deaths_1:
  highest_ten_deaths.append(a[0])
print(highest_ten_deaths)

"""## <font color="red">Student Task 4B (CLO 2):- <u>(Marks: 20)</u></font>
During Week 4 we discussed the difference between Data and Information. If you are unsure please refer back to the slides and video recordings of the class from Week 4.

In the <code>markdown</code> cell below please write a 150 word report on the data collected in the text file that was loaded into the <code>covid_data</code> list. 

It may be useful to decribe the data types of the content and then possibly dicuss how this data can be turned into information. You could write some code that would show some of the data being <b>processed</b> into information and displayed visually using packages such as <code>matplotlib</code>. Click <a href="https://matplotlib.org/">here</a> to learn more about the <code>matplotlib</code> visualisation tool in Python that allows us to display information as charts and graphs. It may be useful to click on <b>tutorials</b> in the website.

The dataset has 192 lists(Countries) and each lists has twelve elements, first attribute shows the country code of the country whose data is stated in the list, country attribute contains the name of the country while the date indicates the date at which the reading has been taking or you can say the current data on that date is mentioned here, while the continent shows one of the six possible continent that are possible, same in the way the total deaths indicates the number of deaths so far in that country, new deaths indicates the number of deaths on the mentioned date, same in the case of total and new cases. while the cases per million indicates the number of people affected per ten lacs of population in that country and deaths per million indicates that these number of people died on every million of people in that country.
"""

#matplotlib code at the last

"""---

## <font color="grey">Student Task 5 (CLO 5):- <u>(Marks: 20)</u></font>
- The final step in your project
- The aim of this takes is to create a new list called <code>totals</code> that will hold the <b>total deaths</b> on January 30th by contintent.
- The structure of the list should follow below where
    - totals[0] contains the total deaths for Africa
    - totals[1] contains the total deaths for Asia
    - totals[2] contains the total deaths for Europe
    - totals[3] contains the total deaths for North America
    - totals[4] contains the total deaths for Oceania
    - totals[5] contains the total deaths for South America
- The instuctor should be able to view any total by simplying running the code
"""

#<--Student code for task 5 goes below-->
totals=[]
continents_list=["Africa","Asia","Europe","North America","Oceania","South America"]
for a in continents_list:
  sum=0
  for b in covid_data:
    if b[1]==a:
      if b[6]=="":
        continue
      sum=sum+float(b[6])
  totals.append(sum)

"""---"""

totals

import matplotlib.pyplot as plt
plt.bar([f for f in continents_list],totals)