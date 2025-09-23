# Two pointers Algorithm

numss = [-7, -2, 0,  1, 4, 10]
nums=[]
left = 0
right = len(numss) - 1
result = []

for num in numss:
    nums.append(num ** 2)


while left <= right:
    if nums[left] > nums[right]:
        result.append(nums[left])
        left += 1
    else:
        result.append(nums[right])
        right -= 1

result.reverse()
print(result)