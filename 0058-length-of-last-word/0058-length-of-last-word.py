class Solution(object):
    def lengthOfLastWord(self, s):
        st=s.strip().split()
        return len(st[-1]) if st else 0
        