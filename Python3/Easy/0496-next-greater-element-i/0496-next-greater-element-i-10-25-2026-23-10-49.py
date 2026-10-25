class Solution:
    def nextGreaterElement(self, k: list[int], n: list[int]) -> list[int]:
        t = {}
        s=[0]
        for i in range(1,len(n)):
            while s and n[s[-1]] < n[i]:
                t[n[s[-1]]] = n[i]
                s.pop()
            s.append(i)
        return [t[i] if i in t else -1 for i in k ]
