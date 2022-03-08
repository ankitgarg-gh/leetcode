class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        from itertools import permutations

        perms = permutations(arr)

        valid_perms = set()
        for perm in perms:
            if perm[2] <= 5:
                if perm[0] == 2 and perm[1] <= 3:
                    valid_perms.add(perm)
                elif perm[0] <= 1:
                    valid_perms.add(perm)

        if len(valid_perms) == 0:
            return ''

        valid_perms = list(valid_perms)

        maxTime = valid_perms[0]
        for valid_perm in valid_perms[1:]:
            if valid_perm[0] > maxTime[0]:
                maxTime = valid_perm
            elif valid_perm[0] == maxTime[0]:
                if valid_perm[1] > maxTime[1]:
                    maxTime = valid_perm
                elif valid_perm[1] == maxTime[1]:
                    if valid_perm[2] > maxTime[2]:
                        maxTime = valid_perm
                    elif valid_perm[2] == maxTime[2]:
                        if valid_perm[3] > maxTime[3]:
                            maxTime = valid_perm
        return '{}{}:{}{}'.format(maxTime[0], maxTime[1], maxTime[2], maxTime[3])


print(Solution().largestTimeFromDigits([1, 2, 3, 4]))
print(Solution().largestTimeFromDigits([0, 0, 0, 0]))
print(Solution().largestTimeFromDigits([0, 0, 0, 6]))
print(Solution().largestTimeFromDigits([6, 6, 6, 6]))
print(Solution().largestTimeFromDigits([4, 3, 2, 1]))
print(Solution().largestTimeFromDigits([0, 0, 1, 0]))
print(Solution().largestTimeFromDigits([9, 0, 7, 7]))
print(Solution().largestTimeFromDigits([2, 0, 6, 6]))
