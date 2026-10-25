class Solution:
    def dailyTemperatures(self, t: list[int]) -> list[int]:
        st=[0]
        res = [0]*len(t)
        for i in range(1,len(t)):
            temp = []
            while st and t[st[-1]] < t[i]:
                res[st[-1]] = i-st[-1]

                st.pop()

            st.append(i)
        return res