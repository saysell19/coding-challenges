# A program that outputs "fizz", "buzz" or "fizzbuzz" depending on the number and conditions
 
class Solution:

	def run(self, N, M):
		#
		# Write your code below; return type and arguments should be according to the problem\'s requirements
		#
		sequence = ""
		for i in range(N, M+1):
			if i % 3 == 0 and i % 5 == 0:
				sequence += "FizzBuzz,"
			elif i % 3 == 0:
				sequence += "Fizz,"
			elif i % 5 == 0:
				sequence += "Buzz,"
			else:
				sequence += str(i) + ","
		return sequence[:len(sequence)-1]

# test_run = Solution()
# print(test_run.run(1, 15))
