class Solution(object):
    def __init__ (self, array, queries):
        self.array = array
        self.queries = queries
    
    def solution(self):
        for i in range (len(self.queries)):
            col1 = self.queries[i][0]
            col2 = self.queries[i][1]
            for j in range (col1, col2+1):
                self.array[j] += 1

        return self.array
    

array = [0,1,2,3,4]
queries = [[0,1], [1,2], [2,3]]

result = Solution(array, queries)

print(result.solution())