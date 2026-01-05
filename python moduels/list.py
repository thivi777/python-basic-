#method 1 create a list
lis=["one","two","three","four","five"]
lis1=["six","seven","eight"]
print(lis+lis1)
print(lis[3])

#method 2 create a list
number_list=list((1,2,3,4,5,6,7,8,9))
print(number_list)
print(type(number_list))
print(number_list[1:3]) #1-3 index elements slice and show
print(number_list[2:])
print(len(number_list))

#method 1 append
num_List=[1,2,3,4,5]
num_List.append(10)
print(num_List)

#method 2 extend
number=[20,30]
num_List.extend(number)
print(num_List)
num_List.append(number)
print(num_List)

#method_3 insert
# num_List.insert(2,15)
# print(num_List)