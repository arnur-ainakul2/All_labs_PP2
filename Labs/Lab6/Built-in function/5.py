my_list=[]
n=int(input())
for i in range(n):
    my_bool=bool(input())
    my_list.append(my_bool)
my_tuple=tuple(my_list)
x=all(my_tuple)
print(x)