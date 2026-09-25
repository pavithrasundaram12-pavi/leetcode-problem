class Solution(object):
    def braceExpansionII(self, expression):
        def concat_words(stack, delimiters):
            words = set([''])
            while stack and stack[-1] not in delimiters:
                ws1 = stack.pop()
                if type(ws1) is not set:
                    ws1 = set([ws1])
                cur_words = set()
                for w1 in ws1:
                    for w2 in words:
                        cur_words.add(w1 + w2)
                words = cur_words
            return words

        stack, i, m = [], 0, len(expression)
        while i < m:
            c = expression[i]
            if c in ['{', ',']:
                stack.append(c)
            elif c == '}':
                words = set()
                while True:
                    words.update(concat_words(stack, ['{', ',']))
                    e = stack.pop()
                    if e == '{': break
                stack.append(words)
            else:
                s = c
                while i+1 < m and expression[i+1].isalpha():
                    s, i = s + expression[i+1], i+1
                stack.append(s)
            i += 1
        return sorted(concat_words(stack, []))     