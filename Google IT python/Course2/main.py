#!/usr/bin/env python3
import csv
from operator import itemgetter
import re

errorFile = open('errorFile.txt')
infoFile = open('infoFile.txt')

er_data=[]
in_data=[]

er_lines = errorFile.readlines()
in_lines = infoFile.readlines()

e_buff=[]
ue_buff=[]
ui_buff=[]
i_buff=[]

for line in er_lines:
        z=re.findall(r"[\w \']*",line)
        e_buff.append(z[0])
        z2=re.findall(r"\(([\w \.]*)",line)
        ue_buff.append(z2[0])
for line in in_lines:
        z=re.findall(r"[\w \']*",line)
        i_buff.append(z[0])
        z2=re.findall(r"\(([\w \.]*)",line)
        ui_buff.append(z2[0])

#print(ui_buff,ue_buff,e_buff,sep='\n')
print(set(ue_buff).union(set(ui_buff)))

error={}
per_user={}

for i in set(e_buff):
        error['Error']=i
        error['Count']=e_buff.count(i)
        er_data.append(error)
        error={}
        
set1=set(ue_buff).union(set(ui_buff))

for j in set1:
        per_user['Username']=j
        per_user['ERROR']=ue_buff.count(j)
        per_user['INFO']=ui_buff.count(j)
        in_data.append(per_user)
        #print(per_user,end='\n\n\n\n')
        per_user={}
        
        
csv_columns1=["Error", "Count"]
csv_columns2=["Username", "INFO", "ERROR"]
#print(er_data,in_data,sep='\n\n')

n_error=sorted(er_data, key=itemgetter('Count'),reverse=True)
n_user=sorted(in_data, key=itemgetter('Username'))

with open('error_message.csv' , 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns1)
    writer.writeheader()
    for data in er_data:
        writer.writerow(data)

