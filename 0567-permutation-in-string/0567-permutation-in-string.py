class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
         n=len(s1)
         m=len(s2)

         if n>m:
            return False
         s1_count=Counter(s1)
         window=Counter(s2[:n])
         if window==s1_count:
            return True
         for i in range(n,m):
            window[s2[i]]+=1 
            window[s2[i-n]]-=1
            if window[s2[i-n]]==0:
                del window[s2[i-n]]
            if window == s1_count:
                return True
         return False
