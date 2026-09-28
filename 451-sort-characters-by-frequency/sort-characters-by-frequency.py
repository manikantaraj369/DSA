from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        freq = Counter(s)
        def logic(char):
            return (-freq[char],char)
        array = sorted(freq.keys(),key = logic)
        return "".join(char * freq[char] for char in array)