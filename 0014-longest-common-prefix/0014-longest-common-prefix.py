class Solution(object):
    def longestCommonPrefix(self, strs):
        Prefix=strs[0]
        for word in strs:
            while not word.startswith(Prefix):
                Prefix=Prefix[:-1]
        return Prefix    
        