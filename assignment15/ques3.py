# Q.3- Split the following irregular sentence into words 
# sentence = "A, very very; irregular_sentence"
# desired_output = "A very very irregular sentence"
import re
sentence = "A, very very; irregular_sentence"
p=re.sub(r"[^a-zA-Z]"," ",sentence)
print(p)
print("\n")
