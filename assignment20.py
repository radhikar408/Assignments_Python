#Ques1-
import pandas as p
# data=[['xyz',23,'radhikar408@gmail.com',839374292728]]
# frame1=p.DataFrame(data,columns=('Name','age','Email','Phonenumber'))
#
# frame2=p.DataFrame([ ['abc',24,'jshdyek@gmail.com',7282839333]],columns=('Name','age','Email','Phonenumber'))
# frame1=frame1.append(frame2)
# print(frame1)
#Ques2-
df=p.read_csv("weather.csv")
print(df.head(5))
print(df.head(10))
print(df.describe())
print(df.tail(5))
print(df["MinTemp"].describe())