class Solution:
    # solve 1
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        alpha_logs = []
        digit_logs = []
        for log in logs:
            digit = False
            for elem in log.split()[1:]:
                if elem.isdigit():
                    digit = True
            if digit:
                digit_logs.append(log)
            else:
                alpha_logs.append(log)
        alpha_logs.sort(key = lambda x:(x.split()[1:], x.split()[0]))
        return alpha_logs + digit_logs

solution = Solution()
solution.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])

"""
Input 
["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output 
["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
"""