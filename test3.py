class Solution(object):
    def __init__(self, number):
        self.number = number


    def solution(self):
        if self.number < 0: 
            return 0
        
        sum = 0
        string = str(self.number)

        for i in range(len(string)):
            sum += int(string[i])
    
        return sum

number = 1234

result = Solution(number)
print(result.solution())