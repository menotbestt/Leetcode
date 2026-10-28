class Solution:
    def trap(self, h: list[int]) -> int:
        stack = []
        rs = 0
        for right in range(len(h)):
            while stack and h[stack[-1]] < h[right]:
                mid = stack.pop()

                if stack:
                    left = stack[-1]
                    rs += (min(h[left], h[right]) - h[mid]) * (right-left-1)

            stack.append(right)
        return rs