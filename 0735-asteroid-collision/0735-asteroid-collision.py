class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for val in asteroids:
            if val>0:
                st.append(val)
            else:
                while len(st)>0 and abs(val)>st[-1] and st[-1]>0:
                    st.pop()
                if len(st)==0 or st[-1]<0:
                    st.append(val)
                if len(st)>0 and st[-1]==abs(val):
                    st.pop()
        return st