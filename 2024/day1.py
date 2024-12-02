with open("day1_input.txt") as f:
    lines = f.readlines()
list1 = []
list2 = [] 
for line in lines:
    list1.append(int(line.split(" ")[0]))  
    list2.append(int(line.split(" ")[-1].replace("\n","")))

list1.sort(), list2.sort()

#distance between lists  -- problem 1
sum_list = [abs(list1[i] - list2[i]) for i in range(len(list1))]
print("The distance between lists is: ",sum(sum_list))


#similarity Score  -- problem 2
similarity_list = [] 

#create dictionary of list2 number of appearances, 1 appears 3 times, 4  2 times.. {1:3, 4:2}
#loop list1 and look for the keys and append the value if found
dict_count = {list2[i]:list2.count(list2[i]) for i in range(len(list2))}
similarity_score = 0
for i in range(len(list1)):
    similarity_score += (dict_count.get(list1[i], 0) * list1[i])

print("The similarity score is: ",similarity_score)