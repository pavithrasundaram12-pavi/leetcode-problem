class Solution(object):
    def digitSum(self, s, k):
        def add(a):
            i=0
            for x in a:
                i+=int(x)
            return str(i)
        def check(s,k):
            if len(s)<=k:
                return s
            p=""
            a=""
            for x in s:
                if len(a+x)>k:
                    p+=add(a)
                    a=""
                a+=x
            if len(a)>0: p+=add(a)
            return check(p,k)
        return check(s,k)                       
     