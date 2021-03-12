# https://leetcode.com/problems/reorder-data-in-log-files

'''
    Algorithm: Custom Sorting
    - Use key function tuple
    Time: 
        -sorting takes NlogN time
        -Comparing two string takes takes the length of the strings themselves
        O(M * NlogN), M = max length of a single log, N = # of logs
    Space: (N)
'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digLogs = []
        letLogs = []
        # separate digit and letter logs
        for log in logs:
            splitLog = log.split(' ', maxsplit=1)
            if splitLog[1][0].isdigit():
                digLogs.append(log)
            else:
                letLogs.append(splitLog)
        # sort letter logs by content, then by identifier
        letLogs.sort(key=lambda x: (x[1], x[0]))
        # turn letter logs back to original 
        ans = [" ".join(log) for log in letLogs]
        # append digit logs after letter logs
        ans.extend(digLogs)
        return ans