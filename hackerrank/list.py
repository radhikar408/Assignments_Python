#--------------ques-list------------------
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0
# ----output----
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]
# n=int(input())
# li=[]
# li.insert(0,5)
# li.insert(1,10)
# li.insert(0,6)
# print(li)
# li.remove(6)
# li.append(9)
# li.append(1)
# li.sort()
# print(li)
# li.pop()
# li.reverse()
# print(li)
#           -------ques-tuples-------
# n = int(input())
# integer_list = map(int, input().split())
# print(tuple(integer_list))
# print(hash(tuple(integer_list)))
li=[]
# n=int(input())
for _ in range(int(input())):
        name = input()
        score = float(input())
        li.append(name)
        li.append(score)
        print(li)
# for i in range(n):
#     for j in range(n):
#         name = input()
#         score = float(input())
#         li.append([i][j
# print(li)
