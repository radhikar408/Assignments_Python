# Q.1- Create a database. Create the following tables:
# 1. Book
# 2. Titles
# 3. Publishers
# 4. Zipcodes
# 5. AuthorsTitles
# 6. Authors

# ans.1
import pymysql
db=pymysql.connect("localhost","root","khushbukhushi","demo")
cursor=db.cursor()
cursor.execute("create table books(Userid int ,Titleid int,Location char(100),Genre int(20) ")
cursor.execute("create table titles(title int,title_id int,ISBN int,publisher_id int,publication_id int)")
cursor.execute("create table publishers(publisherid int,Name char,Street_Address char,Suitenumber int ,ZidCodeId int)")
cursor.execute("create table Zip_Codes(zip_code_id int,City char,State char,Zip_code int)")
cursor.execute("create table Authors_Titles(Author_Title_id int,Author_id int,Title_Id int)")
cursor.execute("create table Authors(Author_id int,First_Name char,Mode_Name char,Last_name char)")


