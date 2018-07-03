#2--insert values in table

import pymysql
db=pymysql.connect("localhost","root","khushbukhushi","demo")
cursor=db.cursor()
cursor.execute("insert into books values("Alchemist",130448,"Ambala","chemist")"):
cursor.execute("insert into titles values("java",567,24567,23,12344)")
cursor.execute("insert into publishers values(122,"balagurusamy","bombay",1244,134007)")
cursor.execute("insert into  Zip_Codes values(123,"Ambala","haryana",86748)")
cursor.execute("insert into Authors_Titles values(123,6316654,123345)")
cursor.execute("insert into Authors values(133,"radhika","None","Dua")")
