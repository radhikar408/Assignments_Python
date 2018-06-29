# Q.1- Extract the user id, domain name and suffix from the following email addresses. 
# emails = "zuck26@facebook.com" "page33@google.com"
# "jeff42@amazon.com"
# desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]
import re
# a="zuck26@facebook.com" 
# b="page33@google.com" 
# c="jeff42@amazon.com"
# p=re.compile(r"([a-zA-Z0-9]+)@([a-zA-Z]+).([a-zA-z]+)")
	
# def show(email):
	# res=p.match(email)
	# print(res)
	# print(res.group(1))
	# print(res.group(2))
	# print(res.group(3))
# show(a)
# show(b)
# show(c)
a="zuck26@facebook.com" 
b="page33@google.com" 
c="jeff42@amazon.com"
print(re.findall(r'(.+)@(.+)\.(.+)',a),end="")
print(re.findall(r'(.+)@(.+)\.(.+)',b),end="")
print(re.findall(r'(.+)@(.+)\.(.+)',c),end="")