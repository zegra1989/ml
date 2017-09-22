# -*- coding:utf-8 -*- 

# 使用 UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import numpy
import pandas
'''
In this exercise, we will perform some rudimentary practices similar to those of
an actual data scientist.

Part of a data scientist's job is to use her or his intuition and insight to
write algorithms and heuristics. A data scientist also creates mathematical models 
to make predictions based on some attributes from the data that they are examining.

We would like for you to take your knowledge and intuition about the Titanic
and its passengers' attributes to predict whether or not the passengers survived
or perished. You can read more about the Titanic and specifics about this dataset at:
http://en.wikipedia.org/wiki/RMS_Titanic
http://www.kaggle.com/c/titanic-gettingStarted
    
In this exercise and the following ones, you are given a list of Titantic passengers
and their associated information. More information about the data can be seen at the 
link below:
http://www.kaggle.com/c/titanic-gettingStarted/data. 

For this exercise, you need to write a simple heuristic that will use
the passengers' gender to predict if that person survived the Titanic disaster.

You prediction should be 78% accurate or higher.
    
Here's a simple heuristic to start off:
   1) If the passenger is female, your heuristic should assume that the
   passenger survived.
   2) If the passenger is male, you heuristic should
   assume that the passenger did not survive.

You can access the gender of a passenger via passenger['Sex'].
If the passenger is male, passenger['Sex'] will return a string "male".
If the passenger is female, passenger['Sex'] will return a string "female".

Write your prediction back into the "predictions" dictionary. The
key of the dictionary should be the passenger's id (which can be accessed
via passenger["PassengerId"]) and the associated value should be 1 if the
passenger survied or 0 otherwise.

For example, if a passenger is predicted to have survived:
passenger_id = passenger['PassengerId']
predictions[passenger_id] = 1

And if a passenger is predicted to have perished in the disaster:
passenger_id = passenger['PassengerId']
predictions[passenger_id] = 0

You can also look at the Titantic data that you will be working with
at the link below:
https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/titanic_data.csv
'''

"""
Pclass-船舱等级
Sex-性别
Age-年龄
Parch-携带直系家属数量
SibSp-携带非直系家属数量
Ticket-船票号码
Fare-船票价格
Cabin-船舱号
Embarked-登船港口
"""

predictions = {}
df = pandas.read_csv("src/titanic_data.csv")

# print df["Sex"].map(lambda x: x=="female")

f_survived = df[(df.Sex == "female") & (df.Survived == 1)]
f_perished = df[(df.Sex == "female") & (df.Survived == 0)]

m_survived = df[(df.Sex == "male") & (df.Survived == 1)]
m_perished = df[(df.Sex == "male") & (df.Survived == 0)]

f_survived_count = f_survived.Survived.count()
f_perished_count = f_perished.Survived.count()

m_survived_count = m_survived.Survived.count()
m_perished_count = m_perished.Survived.count()

print "Female survived rate:", float(f_survived_count)/float(f_survived_count+f_perished_count)
print "Male survived rate:", float(m_survived_count)/float(m_survived_count+m_perished_count)

print "Female survived avg age:", f_survived.Age.mean()
print "Female perished avg age:", f_perished.Age.mean()

print "Male survived avg age:", m_survived.Age.mean()
print "Male perished avg age:", m_perished.Age.mean()

c1_survived = df[(df.Pclass == 1) & (df.Survived == 1)]
c1_perished = df[(df.Pclass == 1) & (df.Survived == 0)]

print "1st Class survived rate:", float(c1_survived.Survived.count())/float(c1_survived.Survived.count()+c1_perished.Survived.count())

c2_survived = df[(df.Pclass == 2) & (df.Survived == 1)]
c2_perished = df[(df.Pclass == 2) & (df.Survived == 0)]

print "2nd Class survived rate:", float(c2_survived.Survived.count())/float(c2_survived.Survived.count()+c2_perished.Survived.count())

c3_survived = df[(df.Pclass == 3) & (df.Survived == 1)]
c3_perished = df[(df.Pclass == 3) & (df.Survived == 0)]

print "3rd Class survived rate:", float(c3_survived.Survived.count())/float(c3_survived.Survived.count()+c3_perished.Survived.count())

def func(x):
	survived = df[x & (df.Survived == 1)].Survived.count()
	perished = df[x & (df.Survived == 0)].Survived.count()

	print df[x & (df.Survived == 1)]
	return float(survived)/(survived+perished)

print "====="
# print func((df.Pclass == 1) & (df.Age < 18))
# print func((df.Fare > 270))

# print func((df.Sex == "female") & (df.SibSp < 2) & (df.Parch < 2))
print func((df.Sex == "female"))




# print df[(df.Pclass == 1)]

# print df.Parch

# print 
# print df[(df.Pclass == 1) & (df.Survived == 0)]
# print f_perished.Pclass.mean()

# print df.sum(df["Sex"] == "female")