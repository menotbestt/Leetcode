class Solution:
    def smallestSubsequence(self, s: str) -> str:
        c= Counter(s)
        seen = set()
        st = []
        for i in s:
            c[i] -= 1
            if i in seen:
                continue
            while st and st[-1] > i and c[st[-1]]:
                seen.remove(st.pop())

            st.append(i)
            seen.add(i)
        return ''.join(st)