def sum_digit(nums):
  end = []
  for i in range(len(nums)):
    total = 0
    while nums[i] // 10 != 0:
      total += nums[i] % 10
      nums[i] = nums[i] // 10
    total += nums[i]
    if total % 2 == 0:
      end.append(True)
    else:
      end.append(False)
  return end
    
print(sum_digit([123, 456, 789]))
print(sum_digit([321, 654, 987]))