num_list=[1,4,5,9,7,10,8]
print("Original list:",num_list)

count=0

for i in num_list:
    print("The value of i is",i)
    count+=i
    avg=count/len(num_list)
    print("Sum =",count)
    print("Average=",avg)

num_list.sort()
print("Ater sorting",num_list)

#Function to check weather the 1st and lat chararacter of words match

def match_words(words):
 ctr=0
 list_of_words=[]
    
 for word in words:
    if len(word)>1 and word[0]==word[-1]:
     ctr+=1
     list_of_words.append(word)
 print("List of word with the first and last character is same:",list_of_words) 
 return ctr

count=match_words(['abc','cbf','ghg','jkl','mno','aba'])

