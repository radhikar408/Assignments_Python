#update


db=pymysql.connect('localhost','root','khushbukhushi','demo')
cursor=db.cursor()
q1="select * from titles"
q2="update titles set titles = 'python' where titleid="567"
cursor.execute(q1)
print(cursor.fetchall())
try:
    crsor.execute(q2)
    db.commit()
except:
    db.rollback()
cursor.execute(q1)

db.close()
