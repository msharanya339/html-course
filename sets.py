my_set = {1,2,2,3,3,4,4}
print(my_set)

my_set.add(5)
print(my_set)

my_set2 = {2,4,5,6}

print("difference: ",my_set.difference(my_set2)) #(1,3,5,6)
print("symmetric difference: ",my_set.symmetric_difference(my_set2)) #(1,3,5,6)

set1 = {"grenen","blue"}
set2 = {"blue","red"}
print("Union: ",set1.union(set2) )
print("intersection:",set1.intersection(set2))