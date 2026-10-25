class Solution:
    def largestRectangleArea(self, h: list[int]) -> int:
        s = [0]
        m = 0
        h.append(0) #To ensure all items pop from stack
        
        for i in range(1,len(h)):
            while s and h[s[-1]] > h[i]:
                top = s.pop() #Pop first to calc the area with this bar to be the height
                # The new top stack is the first bar that is shorter than h[top]
                wid = i-s[-1]-1 if s else i #If stack is empty meaning h[top] is the shortest and thus reaches all the way left to idx 0
                m = max(m, h[top] * wid) # Calc area with h[top] being height      
            
            s.append(i)
        return m