class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9+7
        st = []
        res = 0
        for r in range(len(arr)):
            while st and arr[st[-1]] >= arr[r]:
                top = st.pop()
                l = st[-1] if st else -1

                #We used formula (mid - L) x (R - mid) to work out the total number of subarrays between the 2
                res += (top-l)*(r-top)*arr[top] 
                res %= MOD
            st.append(r)
        
        r = len(arr)
        #We need to treat the items that are left in the stack which its right boundary will always be len(arr)
        while st:
            top = st.pop()
            l = st[-1] if st else -1
            res += (top-l)*(r-top)*arr[top]
            res %= MOD
        return res
