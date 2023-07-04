# A program that outputs the xth smallest number from an unordered list

class XthInOrder:
  def __init__(self, x, nums):
    self.x = x
    self.nums = nums
  
  def getX(self):
    if self.x > len(self.nums) or len(self.nums) == 0:
      return 0
    else:
      sorted_nums = sorted(self.nums)
      print(sorted_nums)
      return sorted_nums[self.x-1]
  
  def __str__(self):
    return str(self.getX())

# xth = XthInOrder(2, [-13, 41, -31, -23, -1, 1, -29, 26, 31, -26, 26, 37, 25, -36, 7, -21, 23, -1, 37, -6])
# print(xth)