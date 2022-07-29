class Solution:
   def solve(self, s, k):
      while True:
         count = 0
         chars = set(s)
         for c in chars:
            if c * k in s:
               s = s.replace(c * k, "")
               count += 1
         if count == 0:
            break
      return s

ob = Solution()
s = "paaappmmmma"
k = 3
print(ob.solve(s, k))
