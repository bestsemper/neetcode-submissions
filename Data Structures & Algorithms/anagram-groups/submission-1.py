class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}
        groups = []
        alpha = {}
        for i, c in enumerate("abcdefghijklmnopqrstuvwxyz"):
            alpha[c] = i
        for s in strs:
            key = getKey(s, alpha)
            print(s, key)
            if key in keys:
                groups[keys[key]].append(s)
            else:
                groups.append([s])
                keys[key] = len(groups) - 1
        return groups


def getKey(s, alpha):
    key = [0] * 26
    for c in s:
        key[alpha[c]] += 1
    return str(key)