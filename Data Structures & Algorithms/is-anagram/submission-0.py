class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_table = {}
        for c in s:
            if c in s_table:
                s_table[c] += 1
            else:
                s_table[c] = 1
        t_table = {}
        for c in t:
            if c in t_table:
                t_table[c] += 1
            else:
                t_table[c] = 1
        return s_table == t_table