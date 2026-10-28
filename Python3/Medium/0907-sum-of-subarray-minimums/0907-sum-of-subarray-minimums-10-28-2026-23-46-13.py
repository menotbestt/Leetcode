class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9+7
        st = []
        res = 0
        for r in range(len(arr)):
            while st and arr[st[-1]] >= arr[r]:
                top = st.pop()
                l = st[-1] if st else -1
                res += (top-l)*(r-top)*arr[top]
                res %= MOD
            st.append(r)
        r=len(arr)
        while st:
            top = st.pop()
            l = st[-1] if st else -1
            res += (top-l)*(r-top)*arr[top]
            res %= MOD
        return res
