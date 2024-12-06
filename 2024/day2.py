#test cases
# lines = [[1,2,3,4,5],
#          [8,6,5,4],
#          [1,5,9]]
# lines = [[51, 52, 55, 58, 60, 61, 62, 61],
            #  [64, 65, 67, 70, 72, 74, 77, 77]]

with open("day2_input.txt") as f:
    lines = f.readlines()
lines = [[int(line) for line in line.split()] for line in lines]
         
increasing_condition = lambda x: all(later > earlier for earlier, later in zip(x, x[1:]))
decreasing_condition = lambda x: all(earlier > later for earlier, later in zip(x, x[1:]))
lte_3_difference = lambda x: all(abs(later - earlier) <= 3 for earlier, later in zip(x, x[1:]))   
def is_true(line):
    return (increasing_condition(line) or decreasing_condition(line)) and lte_3_difference(line)

#check if removing each entry one by one makes the condition solvable, but also check if it works on its own
#to check use list[:idx] + list[idx+1:] <- this will remove the element at idx 
def dampening(line):
    if is_true(line):
        return True
    for idx in range(len(line)):
        if is_true(line[:idx] + line[idx+1:]):
            return True
prob1 = 0

for line in lines:
    #Problem 1 
    if is_true(line):
        prob1 +=1
print("Prob1: ",prob1)

#problem 2 - dampener
sum_prob2 = 0 
for line in lines:
    if dampening(line):
        sum_prob2+=1 
print("Prob 2: ", sum_prob2)
        
        
