# -*- coding: utf-8 -*-

import csv
import pandas as pd
#Activity1
#write the csv file names
file1 = ''
file2 = ''

d1 = []
d2 = []
with open(file1,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        d1.append(i)
        
with open(file2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]

stars_d1 = d1[1:]
stars_d2 = d2[1:]

h = h1+h2

stars_d =[]

for i in stars_d1:
    stars_d.append(i)
#Activity2
#uncomment the correct code to 

#for j in stars_d2:
    #stars_d.append(j)
#for j in star_d2:
    #star_d.append(j)
#for i in stars_d2:
    #stars_d.append(j)
#Activity3
#uncomment the correcct code
#with open("final.csv",'w') as f:
    #csvwriter = csv.writer(f)
    #csvwriter.writerows(h)   
    #csvwriter.writerows(stars_d)
#with open("final.csv",'w',encoding='utf8') as f:
    #csvwriter = csv.writer(f)
    #csvwriter.writerow(h)   
    #csvwriter.writerows(stars_d)
#with open("final.csv",'w',encoding='utf8') as f:
    #csvwriter = csv.writer(f)
    #csvwriter.writerow(h)   
    #csvwriter.writerows(star_d)
    
df = pd.read_csv('final.csv')
df.tail(8)