# A program that outputs the number that is not duplicated in a list of numbers

class Solution:

    def run(self, student_list):
        try:
            single_student_number = None
            student_list.sort()
            # print(f"DEBUG LST: {student_list}")

            single_student_number = [student_number for student_number in student_list if student_list.count(student_number) == 1]
            # output single_student_number as a str

            return str(single_student_number[0])
        except IndexError:
            return "The list was empty! Please try again."
    

test_run = Solution()
print(test_run.run([1, 2, 3, 4, 5, 1, 2, 3, 4]))
