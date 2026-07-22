test_dict={
       'Codingal':2,
       'is':2,
        'best':2,
        'for' :2,
         'coding':1
}
 # printing original dictionry
print("the origina ldictionry"+ str(test_dict))


k=2
#Using loop , I want selective key values in dictionary

res=0
for key in test_dict:
      if test_dict[key]==k:
         res=res+1

print("gdcghd"+str(res))