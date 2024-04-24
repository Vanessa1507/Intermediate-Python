# CONVERTING BETWEEN TYPES
my_data="this,is,a,coma,separated,string"
print(my_data.split(",")) # ['this', 'is', 'a', 'coma', 'separated', 'string']

student="Mary,8,Math"
print(student.split(",")) # ['Mary', '8', 'Math']

name, age, subject = student.split(",")
print(name) # Mary

my_list = my_data.split(",")
print(my_list) # ['this', 'is', 'a', 'coma', 'separated', 'string']

print(", ".join(my_list)) # this, is, a, coma, separated, string

print(int("5")) # 5
print(float("4.0")) # 4.0