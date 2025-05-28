num = [ 10,58,26,25,42,36,45,78,78,89,100 ]
print("Original list:", num)

print(num[0:3])  # First three elements
print(num[-2: ]) # Last two elements
print('Reserve Number', num[::-1]) # elements in reverse order)  

num[1]= 999 # Change the second element
print("After changing second element:", num)

num.append(200) # Add a new element at the end
print("After appending 200:", num)
num.insert(4, 300) # Insert 300 at index 4
print("After inserting 300 at index 4:", num)
num.pop(3) # Remove the element at index 4  
print("After popping index 4:", num)






print("Sum of all elements:", sum(num)) # Sum of all elements
print("Maximum element:", max(num)) # Maximum element
print("Minimum element:", min(num)) # Minimum element
print("Length of the list:", len(num)) # Length of the list
print("Sorted list:", sorted(num)) # Sorted list
print("Reversed list:", list(reversed(num))) # Reversed list


#Sum Formula 

max_num = num[0]
for i in num:
    if max_num < i:
        max_num = i
print("Maximum element using loop:", max_num)


min_num = num[0]
for i in num:
    if min_num > i:
        min_num = i 
print("Minimum element using loop:", min_num)

sum_num = 0
for i in num:
    sum_num += i
print("Sum of all elements using loop:", sum_num)
    



even_num = []

for i in num:
    if i%2 ==0:
        even_num.append(i)
print("Even numbers in the list:", even_num)

odd_num = []
for i in num:
    if i%2 !=0:
        odd_num.append(i)       
print("Odd numbers in the list:", odd_num)

dict = {}
for i in num:
    dict[i] = num.count(i)          
print("Count of each element in the list:", dict)



odd_num = []
for i in num:
    if i % 2 != 0:
        result = i**2
        odd_num.append(result)
print("Square of odd numbers in the list:", odd_num)

dup_num = []
for i in num:
    if num.count(i) > 1 and i not in dup_num:
        dup_num.append(i)
print("Duplicate numbers in the list:", dup_num)



# List Comprehensions




