from string import ascii_uppercase
class Solution:
    def numDecodings(self, s: str) -> int:
        table = {}
        for val, letter in enumerate(ascii_lowercase, start=1):
            table[val] = letter
        print(table)
        return 0