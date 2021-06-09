class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folders = []
        for log in logs:
            if log == '../':
                if folders:
                    folders.pop()
            elif log != './':
                folders.append(log)
        return len(folders)
