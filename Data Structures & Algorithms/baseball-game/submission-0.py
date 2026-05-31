class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        records = []
        n = len(operations)

        for i in range(n):
            m = len(records)
            curr = operations[i]
            if curr == "+":
                records.append(records[-1] + records[m - 2])
            elif curr == "C":
                total = total - records[-1]
                records.pop()
                continue
            elif curr == "D":
                records.append(2 * records[-1])
            else:
                records.append(int(curr))

            total += records[-1]
        
        return total
