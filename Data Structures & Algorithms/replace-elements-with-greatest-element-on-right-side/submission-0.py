class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        res[n-1] = -1

        rightMax = arr[n - 1]

        for i in range(n - 1, 0, -1):
            if arr[i] > rightMax:
                rightMax = arr[i]
            res[i - 1] = rightMax

        return res



        