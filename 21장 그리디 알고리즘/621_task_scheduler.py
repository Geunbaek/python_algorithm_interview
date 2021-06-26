from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter = Counter(tasks)
        result = 0

        while True:
            sub_count = 0

            for task, _ in counter.most_common(n+1):
                sub_count += 1
                result += 1
                print(counter)
                counter.subtract(task)
                print(counter)
                counter += Counter()
                print(counter)
            if not counter:
                break

            result += n - sub_count + 1
        return result




sol = Solution()
print(sol.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))

"""
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
"""
