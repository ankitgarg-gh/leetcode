'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.generate(n,'o')

    def generate(self,n,type):
        if n==0:
            # print(")")
            return
        print("(")
        self.generate(n-1)
        print(")")



input = [3,1,2,4]
for i in input:
    print(Solution().generate(i))