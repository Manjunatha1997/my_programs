# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [2,7,11,15]
target = 9

def addTwoSum(nums,target):

	for i in range(len(nums)-1):
		for j in range(i,len(nums)-1):
			if target == nums[i] + nums[j+1]:
				return i,j+1


res = addTwoSum(nums,target)
print(res)



