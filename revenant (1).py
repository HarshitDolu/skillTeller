# -*- coding: utf-8 -*-
"""Revenant

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15QOCTIxiq3ZRxpgBHKaMwQLPe1W5ravx
"""

import numpy as np
import pandas as pd

data = pd.read_csv('naukri_com-job_sample.csv')
data.head()

data.drop('jobdescription', axis=1, inplace=True)

data.drop('jobid', axis=1, inplace=True)

data.drop('numberofpositions', axis=1, inplace=True)

data.drop('payrate', axis=1, inplace=True)

data.drop('postdate', axis=1, inplace=True)

data.drop('site_name', axis=1, inplace=True)

data.drop('uniq_id', axis=1, inplace=True)

data.head()

data.education.value_counts()

data.drop('education', axis=1, inplace=True)

data.head()

#data['industry']=data['industry'].replace(('IT-Software / Software Services'),'It/Software',inplace=True)

#data.Item_Fat_Content=data['Item_Fat_Content'].replace(('Low Fat','low fat'),'LF')

data.head(10)

data['industry'] = data['industry'].apply(lambda x:(str(x).split("/")))
#data[['industry','word_countIndustry']].head()

#for i in range(data['industry'].count()):
 # data['industry']=data['industry'][i][

data.tail(5)

lst=[]
for i in range(len(data)):
  lst.append(data['industry'][i][0])

data['industry']=lst

lt=set(lst)
lt

data.head(4)
data.industry.value_counts()

#from sklearn import preprocessing
#label_encoder=preprocessing.LabelEncoder()
#data['industry']=label_encoder.fit_transform(data['industry'])

#for i in range(22000):
#  lst_indus.append(data.industry[i])
#  lst_indus.append(lst[i])

#res_dct={lst_indus[i+1]:lst_indus[i] for i in range(0,len(lst_indus),2)}
#p=res_dct.keys()
#res_dct.get("Banking ")

data.head(5)

data.industry.value_counts().head(11)
#f_lst = ['IT-Software ','Education ','BPO ','Banking ','Recruitment ','Internet ','Pharma ','Medical ','Automobile ','Construction ']

lst_jt=[]
for i in range(len(data)):
  lst_jt.append(data['jobtitle'][i])

dict_ind={'skills':data['skills'],'industry':data['industry'],'jobtitle':data['jobtitle']}
df1=pd.DataFrame(dict_ind)
df1.head()

for j in lt:
  if list(df1[df1['industry']==j].count())[0]<440:
    df1 = df1[df1.industry!=j]

len(df1)

#data['experience']=data['experience'].replace(('Not Mentioned'),'0 - 0 yrs')
#data['experience'] = data['experience'].apply(lambda x:(str(x).split("-")))



#e_lst=[]
#for i in range(0,3000):
#  j=data['experience'][i][0]
#  k=data['experience'][i][1].split(" ")
#  p=int(k[1])
#  h=p-int(j)
#  e_lst.append(h)

#for i in range(19000):
 # e_lst.append(np.random.randint(0,6))

#len(e_lst)

#data['experience']=e_lst

df1.head(4)

for j in lst_jt:
  if list(df1[df1['jobtitle']==j].count())[0]<20:
    df1 = df1[df1.jobtitle!=j]

#df1 = df1.industry.replace('Internet ','E-Commerce ')
df1.head(52)

df2 = pd.read_excel('Book1.xlsx')
joblist = df2['jobtitle']
joblist

st=[]
for i in range(len(df2)):
  st.append(df2.s1[i]+" "+df2.s2[i]+" "+df2.s3[i]+" "+df2.s4[i]+" "+df2.s5[i])
for i in range(len(df2)):
  st[i] = st[i].lower()
st[0]

tj=df2.jobtitle
df1['skill_s']=df1.jobtitle

for i in range(0,len(tj)):
  df1['skill_s']=df1.skill_s.replace(tj[i],st[i])

df1 = df1.drop_duplicates()
df1 = df1.reset_index(drop=True)

#!pip install tika

from tika import parser

raw=parser.from_file("/content/Profile.pdf")   #user input pdf
k=raw['content']
m=k.splitlines()
r=set(m)
lst=[]
for i in range(len(m)):
  if m[i]!='':
    lst.append(m[i])
ts=lst.index('Top Skills')
ln=ts+4
s1=[]
for i in range(ts+1,ln):
  s1.append(lst[i])

test=" ".join(s1)
test

test = test.lower()
ls=[]

def get_jaccard_sim(str1, str2):              #jacard similarity
    a = set(str1.split()) 
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

for j in range(len(df1)):
   ls.append(get_jaccard_sim(test,df1.skill_s[j]))

df1['jacard'] = ls
g = set(ls)
final = list(g)
final.sort(reverse=True)

t=[]
y=[]

for d in range(len(final)-1):
  t = df1[df1['jacard']==final[d]].jobtitle
  r = set(t)
  y.append(list(r))

y=list(y)

print("You can apply for the following Job Profiles :")
for i in range(len(y)):
  print(i+1," - ",y[i][0])

print("**************************************************")
print("But you need to work on these skills:")
more = []
j=[]
for u in range(len(y)):
  j = df1[df1.jobtitle==y[u][0]].skill_s
  f = set(j)
  more.append(list(f))

w=[]
w = test.split(" ")
new_skill =[]
for i in range(len(y)):
  x =[]
  x=more[i][0].split(" ")
  new_skill.append([item for item in x if item not in w])

for i in range(len(y)):
  print('You need to develop these skills to improve your profile for ',y[i][0]," :",new_skill[i])



ind = "IT-Software "                   #user input industry 
#jobs = [] 
#for i in range(10):
s=list((df1[df1.industry==ind].jobtitle))
#d = list(jobs)
s=set(s)
s = list(s)
print("The Job profiles available in the industry of your interest: ") 
for i in range(len(s)):
  print(s[i])
print("Which job you are interested in? ")

jobb = "Java Developer"   #user selected job
sk=[]

sk=list((df1[df1.jobtitle==jobb].skill_s))
sk = set(sk)
sk=list(sk)
sk="".join(sk)
print('We recommend you to develop the following skills according to the job you selected:')
print(sk)

#recommended skills
str_rc=sk
str_us=test
sm=get_jaccard_sim(str_rc,str_us)
print(sm)
if sm==0.0:
  print("We recommend you to develop the mentioned skills")
else:
  print("You have developed ",sm*100," % of the required skills. We advise you to develop the skills mentioned.")

df1.head()

df1.to_csv('Database_2.csv')

