# array_string = input('Enter array :')
array_string = '[1,-2,3,-4,0,-10]'


# array_number = []
# for ch in array_temp:
#     array_number.append(int(ch))

# Shorter method using list comprehension

array_temp = array_string.replace('[', '').replace(']', '').split(',')

array_number = [int(ch) for ch in array_temp]

print(f'string array = {array_string}', type(array_string))
print(f'temp string array = {array_temp}', type(array_temp))
print(f'number array = {array_number}')

# add comment