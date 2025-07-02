class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 2:
            return "".join(strs)

        length = len(strs[0])
        for i in range(len(strs)):
            length = min(length, len(strs[i]))

        res = []

        for i in range(length):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j+1][i]:
                    return "".join(res)
            res.append(strs[0][i])
        return "".join(res)