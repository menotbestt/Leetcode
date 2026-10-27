class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack =[]
        ins = set()
        c = Counter(s)
        for i in s:
            c[i] -= 1
            if i in ins:
                continue
            while stack and stack[-1] > i and c[stack[-1]]:
                ins.remove(stack.pop())
            
            stack.append(i)
            ins.add(i)
        return ''.join(stack)