class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "/" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        num = 0
        while len(s) > 0:
            idx = s.index("/")
            num = int(s[:idx])
            decoded.append(s[idx+1:idx+1+num])
            s = s[idx+1+num:]
        return decoded