# String and numbers
print(str(50)) # "50"

# print("Today is the " + 23) # TypeError: can only concatenate str (not "int") to str
print("Today is the " + str(23)) # Today is the 23


print(type(str(30))) # <class 'str'>
print(type(int("30"))) # <class 'int'>
print(float("3.14")) # 3.14
print(type(float("3.14"))) # <class 'float'>


greeting="Hello"
greeting_list=list(greeting)
print(greeting_list) # ['H', 'e', 'l', 'l', 'o']
print(",".join(greeting_list)) # print(",".join(list(greeting))) # H,e,l,l,o
print("".join(greeting_list)) # Hello

csv_row="the,quick,brown,fox"
csv_row_split=csv_row.split(",")


names=["Simon", "Arya", "Ramon", "Magola", "Arya"]
print(set(names)) # {'Arya', 'Magola', 'Ramon', 'Simon'}
print(sorted(set(names))) # ['Arya', 'Magola', 'Ramon', 'Simon']









