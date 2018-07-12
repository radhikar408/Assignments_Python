# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()

                #split()method
# text="geeks for geeks"
# print(text.split())
# word="radhika@dua@diksha"
# print(word.split('@'))
# word="catbatrat"
# print([word[i:i+3] for i in range(0, len(word), 3)])


                #map()method
# def addition(n):
#     return(n+n)
# numbers=(1,2,3,4,5)
# result=map(addition,numbers)
# print(list(result))
#map lambda
# numbers = (1, 2, 3, 4)
# result=map(lambda x:x+x,numbers)
#print(list(result))
# Add two lists using map and lambda

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]

# result = map(lambda x, y: x + x, numbers1, numbers2)
# print(list(result))

# List of strings
# l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
# test = list(map(list, l))
# print(test)
n = int(input())
arr = map(int, input().split())
li=[]
#print(li)
#li.sort()
#print(li)
for i in arr:
    li.append(i)
## for i in range(1,len(li)):
#     c=li[0]
#     if(c==li[i]):
#         print(i+1)

    #li.remove(min(li))

# li.remove(min(li))
#     c=li[0]
#     #print(c)
#     if(c==[i]):
#         li.remove([i])
#print(li)
a=max(li)
while(max(li)==a):
    li.remove(max(li))
print(max(li))

#list(arr).remove(max(list(arr)))
# list1=(list(arr))
# print(list1)
# list1.sort()
# list1.reverse()
# print(list1)
# c=list1[0]
# for i in range(1,len(list1)):
#     if(i==c):
#         list1.remove(c)
# print(list1)
# great=0
# great2=0
# for i in arr:
#     if i>great:
#         great2=great
#         great=i
#     elif i>great2 and i!=great:
#         great2=i
# print(great)
# print(great2)

