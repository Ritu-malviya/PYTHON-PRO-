#WAP to create a list taking input from users
lst = []
  
n = int(input("Enter number of elements : "))
  
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele) # adding the element
      
print(lst)
