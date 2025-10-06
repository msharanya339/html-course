my_dict = {1: "apple", 2: "ball", 'name': "john", 'marks': [60, 55, 55]}
		   
print("Marks :", my_dict['marks'])
my_dict['isStudent'] = False #Update value
print(my_dict)

my_dict['grade'] = 7 #Add value
print(my_dict)

my_dict.pop('marks')
print(my_dict)

my_dict.clear()
print(my_dict)
