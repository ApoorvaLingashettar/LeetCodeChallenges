s_input_string = "Let's take LeetCode contest"

s_list = s_input_string.split(' ')

reversed_string = []
for word in s_list:
    reversed_string.append(word[::-1])

_reversed_string = reversed_string[0]

for i in range(1, len(reversed_string)):
    _reversed_string += " " + reversed_string[i]

print(s_input_string)
print(_reversed_string)





