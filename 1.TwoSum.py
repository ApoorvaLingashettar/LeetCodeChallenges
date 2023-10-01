# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


input_array = [3,2,3]
target = 5

result = []
for i in range(len(input_array)):
    for j in range(len(input_array)):
        if input_array[i] + input_array[j] == target:
            if i != j:

                result.append(i)
                result.append(j)

print(result)





