class Solution:
    def sumAndMultiply(self, n):
        digits = [d for d in str(n) if d != '0']
        if digits:
            x = int(''.join(digits))
        else:
            x = 0
        total = 0
        for d in digits:
            total = total + int(d)
        return x * total