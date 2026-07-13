class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        
        # dp[i][j] = True if s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # empty string matches empty pattern
        
        # Handle patterns like a*, a*b*, a*b*c* matching empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Option 1: zero occurrences of the preceding element
                    dp[i][j] = dp[i][j - 2]
                    # Option 2: one or more occurrences, if it matches current char
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                # else: dp[i][j] stays False (no match)
        
        return dp[m][n]