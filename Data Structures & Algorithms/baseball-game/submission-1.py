class Solution:
    def calPoints(self, operations: List[str]) -> int:

        record, total = [], 0

        for op in operations:
            if  op == "+":
                record.append(record[-1] + record[-2])
            elif op == "C":
                total = total - record[-1]
                record.pop()
                continue
            elif op == "D":
                record.append(2 * record[-1])
            else:
                record.append(int(op))

            total += record[-1]
        
        return total
