class Solution:
  def isPalindrome(self, s: str) -> bool:
    s=s.lower()
    a=""
    for i in s:
        if i.isalnum():
            a+=i
    ptr1,ptr2=0,len(a)-1
    while ptr1<ptr2:
        if a[ptr1]==a[ptr2]:
            ptr1+=1
            ptr2-=1
        else:
            return False
    return True

sol=Solution()
s=input()
print(sol.isPalindrome(s))
